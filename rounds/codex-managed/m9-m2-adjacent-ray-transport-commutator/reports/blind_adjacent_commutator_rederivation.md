# Blind adjacent commutator rederivation

## 1. Result

For a finite zero-extended sequence \(f:\mathbb Z\to\mathbb C\), put

\[
 \epsilon_q=(-1)^q,\qquad d^+f(q)=f(q)-f(q+1).
\]

Then the exact finite parity high-pass identities are

\[
 \begin{aligned}
 \sum_q\epsilon_qf(q)
 &=\sum_{r\in\mathbb Z}\bigl(f(2r)-f(2r+1)\bigr)\\
 &=\sum_r d^+f(2r)
 =-\sum_r d^+f(2r+1)\\
 &=\frac12\sum_q\epsilon_qd^+f(q).
 \end{aligned}
 \tag{1.1}
\]

Apply this with \(f(q)=F_{L,a}(q)\), retaining only the forward orientation
\((2r,2r+1)\).  With

\[
 \mathcal K_L^+
 :=\sum_{a\ {\rm odd}}\sum_{q\in\mathbb Z}
       \epsilon_q\bigl(F_{L,a}(q)-F_{L,a}(q+1)\bigr),
 \tag{1.2}
\]

one obtains the exact signed commutator identity

\[
 \boxed{\ \mathcal K_L^+=2\mathfrak C_L^{\mathrm{off}}\ }.
 \tag{1.3}
\]

Consequently, under the usual absolute-value meaning of Vinogradov
notation, the weakest exact terminal signed-commutator condition is

\[
 \left|\Re\mathcal K_L^+\right|
 \ll_\varepsilon L^2X^\varepsilon.
 \tag{1.4}
\]

It is equivalent, up to the exact factor \(2\), to the stated target.  A
bound for \(|\mathcal K_L^+|\) is stronger; a total-variation, maximal,
row-energy, or Gram-norm bound is only a sufficient surrogate and generally
loses cancellation or cardinality factors.  None of those surrogate bounds
for the actual coefficient follows from the blind statement.

## 2. Exact statement and hypotheses

Let \(\mathcal A\) be a finite set and let
\(f_a:\mathbb Z\to\mathbb C\), \(a\in\mathcal A\), be finitely supported and
zero outside its literal support.  Define

\[
 \begin{gathered}
 S_a=\sum_q\epsilon_qf_a(q),\qquad
 d_a(q)=f_a(q)-f_a(q+1),\\
 \mathcal C=\sum_aS_a,\qquad
 \mathcal K=\sum_{a,q}\epsilon_qd_a(q).
 \end{gathered}
 \tag{2.1}
\]

The following quantities are distinct.

- The real signed commutator is
  \(|\Re\mathcal K|\); the complex signed commutator is \(|\mathcal K|\).
- The aggregated and rowwise total adjacent variations are, respectively,

  \[
   V_{\rm agg}=\sum_q\left|\sum_ad_a(q)\right|,
   \qquad
   V_{\rm row}=\sum_{a,q}|d_a(q)|.
   \tag{2.2}
  \]

- For
  \(S_a(Q)=\sum_{q\le Q}\epsilon_qf_a(q)\), the aggregated and rowwise
  maximal partial-sum quantities are

  \[
   M_{\rm agg}=\max_Q\left|\sum_aS_a(Q)\right|,
   \qquad
   M_{\rm row}=\sum_a\max_Q|S_a(Q)|.
   \tag{2.3}
  \]

- With
  \(n_a=|\operatorname{supp}f_a|\) and
  \(m_a=|\operatorname{supp}d_a|\), the original and difference row
  energies are

  \[
   E_0=\sum_{a,q}|f_a(q)|^2,
   \qquad
   E_\Delta=\sum_{a,q}|d_a(q)|^2.
   \tag{2.4}
  \]

- Choose the active rows \(\mathcal A\) and a finite column set
  \(\mathcal Q\subset\mathbb Z\) containing every support of \(d_a\).  Let
  \(D=(d_a(q))_{a\in\mathcal A,q\in\mathcal Q}\),
  \(G_{\rm row}=DD^*\), and \(G_{\rm col}=D^*D\).  These positive
  semidefinite Gram matrices retain cross-row or cross-column information;
  their common trace is merely \(E_\Delta\).

For these objects one has

\[
 \begin{aligned}
 |\Re\mathcal C|
 &\le |\mathcal C|=\frac12|\mathcal K|\\
 &\le \frac12V_{\rm agg}
 \le \frac12V_{\rm row},                                      \tag{2.5}\\
 |\mathcal C|&\le M_{\rm agg}\le M_{\rm row},                 \tag{2.6}\\
 |\mathcal C|
 &\le \sum_a\sqrt{n_a}\,\|f_a\|_2
 \le \sqrt{\sum_an_a}\,\sqrt{E_0},                           \tag{2.7}\\
 |\mathcal C|
 &\le \frac12\sum_a\sqrt{m_a}\,\|d_a\|_2
 \le \frac12\sqrt{\sum_am_a}\,\sqrt{E_\Delta}.             \tag{2.8}
 \end{aligned}
\]

Writing \(\boldsymbol 1\) for the all-one vector on \(\mathcal A\) and
\(\boldsymbol\epsilon=(\epsilon_q)_{q\in\mathcal Q}\), the two Gram
implications are

\[
 \begin{aligned}
 |\mathcal C|^2
 &\le \frac14|\mathcal Q|\,
       \boldsymbol1^*G_{\rm row}\boldsymbol1,                  \tag{2.9}\\
 |\mathcal C|^2
 &\le \frac14|\mathcal A|\,
       \boldsymbol\epsilon^*G_{\rm col}\boldsymbol\epsilon.  \tag{2.10}
 \end{aligned}
\]

In particular,

\[
 |\mathcal C|
 \le \frac12\sqrt{|\mathcal A|\,|\mathcal Q|}\,\|D\|_{\rm op},
 \qquad
 \|D\|_{\rm op}^2=\|G_{\rm row}\|_{\rm op}
 =\|G_{\rm col}\|_{\rm op}\le E_\Delta.
 \tag{2.11}
\]

Thus neither row energy nor an undirected Gram norm is the signed
commutator; each needs an explicit dimension or directional quadratic-form
bound.

For (B111.1), the active family is finite.  Indeed, a nonzero contribution
gives an ordered pair
\(h_1=ga,h_2=g(a+2q)\in\mathscr H_L\).  There are finitely many such pairs,
and for each pair only finitely many possible nonzero integer divisors
\(g\), after which \(a\) and \(q\) are fixed.  The \(m\)-interval is finite.
Hence the abstract hypotheses apply with \(f_a=F_{L,a}\).  The conditions
\(X\ge2\), \(J=\sqrt X\), and \(1\le L\le J^{1/2}\) are not needed for the
finite algebra; they enter only the desired analytic scale.

## 3. Proof or derivation

All sums below are finite, so index shifts have no convergence remainder.
Let \(S=\sum_q\epsilon_qf(q)\).  Since

\[
 \sum_q\epsilon_qf(q+1)
 =\sum_k\epsilon_{k-1}f(k)=-S,
\]

subtraction gives

\[
 \sum_q\epsilon_q\bigl(f(q)-f(q+1)\bigr)=2S.
 \tag{3.1}
\]

Separating even and odd indices gives the other equalities in (1.1).
Equivalently, the parity character is an eigenvector of one-step
translation with eigenvalue \(-1\), so the forward high-pass \(I-T\)
multiplies its Fourier coefficient by \(2\).

There is a mirrored backward identity with
\(d^-f(q)=f(q)-f(q-1)\), but it is not an additional contribution:

\[
 \sum_q\epsilon_qd^-f(q)=2S.
 \tag{3.2}
\]

Adding the forward and backward formulas would double-count the same
survivor.  This report fixes the single forward orientation in (1.2).

Truncation has an endpoint term.  If

\[
 K_a(Q)=\sum_{q\le Q}\epsilon_qd_a(q),
\]

then the exact partial identity is

\[
 K_a(Q)=S_a(Q)+S_a(Q+1)
       =2S_a(Q)+\epsilon_{Q+1}f_a(Q+1).
 \tag{3.3}
\]

Only after \(Q\) has passed the support does the last term vanish.  Hence,
with \(M_{\Delta,a}=\max_Q|K_a(Q)|\),

\[
 \max_Q|S_a(Q)|
 \le\frac12\left(M_{\Delta,a}+\|f_a\|_\infty\right),
 \qquad
 M_{\Delta,a}
 \le2\max_Q|S_a(Q)|+\|f_a\|_\infty.
 \tag{3.4}
\]

This is why a maximal claim is not the terminal commutator identity with a
supremum inserted.

Taking absolute values in (3.1), first after aggregating in \(a\) and then
before aggregating, proves (2.5).  Equation (2.6) follows because, after the
last support point, the relevant partial sum equals the full sum.  Applying
Cauchy--Schwarz on each row and then in \(a\) proves (2.7) and (2.8).

For the Gram claims,

\[
 \mathcal K=\boldsymbol1^*D\boldsymbol\epsilon.
 \tag{3.5}
\]

Cauchy--Schwarz first in the column space yields

\[
 |\mathcal K|^2
 \le |\mathcal Q|\,\|D^*\boldsymbol1\|_2^2
 =|\mathcal Q|\,\boldsymbol1^*G_{\rm row}\boldsymbol1;
\]

Cauchy--Schwarz first in the row space yields

\[
 |\mathcal K|^2
 \le |\mathcal A|\,\|D\boldsymbol\epsilon\|_2^2
 =|\mathcal A|\,\boldsymbol\epsilon^*G_{\rm col}
                         \boldsymbol\epsilon.
\]

Using \(\mathcal K=2\mathcal C\) proves (2.9)--(2.11).  The difference Gram
itself has the exact adjacent-correlation expansion

\[
 \begin{aligned}
 (G_{\rm row})_{ab}
 &=2\sum_qf_a(q)\overline{f_b(q)}
   -\sum_qf_a(q)\overline{f_b(q+1)}\\
 &\hspace{18mm}
   -\sum_qf_a(q+1)\overline{f_b(q)},
 \end{aligned}
 \tag{3.6}
\]

where zero extension makes the two unshifted terms exactly equal and
prevents a hidden endpoint remainder.

If a row has first and last nonzero locations \(u\) and \(v\), then
\(d_a\) is supported inside \([u-1,v]\), with the literal birth and death
terms

\[
 d_a(u-1)=-f_a(u),\qquad d_a(v)=f_a(v).
 \tag{3.7}
\]

Internal support births, deaths, holes, and coefficient changes are likewise
already present in \(d_a(q)\).  For the actual row, \(q<1\) is zero, so a
birth at \(q=1\) contributes \(d_a(0)=-F_{L,a}(1)\).  The half-open
membership of \(\mathscr H_L\), all floors, stars, collars, half weights, and
empty \(m\)-ranges are kept literally inside \(F_{L,a}\); no endpoint is
smoothed or translated.  The orientation is exactly the ordered \(q\ge1\)
orientation in (B111.1); no reflected negative-\(q\) row or symmetry factor
has been introduced.

Finally, (1.3) gives

\[
 |\Re\mathfrak C_L^{\mathrm{off}}|
 =\frac12|\Re\mathcal K_L^+|.
 \tag{3.8}
\]

Thus (1.4), with the exact factor \(2\) absorbed by the implied constant,
is the weakest terminal commutator implication into (B111.3).  If
(B111.3) is intended as a one-sided inequality rather than the standard
absolute Vinogradov bound, the same statement holds after removing both
absolute-value signs in (3.8).

## 4. First doubtful or unproved step

The first unproved step is any nontrivial estimate for
\(\mathcal K_L^+\), \(V_{\rm agg}\), \(V_{\rm row}\), a maximal quantity,
\(E_\Delta\), or one of the directional Gram quadratic forms at the scale
\(L^2X^\varepsilon\).  Formula (B111.1) supplies finiteness but supplies no
regularity in \(q\).  Passing from the exact difference

\[
 F_{L,a}(q)-F_{L,a}(q+1)
\]

to a small adjacent-ray error would require a proved transport or matching
of the changing \(g\)-support, \(m\)-endpoints, phases, floors, stars, half
weights, collars, entry/exit data, profiles, and zero extensions.  No such
matching is present in the allowed statement.  In particular, it is not
valid to differentiate or Lipschitz-bound the literal actual coefficient,
to discard births and deaths, or to replace the signed commutator by row
energy without the losses displayed above.

## 5. Required control test and outcome

- **Empty row.**  Input: \(f\equiv0\).  Expected invariant: every terminal,
  maximal, variation, energy, and Gram quantity is zero.  Observed: (1.1),
  (3.3), and (3.7) all give zero.  Implication: empty \(m\)-ranges and empty
  actual rows create no exceptional term.

- **Singleton and both zero-extension endpoints.**  Input:
  \(f(q_0)=c\ne0\) and \(f(q)=0\) otherwise.  Expected invariant:
  \(\mathcal K=2S\) with both boundary jumps retained.  Observed:

  \[
   S=\epsilon_{q_0}c,\quad
   d(q_0-1)=-c,\quad d(q_0)=c,\quad
   V=2|c|,\quad \mathcal K=2\epsilon_{q_0}c.
  \]

  Implication: the factor \(1/2\) in the variation bound is sharp, and
  omitting either the birth or death term breaks the identity.  For
  \(q_0=1\), the required left endpoint is the zero-extended value at
  \(q=0\).

- **Truncated endpoint.**  Input: the same singleton at \(q_0=Q+1\).
  Expected failure: the false partial formula \(K(Q)=2S(Q)\) should fail.
  Observed: \(S(Q)=0\) but
  \(K(Q)=\epsilon_{Q+1}c\), exactly the endpoint term in (3.3).
  Implication: terminal identities cannot be promoted to maximal identities
  without the boundary correction.

- **Adversarial parity coefficients.**  Input:
  \(f_N(q)=\epsilon_qc\) for \(1\le q\le N\), zero otherwise.  Expected
  failure: finiteness or row energy alone should not force parity
  cancellation.  Observed:

  \[
   S_N=Nc,\quad V_N=2N|c|,\quad E_{0,N}=N|c|^2,
   \quad E_{\Delta,N}=(4N-2)|c|^2.
  \]

  Implication: the support-cardinality losses in (2.7)--(2.8) are necessary
  for arbitrary finite coefficients; the variation bound can be attained
  exactly.

- **Large maximal sum with zero terminal commutator.**  Input:
  \(f(q)=\epsilon_qc\) for \(1\le q\le N\) and
  \(f(q)=-\epsilon_qc\) for \(N<q\le2N\).  Expected failure: a maximal
  bound should not be identified with the final signed sum.  Observed: the
  terminal sum is zero, while the maximum partial-sum magnitude is
  \(N|c|\).  Implication: maximal control is strictly stronger than the
  terminal claim.

- **Large total variation with zero signed survivor.**  Input:
  \(f(2r)=f(2r+1)=c_r\) for \(1\le r\le N\), with zero extension and, for
  example, \(c_r=(-1)^rc\).  Expected failure: total variation should not be
  necessary for a small signed commutator.  Observed: each adjacent parity
  pair cancels, so \(S=0\), whereas

  \[
   V=|c_1|+\sum_{r=1}^{N-1}|c_r-c_{r+1}|+|c_N|
  \]

  grows linearly in \(N|c|\).  Implication: total variation is a stronger
  unsigned surrogate, not an equivalent form of signed cancellation.

- **Gram coherence adversary.**  Input: take a fixed finite row \(f\) with
  signed sum \(s\ne0\), and \(M\) rows \(f_a=\omega_af\),
  \(|\omega_a|=1\).  Compare \(\omega_a=1\) with phases satisfying
  \(\sum_a\omega_a=0\).  Expected failure: diagonal row energies, the trace,
  or a generic Gram operator norm should not determine the total signed
  survivor.  Observed: both inputs have the same row energies, Gram trace,
  and Gram operator norm, but the first has total \(Ms\) and the second has
  total \(0\); correspondingly
  \(\boldsymbol1^*G_{\rm row}\boldsymbol1\) is respectively
  \(M^2\|d\|_2^2\) and \(0\).  Implication: the directional Gram quadratic
  form, including off-diagonal phases, cannot be replaced by diagonal
  energy data.

These are exact finite symbolic controls, not numerical evidence.  They
show that all endpoint identities survive arbitrary coefficients, while
every proposed analytic saving can fail for an arbitrary finite
coefficient row.  They therefore do not establish, or purport to model,
regularity of the literal coefficient \(A_L\).

## 6. Dependencies and exact artifacts used

- problems/gauss_circle.md: only the ambient Gauss-circle research goal.
- state/control_models.md: the requirements to separate signed and
  unsigned claims, test coefficient adversaries, and audit support and
  degeneracy.
- rounds/codex-managed/m9-m2-adjacent-ray-transport-commutator/blind_statement.md:
  the literal row (B111.1), survivor (B111.2), target (B111.3), parameter
  range, and isolation restrictions.

No proof graph, strategy file, Round-111 derivation packet or candidate,
prior-round derivation, or sibling Round-111 report was consulted.

## 7. Recommended state effect

**Promote only the finite algebraic lemma** (1.1)--(1.3), including the
zero-extension endpoint and one-orientation conventions, and the exact
norm implications (2.5)--(2.11).  **Retain the analytic commutator estimate
as open:** the blind statement does not prove (1.4), any suitable variation,
maximal, energy, or directional Gram bound, or any \(q\)-regularity of the
actual coefficient.  Accordingly, this report recommends no promotion of
(B111.3) itself.

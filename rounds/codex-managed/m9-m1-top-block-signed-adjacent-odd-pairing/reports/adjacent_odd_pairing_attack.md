# Round 57 discovery report: exact adjacent-odd decomposition and an unmatched-endpoint obstruction

## 1. Result: pairing identity plus strict scoped no-go

On \(R/4<h\leq R/2\), every fixed-\(h\) row in a length-\(R\)
product window contains zero, one, or two odd denominators. When it
contains two, they are necessarily \(q,q+2\), and the exact signed row is

\[
 \chi_4(q)e(\sqrt{Xhq})
 \left\{\mathcal A_X(h,q)
 -\mathcal A_X(h,q+2)e(\Theta_h(q))\right\},                \tag{1.1}
\]

\[
 \Theta_h(q)=\frac{2\sqrt{Xh}}{\sqrt{q+2}+\sqrt q}.          \tag{1.2}
\]

There is an exact global decomposition into these matched rows and
unmatched singleton rows, with no reassigned half weights. The matched
bracket obeys

\[
\begin{split}
 \mathcal A_X(h,q)-\mathcal A_X(h,q+2)e(\Theta_h(q))
 ={}&\mathcal A_X(h,q)-\mathcal A_X(h,q+2)\\
 &+\mathcal A_X(h,q+2)\{1-e(\Theta_h(q))\}.                 \tag{1.3}
\end{split}
\]

Neither term is uniformly small: the actual top plateau can make the
first exactly zero, while \(\|\,\Theta_h(q)\,\|\) may be bounded away from
zero; at hard-profile or equality-star seams the first term can have order
one.

More decisively, adjacent-odd pairing cannot by itself prove the required
\(O(\sqrt R)\) aggregate by endpoint counting or post-pair absolute
values. There are infinitely many perfect fourth powers \(X=K^4\) and
strict star-free actual-profile windows \(J_K\) with
\(\gg K\asymp R\) unmatched high-shell rows, each of amplitude at least
\(1/2\). Hence the exact post-pair majorant satisfies

\[
 \boxed{
 \sum_{h\in\mathcal H_1(J_K)}
 |\mathcal A_X(h,q_h)|\gg R.}                               \tag{1.4}
\]

This no-go is sharply scoped. It refutes a deterministic
\(O(\sqrt R)\) unmatched-endpoint count and every route taking absolute
values after pairing. It is not a signed lower bound for \(P_J\):
cross-\(h\) phase cancellation could still reduce the unmatched sum, and
that is the exact survivor.

## 2. Exact statement and hypotheses

Let \(J=[A,B]\cap\mathbb Z\), \(B-A+1\leq R\), and put

\[
 \mathcal Q_h(J)=\{q\geq1:q\ {\rm odd},\ hq\in J\}.          \tag{2.1}
\]

Since consecutive members differ by two and their products by \(2h\),

\[
 \#\mathcal Q_h(J)
 \leq 1+\left\lfloor\frac{B-A}{2h}\right\rfloor\leq2
 \quad(R/4<h\leq R/2).                                     \tag{2.2}
\]

Define

\[
 \mathcal H_2(J)=\{h:R/4<h\leq R/2,\ \#\mathcal Q_h(J)=2\},
\]

\[
 \mathcal H_1(J)=\{h:R/4<h\leq R/2,\ \#\mathcal Q_h(J)=1\}. \tag{2.3}
\]

For \(h\in\mathcal H_2(J)\), write
\(\mathcal Q_h(J)=\{q_h,q_h+2\}\). For
\(h\in\mathcal H_1(J)\), write \(\mathcal Q_h(J)=\{q_h\}\).
All inherited radial and angular equality stars remain inside
\(\mathcal A_X(h,q)\); artificial window endpoints create no new stars.
The exact matched/unmatched decomposition is

\[
\boxed{
\begin{split}
 P_J={}&
 \sum_{h\in\mathcal H_2(J)}
 \chi_4(q_h)e(\sqrt{Xhq_h})
 \{\mathcal A_X(h,q_h)
 -\mathcal A_X(h,q_h+2)e(\Theta_h(q_h))\}\\
 &+\sum_{h\in\mathcal H_1(J)}
 \chi_4(q_h)\mathcal A_X(h,q_h)e(\sqrt{Xhq_h}).
                                                               \tag{2.4}
\end{split}}
\]

The two-point geometry is exact. If
\[
 q_h=\min\{q\ {\rm odd}:hq\geq A\},
\]
then

\[
 h\in\mathcal H_2(J)\iff h(q_h+2)\leq B,                   \tag{2.5}
\]

and otherwise the row is unmatched. Thus the matched count depends on
the fractional alignment of \(A/h\); the inequality \(2h\leq|J|\) is
necessary but not sufficient.

The exact phase-increment derivatives, useful only after both points are
present, are

\[
 \Theta_h(q)=\sqrt{Xh}\,(\sqrt{q+2}-\sqrt q),               \tag{2.6}
\]

\[
 \Theta_h(q)
 =\frac{\sqrt X\,h}{\sqrt{hq}}
 \left(1+O\left(\frac h{hq}\right)\right)
 \asymp hR,                                                 \tag{2.7}
\]

uniformly for \(hq\asymp R^2\). Consequently

\[
 |1-e(\Theta_h(q))|
 \asymp \min\{1,\|\Theta_h(q)\|\}                           \tag{2.8}
\]

up to absolute constants; no smallness follows from the character sign.

## 3. Proof and derivation

### 3.1 Pairing identity and owner ledger

Equation (2.2) follows because three odd denominators would span product
length \(4h>R\), impossible in \(J\). If two occur, they are consecutive
odd integers. The character identity

\[
 \chi_4(q+2)=-\chi_4(q)
\]

and phase factorization

\[
 e(\sqrt{Xh(q+2)})
 =e(\sqrt{Xhq})e(\Theta_h(q))
\]

give (1.1), and adding and subtracting
\(\mathcal A_X(h,q+2)\) gives (1.3). Summing the disjoint row cases gives
(2.4).

The left product owns \(\mathcal A_X(h,q)\) and all of its floors,
profiles, hard-top and equality stars; the right product separately owns
\(\mathcal A_X(h,q+2)\) and its stars. The artificial tests
\(hq\geq A\) and \(hq\leq B\) are full cutoffs even at equality. No
window-created half weight appears.

### 3.2 Local amplitude difference

Away from a hard-profile or equality-star seam, the actual formula and
the bounded derivatives of \(W\) and \(\Phi\) give the local estimate

\[
 |\mathcal A_X(h,q+2)-\mathcal A_X(h,q)|
 \ll \frac hY.                                               \tag{3.1}
\]

Indeed, with \(n=hq\) and \(d=2\sqrt{Xh/q}\),

\[
 \frac{|d(h,q+2)-d(h,q)|}{d(h,q)}
 =1-\sqrt{\frac q{q+2}}\ll\frac1q\asymp\frac hY.            \tag{3.2}
\]

Only \(O(1)\) dyadic profiles meet the short angular interval, and for
fixed \(h\) all height and Vaaler factors are constant. This proves
(3.1) on smooth pieces. If one step crosses the one-sided top cutoff or
an angular equality-star sample, the difference can be \(O(1)\); the
fixed-\(h\) sampled-BV theorem counts such events but supplies no local
\(h/Y\) gain. Thus the exact uniform statement is

\[
 |\mathcal A_X(h,q+2)-\mathcal A_X(h,q)|
 \ll \frac hY+\mathbf1_{\mathcal E}(h,q),                   \tag{3.3}
\]

where \(\mathcal E\) is the set of actual hard-top or equality-star seams
crossed by the adjacent pair. The height factors are constant in a
fixed-\(h\) row and create no \(q\)-difference seam. Equation (3.3) is an owner
ledger, not a claim that the seam count is target-sized after summing
over \(h\).

On the top-profile unit plateau the difference vanishes exactly, but
(1.3) reduces there to
\[
 \mathcal A_X(h,q)\{1-e(\Theta_h(q))\}.
\]
It is small only near integer \(\Theta_h(q)\); sign reversal alone is not
cancellation.

### 3.3 Unmatched endpoints can have full density

The availability condition (2.5) is alignment-sensitive. In particular,
if \(J\) contains only products in a single parity class of the quotient
for many \(h\), those rows are unmatched even though \(2h<R\). There is no
deterministic \(O(\sqrt R)\) bound on \(\#\mathcal H_1(J)\): the strict
family below has \(\#\mathcal H_1(J)\gg R\).

The cross-\(h\) phase produced by the exact pairing is not a smooth
one-variable phase. Explicitly,
\[
 q_h=2\left\lceil\frac{A/h-1}{2}\right\rceil+1,\qquad
 n_h=hq_h=A+\delta_h,\qquad0\leq\delta_h<2h,
\]
\[
 h\in\mathcal H_2(J)\iff \delta_h+2h\leq B-A,
\]
and
\[
 \sqrt{Xn_h}
 =\sqrt{XA}+
 \frac{\sqrt X\,\delta_h}{\sqrt{A+\delta_h}+\sqrt A}.
\]
The rounding sawtooth \(\delta_h\) jumps when \(A/h\) crosses an odd
integer. Differentiating a schematic \(\sqrt{Xhq(h)}\) in \(h\) while
discarding these jumps is therefore unlawful; any cross-\(h\) estimate
must control this exact sawtooth phase.

This also shows why completing a singleton row by adjoining the missing
\(q+2\) outside \(J\) is unlawful. It would add an artificial boundary
term of the same order as the original row. The inherited stars cannot be
moved to that artificial point.

### 3.4 Strict fourth-power unmatched-endpoint family

Let \(K\) run through positive multiples of \(16\), and set

\[
 X=K^4,\qquad R=K,\qquad Y=K^2,\qquad
 \mathcal H_K=[3K/8,7K/16]\cap\mathbb Z.                    \tag{3.4}
\]

For an integer start \(A\), put
\[
 J_A=[A,A+K-1]\cap\mathbb Z.
\]
For fixed \(h\), the odd products form the single residue class
\(h\bmod 2h\), of spacing \(s_h=2h\). Since
\[
 3K/4\leq s_h\leq7K/8<K<2s_h,
\]
every \(J_A\) contains one or two odd products. As \(A\) runs through one
complete period modulo \(s_h\), exactly
\[
 2s_h-K=4h-K                                                 \tag{3.5}
\]
starting residues give exactly one product. Indeed the average number of
lattice points is \(K/s_h\), and the only possibilities are one and two.
Thus the unmatched proportion is
\[
 2-\frac K{2h}\geq\frac23.                                  \tag{3.6}
\]

Average \(A\) over the integer interval
\[
 \mathcal I_K=[15K^2/16,\ K^2-K]\cap\mathbb Z,               \tag{3.7}
\]
whose length \(T\asymp K^2\). For each fixed \(h\), splitting
\(\mathcal I_K\) into complete periods and at most two remainders gives
\[
 \sum_{A\in\mathcal I_K}\mathbf1_{\{h\in\mathcal H_1(J_A)\}}
 \geq \frac23T-O(h).
\]
Summing over \(h\in\mathcal H_K\), and using
\(\#\mathcal H_K\asymp K\), \(\sum_{\mathcal H_K}h=O(K^2)\), yields
\[
 \sum_{A\in\mathcal I_K}\#\big(\mathcal H_1(J_A)\cap\mathcal H_K\big)
 \gg TK.                                                     \tag{3.8}
\]
Hence some \(A_K\in\mathcal I_K\) satisfies
\[
 \#\big(\mathcal H_1(J_{A_K})\cap\mathcal H_K\big)\gg K.     \tag{3.9}
\]

Every incidence in these windows is strictly on the actual top plateau.
Indeed \(n=hq\in[15K^2/16,K^2]\), so
\[
 \frac{2\sqrt{Xh/q}}{\sqrt X}
 =\frac{2h}{\sqrt n}
 \in\left[\frac34,\frac{7}{8}\sqrt{\frac{16}{15}}\right]
 \Subset(2/3,1).                                             \tag{3.10}
\]
The finer profiles vanish, the top height is \(H_0=K>h\), and no hard,
angular, or radial star occurs. Therefore
\[
 \mathcal A_X(h,q)=\Phi\left(\frac h{K+1}\right)\geq\frac12.
                                                                    \tag{3.11}
\]
Equations (3.9)--(3.11) prove the strict post-pair endpoint majorant
\[
 \sum_{h\in\mathcal H_1(J_{A_K})}
 |\mathcal A_X(h,q_h)|\gg K=R,                              \tag{3.12}
\]
which is (1.4).

### 3.5 Perfect-fourth-power signed control

The construction above proves endpoint capacity, not signed coherence.
A one-point window near \(K^2\) would make all radial phases equal, but
then its high-shell incidences are indexed by divisors of one integer and
are only \(K^{o(1)}\), not \(\gg K\). Conversely, the familiar coherent
products \(K^2-t^2\) do not form a consecutive physical window. These
controls prevent upgrading (3.12) to a signed lower bound.

For the actual consecutive \(J_{A_K}\), the unmatched phase is
\(e(K^2\sqrt{hq})\), whose variation across a length-\(K\) window includes
a quadratic scale of order \(K\). No constant-sign conclusion follows.
For every matched plateau row, the exact bracket also passes all three
mandatory alignments:

\[
 \Theta_h(q)\in\mathbb Z
 \ \Longrightarrow\ 1-e(\Theta_h(q))=0,
\]
\[
 \Theta_h(q)\in\mathbb Z+\tfrac12
 \ \Longrightarrow\ 1-e(\Theta_h(q))=2,
\]
while \(\|\Theta_h(q)\|\geq c>0\) gives
\(|1-e(\Theta_h(q))|\gg_c1\). At \(X=K^4\), the leading local expansion
near \(hq=K^2\) is \(\Theta_h(q)=Kh+O(h)\); its integer leading term does
not control the exact correction modulo one. Thus integral alignment is
favourable, half-integral alignment is maximally unfavourable, and neither
may be assumed uniformly.

The exact lawful verdict is therefore
\[
 \boxed{\#\mathcal H_1(J_{A_K})\gg R,\quad
 \sum_{h\in\mathcal H_1(J_{A_K})}|\mathcal A_X(h,q_h)|\gg R,
 \quad |P_J|\ll R,}                                         \tag{3.13}
\]
while the signed \(O(\sqrt R)\) estimate remains open.

### 3.6 High-shell exponent ledger

There are \(O(R)\) admissible \(h\)'s, at most \(O(R)\) original
incidences, at most one matched bracket per \(h\), and at most one
unmatched singleton per \(h\). The unweighted ledger is:

| owner/method | available bound | target ratio |
|---|---:|---:|
| original absolute rows | \(R\) | \(\sqrt R\) too large |
| unmatched endpoints by counting | \(R\) | \(\sqrt R\) too large |
| amplitude-difference smooth part | \(\sum_h h/Y=O(1)\) | safe |
| amplitude seam part | \(R\) without a cross-\(h\) theorem | \(\sqrt R\) too large |
| phase-difference brackets | \(\sum_h\min(1,\|\Theta_h(q_h)\|)\leq R\) | \(\sqrt R\) too large |
| required signed aggregate | \(\sqrt R\) | target |

Thus the smooth amplitude difference is genuinely harmless. The two
survivors are unmatched endpoints and the signed \(h\)-sum of phase
increments, with any actual seams retained.

Restoring \((hq)^{-3/4}\asymp R^{-3/2}\), the \(R\)-capacity rows become
\(R^{-1/2}=Y^{-1/4}\), while the desired \(\sqrt R\) row becomes
\(R^{-1}=Y^{-1/2}\). The exact normalized excess is therefore
\(\sqrt R=Y^{1/4}\).

## 4. First doubtful or unproved step

The first unproved step is a signed cross-\(h\) theorem for the exact
objects produced by (2.4):

\[
\begin{split}
 &\left|
 \sum_{h\in\mathcal H_2(J)}
 \chi_4(q_h)e(\sqrt{Xhq_h})
 \mathcal A_X(h,q_h+2)\{1-e(\Theta_h(q_h))\}\\
 &\qquad+
 \sum_{h\in\mathcal H_1(J)}
 \chi_4(q_h)\mathcal A_X(h,q_h)e(\sqrt{Xhq_h})
 \right|
 \ll_\varepsilon X^\varepsilon\sqrt R,                     \tag{4.1}
\end{split}
\]

plus the seam part from (3.3). The smooth amplitude-difference part is
\(O(1)\).

No strict signed obstruction to (4.1) has been proved: the natural
perfect-fourth-power signed-coherence candidates fail either divisor
multiplicity or consecutive-window geometry. Equally, no square-root
estimate follows merely from
\(\chi_4(q+2)=-\chi_4(q)\), because pair availability and
\(\Theta_h(q)\) remain uncontrolled.

Even a proof of (4.1) would close only \(R/4<h\leq R/2\). The lower sector
\((\log X)^B<h\leq R/4\), the full residual core, and the alpha transfer
would remain open.

## 5. Required control tests and outcomes

| control | outcome |
|---|---|
| `pairing_identity` | Pass. Equations (1.1)--(1.3) and (2.4) retain both actual amplitudes and the exact sign reversal. |
| `two_point_window_geometry` | Pass. Equations (2.2) and (2.5) characterize pair availability; \(2h\leq|J|\) alone is not sufficient. |
| `phase_increment` | Open as a signed aggregate. Equations (2.6)--(2.8) are exact and show that character reversal supplies no automatic smallness. |
| `amplitude_difference` | Scoped pass. The smooth contribution is \(O(h/Y)\); hard-profile or equality-star crossings can be \(O(1)\) and remain explicit. |
| `unmatched_endpoints` | Sharp counting obstruction. The strict family (3.4)--(3.12) has \(\gg R\) unmatched full-amplitude rows, and artificial completion reproduces their boundary cost. No signed coherence is claimed. |
| `cross_h_aggregation` | Open. Formula (4.1) is the exact remaining signed theorem. |
| `perfect_fourth_power` | Pass as a hostile control. Perfect fourth powers give the strict endpoint-capacity family; the one-point coherent candidate lacks enough divisors and the \(K^2-t^2\) candidate is not a consecutive window, so no signed no-go is licensed. |
| `target_ledger` | Pass. Section 3.6 isolates the safe smooth amplitude term and the two \(R\)-capacity survivors. |
| `lower_shell_scope` | Pass. Only \(R/4<h\leq R/2\) is considered; the lower residual sector remains untouched. |
| `downstream_scope` | Pass. No GAR, alpha, M9-M1, M9, or exponent promotion is asserted. |

## 6. Dependencies and exact artifacts used

Only the task-authorized artifacts were used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `rounds/codex-managed/m9-m1-top-block-signed-adjacent-odd-pairing/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-top-block-intermediate-h-resonance/synthesis.md`;
- `rounds/codex-managed/m9-m1-top-block-low-leg-curvature/synthesis.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.

All pairing, window, amplitude, endpoint, and exponent calculations are
internal. No external theorem, web source, or numerical experiment was
used. The report is 100% analytical/algebraic.

## 7. Recommended state effect

Promote, after independent validation, the exact adjacent-odd
matched/unmatched decomposition (2.4), the pair-existence criterion (2.5),
the phase increment (2.6)--(2.8), and the smooth-versus-seam amplitude
ledger (3.1)--(3.3).

Promote only the scoped capacity no-go: taking absolute values after the
pairing, or assuming sign reversal alone makes a pair small, cannot prove
the \(\sqrt R\) target. Do **not** promote a signed lower bound; the two
natural fourth-power constructions fail the mandatory multiplicity or
window controls.

Retain (4.1), the lower shell, full residual core, GAR, alpha transition,
M9-M1, M9, and the final theorem open. The next attack must study the
joint \(h\)-phase of matched phase brackets and unmatched endpoints,
without absolute values.

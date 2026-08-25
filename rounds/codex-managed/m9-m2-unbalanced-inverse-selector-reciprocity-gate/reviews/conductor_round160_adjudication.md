# Round 160 conductor adjudication

- Campaign: m9-m2-unbalanced-inverse-selector-reciprocity-gate
- Round: 160
- Task: conductor_round160_adjudication
- Role: conductor adjudication
- Generated at: 2026-08-25T19:00:54+08:00
- Starting graph:
  4ad56f62aeb814c11c31fe655bc48da6d74639e3bd61077e9496d647c366c41d
- Terminal label: inverse_selector_projective_capacity_no_go
- Allocation: 100% analytical, algebraic, and primary-source work;
  0% numerical experimentation

## 1. Result

Round 160 closes under
**inverse_selector_projective_capacity_no_go**, with a strict route
qualification.

The round proves the exact shorter-modulus reciprocity representation of
the already centered flat-smooth strict-UNBAL owner. It independently
checks the sign, arbitrary inverse representatives, even and odd \(j\),
the \(1/(gnj)\) normalization, both \(\chi_4\) directions, and complete
\(h\)-reconstruction. Complete frequency summation returns the original
reciprocal row; the already safe \(h=0\pmod n\) Ramanujan row is removed
exactly once.

The genuinely new finite statement is an exact projective-capacity
obstruction for the unweighted inverse-residue kernel. For any
\(A\subseteq(\mathbb Z/j\mathbb Z)^\times\), \(M=|A|\), the nonzero
residue matrix

\[
 F_{j,A}(u,h)=e(h\overline u_j/j),
 \qquad u\in A,\quad 1\le h\le j-1,
\]

satisfies

\[
 F_{j,A}F_{j,A}^*=jI_M-\mathbf1\mathbf1^*.
\tag{160.A1}
\]

Its exact nuclear-to-Hilbert--Schmidt inflation is \(\gg\sqrt M\).
For all unit classes this is \(j^{1/2-o(1)}\). The literal positive block
\(1\le h\le j\), normalized by \(j^{-1/2}\), has orthonormal rows and
exact inflation \(\sqrt{\varphi(j)}\). Thus deleting the original
\(h=0\pmod n\) row does not make the short-modulus kernel low-rank.

The full long-\(h\) range supplies the independent sharp operator control

\[
 \|P_{n,j}\|_{2\to2}
 =\sqrt{\left\lceil\frac{n-1}{j}\right\rceil}
 \asymp\sqrt\Delta.
\tag{160.A2}
\]

In particular, all positive frequencies \(h=mj<n\) remain, their short
inverse phase is \(1\), and the reciprocity correction is \(1+O(1/j)\).

At \(g=1\), \(j\asymp K\), the scalar projective price
\(K^{1/2-o(1)}\) and the long-block scale \(X^{a/2}\) each exceed the
entire missing boundary power at every fixed strict exponent pair. The
audited scalar Bettin--Chandee/Wright, Blomer--Milićević,
Deshouillers--Iwaniec, and Assing--Blomer--Li interfaces do not absorb
the joint Kloosterman coefficient, projective charge, long complement,
moving support, high additive bandwidth, or growing spectral levels.

This proves only that exact unweighted Hilbert rank-one scalarization,
followed termwise by a triangle inequality, and the named audited scalar
realizations are not low-cost continuations. It does not lower-bound the
literal signed scalar or weighted matrix, and it does not exclude a new
coefficient-sensitive vector theorem.

No target estimate, strict owner-complete range, downstream theorem, or
global exponent improvement is proved.

## 2. Exact accepted statement and hypotheses

Let

\[
 X=N_0+\xi,\quad D=X^\delta,\quad L=X^\ell,\quad
 R=X/D,\quad K=XL/D^2,\quad
 \Delta=D/L,\quad a=\delta-\ell,
\tag{160.A3}
\]

where

\[
 \frac14\le\delta<\frac12,\qquad
 0\le\ell<\delta-\frac14,\qquad
 178\ell+1638\delta>463.
\tag{160.A4}
\]

Retain odd \(g,n\), \(gn\asymp R\), arbitrary parity of \(j\),
\((j,n)=1\), arbitrary \((N_0,n)\), all \(1\le h<n\), the literal
moving \(j\)-support with zero extension, both character directions,
real-centre factors, profiles, entries, exits, transitions, and
endpoints.

For

\[
 b_{g,n}(j)=\frac{q_L(4Xj/(gn^2))}{gj}e(\xi j/n),
\]

the exact identity

\[
 e(-h\overline j_n/n)
 =e(h\overline n_j/j-h/(jn))
\tag{160.A5}
\]

gives the termwise scalar

\[
 \frac{\chi_4(g)\chi_4(n)}{gnj}
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
 e\!\left(\frac{\xi j}{n}+\frac{h\overline n_j}{j}
                 -\frac{h}{jn}\right)S(N_0,h;n).
\tag{160.A6}
\]

The complete reconstruction is

\[
 \sum_{h\bmod n}\widehat\gamma_{g,n}(h)S(N_0,h;n)
 =\sum_{\substack{j\in\mathcal J_{g,n}\\(j,n)=1}}
 b_{g,n}(j)e(N_0j/n).
\tag{160.A7}
\]

The factor \(e(\xi j/n)\) in \(b_{g,n}(j)\) restores the original
\(e(Xj/n)\) row. The centered scalar is (160.A7) minus
\(\widehat\gamma_{g,n}(0)c_n(N_0)\) exactly once.

For the matrix in (160.A1), the exact spectrum is

\[
 \operatorname{sing}(F_{j,A})
 =\{\sqrt j\ (M-1\text{ times}),\sqrt{j-M}\},
\tag{160.A8}
\]

\[
 \|F_{j,A}\|_{S_1}=(M-1)\sqrt j+\sqrt{j-M},
 \qquad
 \|F_{j,A}\|_{S_2}^2=M(j-1).
\tag{160.A9}
\]

Every exact Hilbert rank-one factorization
\(F_{j,A}=\sum_\nu u_\nu v_\nu^*\) therefore satisfies

\[
 \sum_\nu\|u_\nu\|_2\|v_\nu\|_2
 \ge\|F_{j,A}\|_{S_1}.
\tag{160.A10}
\]

If all \(j\) residue columns are kept and the kernel is normalized by
\(j^{-1/2}\), the rows are orthonormal. This gives exact nuclear and
Hilbert--Schmidt norms \(M\) and \(\sqrt M\), respectively.

The additive expansion

\[
 \mathbf1_{(n,j)=1}e(h\overline n_j/j)
 =\frac1j\sum_{t\bmod j}S(h,-t;j)e(tn/j)
\tag{160.A11}
\]

is exact. A fixed proportion of its joint coefficient mass lies at
centered \(|t|\asymp j\). This last conclusion is promoted only as a
finite Fourier diagnostic, not as a source-independent automorphic
Sobolev statement.

## 3. Power and source adjudication

The required saving exponent is

\[
 \mu(a)=
 \begin{cases}
 a-\frac14,&1/4<a\le1/3,\\[1mm]
 \frac{1-2a}{4},&1/3\le a<1/2.
 \end{cases}
\tag{160.A12}
\]

At \(g=1\),

\[
 K=X^{1+\ell-2\delta}=X^{1-\delta-a}.
\tag{160.A13}
\]

For the projective scale,

\[
 \frac{1-\delta-a}{2}-\mu(a)
 =\begin{cases}
 \dfrac{3-2\delta-6a}{4}>0,&a\le1/3,\\[2mm]
 \dfrac{1-2\delta}{4}>0,&a\ge1/3.
 \end{cases}
\tag{160.A14}
\]

For the long block,

\[
 \frac a2-\mu(a)
 =\begin{cases}
 \dfrac14-\dfrac a2,&a\le1/3,\\[2mm]
 \dfrac{4a-1}{4},&a\ge1/3,
 \end{cases}
 \quad>0.
\tag{160.A15}
\]

Both comparisons are pointwise at fixed strict exponent pairs. No
uniform positive margin is asserted at the open face \(\delta=1/2\).

The audited primary-source seam is:

1. The Bettin--Chandee and Wright trilinear theorems accept independent
   scalar coefficient sequences, not the simultaneous moving factor
   \(S(N_0,h;n)\). Opening that factor and completing \(h\) returns
   (160.A7).
2. Blomer--Milićević accepts one arithmetic modulus weight, but for
   \(j=p\) prime the normalized Mellin \(L^1\) norm of
   \(u\mapsto e(h\overline u_p/p)\) is \(\asymp p\), not \(O(1)\).
3. Legal arithmetic encoding has period
   \(\operatorname{lcm}(4,j)\). For \(j=p\) prime it creates levels
   \(4,8,4p,8p\) for the odd principal \(p\)-character and
   \(4p,8p,4p^2,8p^2\) for nonprincipal characters. For \(p\ge5\),
   both parities occur across the latter conductor-\(4p\) family; every
   induced level retains all compatible holomorphic, Maaß, exceptional,
   Eisenstein, newform, and oldclass terms.
4. The scalar Linnik range
   \(h\ll K/(Lg^2)\) covers only a proportion \(\asymp1/(Dg)\) of the
   complete physical row.
5. Deshouillers--Iwaniec and Assing--Blomer--Li retain fixed scalar
   coefficient and smoothness interfaces. The moving \(h\)-dependent
   residue weight and high additive bandwidth do not enter at free cost.
   Assing--Blomer--Li also has no \(\chi_4(c)\) modulus twist; encoding
   it on odd moduli costs normalized frequency \(\asymp R/g\).

These are theorem-hypothesis mismatches and route capacities, not
impossibility theorems.

## 4. First doubtful or unproved step

The first missing step in transferring the finite obstruction to the
literal weighted matrix is a lower-buffer theorem. The accepted profile
state gives upper size, support, and regularity information, but no
quantified interval on which, for one fixed \(g,j\), the joint factor

\[
 W\!\left(\frac{X}{gnD}\right)
 q_L\!\left(\frac{4Xj}{gn^2}\right)
\tag{160.A16}
\]

is uniformly comparable to a nonzero value while every required unit
\(n\bmod j\) class occurs. Upper bounds and zero extension do not imply
such a lower control. Diagonal weighting can delete rows or make their
nuclear contribution arbitrarily small.

Even a future lower-buffer lemma would control only the inverse-phase
submatrix. It would not show that entrywise multiplication by the actual
\(S(N_0,h;n)\) array preserves the same nuclear lower bound, nor would it
exclude a vector theorem that retains this interaction before positive
norms.

The first open positive theorem is therefore a signed vector-valued
estimate for the entire literal \((g,n,j,h)\) matrix, with the full
long-\(h\) range, both characters, moving support, endpoints, every
growing level and spectral piece, and a gain of \(X^{\mu(a)}\).

## 5. Required controls and outcomes

- reciprocity sign, representatives, and both parities of \(j\):
  **GREEN**;
- literal normalization, both character directions, real centre, and
  arbitrary gcd strata: **GREEN**;
- complete \(h\)-reconstruction and exactly-once zero deletion:
  **GREEN**;
- unweighted residue spectrum, nuclear norm, and Hilbert projective
  interpretation: **GREEN with exact-scalarization-plus-triangle scope**;
- full positive residue block and survival of \(h=mj\): **GREEN**;
- sharp long-block operator norm: **GREEN as capacity, not as a signed
  lower bound**;
- additive high-frequency mass: **GREEN as finite diagnostic only**;
- primitive \(g=1\) and both boundary-power branches:
  **GREEN pointwise in the strict region**;
- moving literal weighted lower bound: **NOT PROVED; conditional only**;
- primary-source scalar match: **NO OWNER-SAVING MATCH**;
- bespoke vector theorem: **OPEN and outside the no-go**;
- target, strict range, endpoint uniformity, M9--M2, M9, bridge, and
  exponent: **UNCHANGED**; and
- computation: none used.

## 6. Dependencies and exact artifacts used

The adjudication promotes only the Round-160 kernel under
proofs/kernels/m9_m2_unbalanced_inverse_selector_reciprocity_projective_obstruction.md.
It uses all three reports, the statement-only blind rederivation, the
post-unmask seam review, the independent exact-kernel/power review, the
independent source-level review, and the scope/hygiene review. The
accepted graph dependencies are the Round-107 fixed-centre return, the
flat-wave envelope, the Round-135 Kloosterman-dispersion obstruction, the
Round-143 level-four matrix obstruction, the exact \(\chi_4\) factor, and
the elementary divisor/totient input.

The source statements are used only under their exact audited hypotheses.
No computation is mathematical evidence.

## 7. Recommended state effect

Create one proved-internal route-scoped node for the exact reciprocity
kernel and scalar projective-capacity obstruction. Update the open
flat-smooth strict-UNBAL target and its Round-107, Round-135, and
Round-143 interface records to identify the finite kernel price, long
complement, and first remaining bespoke-vector seam.

Reject an unsigned-to-signed transfer, an unconditional weighted-matrix
lower bound, deletion of positive \(h=mj\), low-bandwidth additive
encoding, free fixed-level spectral encoding, short-Linnik coverage of
the whole row, a universal scalar/vector impossibility claim, any target
or strict-range claim, and any global-exponent improvement.

Leave every other M2 owner, every M1 owner, endpoint uniformity, M9, the
conditional bridge, the quarter target, the internal exponent \(1/3\),
and the separately audited external exponent unchanged. Under the Round
160 strategy, park this exact flat-UNBAL scalar surface and rotate the
next campaign to a different mandatory M2 owner unless a genuinely new
literal-matrix vector theorem is supplied.

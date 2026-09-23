# Conductor Round-195 report reconciliation

- Campaign: m9-m1-t1-p2-determinant-fibre-vector-dispersion-gate
- Round: 195
- Starting graph SHA-256: 815c15c4aba04d4ac8e05a3af89db78b05607242fc933e23ec86954138700c89
- Status: conductor reconciliation; candidate evidence only before seam review and State Patch

## 1. Frozen objective and report receipts

Round 195 froze the complete physical first-failure mask

\[
 P_2=\mathbf 1_{\{|d-gm|\le D_L\}}
     \mathbf 1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil,
\]

inside the exact accepted Round-192 core.  The target was

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll H_B\mathfrak m\kappa uX^\varepsilon
\]

with both orientations, both frequency signs, both \(T\)-branches, every
literal endpoint/event field, the physical-mask commutator, and one outer
real part retained.  The three frozen receipts are:

1. reports/literal_p2_determinant_fibre_vector_attack.md, SHA-256
   c617c18c959792622e3df9fe3eb06f47ba61c6948be77f8617c83bda96302879;
2. reports/p2_gram_diagonal_collision_hostile_audit.md, SHA-256
   52de40ade4e243cca9e0c50edfee5f913c8120a488407b4f39fe951f22d9b8fb;
3. reports/blind_p2_determinant_fibre_rederivation.md, repaired only by
   restoring ten missing TeX separator backslashes, SHA-256
   29ae2a518cf61fe5f7f43369d4d51a52b71a535dae63717801874bf7ffc935df.

No conclusion is selected by vote.  The first two reports independently
derive the same strict physical sector.  The blind report is used only for
algebraic cross-checking after the omissions listed below are restored.

## 2. Selected positive theorem

Put

\[
 P_{2,\ge D}=P_2\mathbf1_{\{\kappa\ge D_L\}},\qquad
 P_{2,<D}=P_2\mathbf1_{\{1\le\kappa<D_L\}}.
\]

This is an exact disjoint split.  The whole \(P_{2,\ge D}\) sector is
target-safe.  The packet-level positive count below also proves the exact
subsector

\[
 P_{2,<D}\mathbf1_{\{\min(Y,D_L)\le H_B\mathfrak m\kappa\}}
\]

target-safe; the remaining packet region has the strict reverse
inequality.

In the plus chart

\[
 d=\kappa gU,\quad d'=g(\kappa U+2S),\quad
 m'=\kappa v,\quad m=\kappa v+2w,\quad h=Sv-Uw>0,
\]

lower closeness gives \(O(D_L)\) choices of \(w\) after
\((\kappa,g,U,v)\) is fixed.  The determinant range
\(0<h<R_0/(2\kappa g)\), together with \(\kappa v\asymp L\), gives
\(O(1)\) choices of \(S\).  In the minus chart the roles are transposed:
lower closeness gives \(O(D_L)\) choices of \(S\), while
\(h=Uw-vS\) and \(\kappa U\asymp L\) give \(O(1)\) choices of \(w\).
The close lower coordinate also forces \(g=O(1)\).  Hence

\[
 \#\mathcal I_{P_{2,\ge D}}
 \ll\sum_{\kappa\ge D_L}D_L(1+L/\kappa)^2
 \ll L^2+LD_L\log(2L)\ll L^2.
\]

Every physical, spectral, core, endpoint, and residual restriction only
deletes candidates.  Complete anchor expansion and the finite exact event
decomposition cost only the inherited \(X^\varepsilon\) ledger.  Thus the
full masked source is absolutely \(O(L^2X^\varepsilon)\).

Rerunning the accepted Round-187--192 projectors on this physically masked
source is deletion-stable.  All new affine births, deaths, carries,
endpoint changes, and the mask commutator remain in the recomputed core.
Source minus safe projector therefore gives

\[
 |\mathscr R_{{\rm core},Y,H_B}^\sigma(P_{2,\ge D}W)|
 \ll L^2X^\varepsilon.
\]

At a fixed packet, each literal projective row has \(O(D_L)\) physical
atoms over the whole height block and there are \(O(uJ/q)\) rows.  The
complete anchor/Abel return costs at most the inherited \(q/J\), so the
new part costs \(O(D_LuX^\varepsilon)\); accepted terminal and Fejer pieces
cost \(O(\kappa uX^\varepsilon)\).  Therefore

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,\ge D}W)|
 \ll (D_L+\kappa)uX^\varepsilon
 \ll\kappa uX^\varepsilon
 \le H_B\mathfrak m\kappa uX^\varepsilon.
\]

This proof is absolute.  It invokes neither coefficient cancellation nor
separate orientation norms.

## 3. Exact complement and selected method boundary

The physical complement is \(P_{2,<D}\).  At fixed height, the close affine
variable lies in one residue class modulo \(v\) in the plus chart and one
residue class modulo \(U\) in the minus chart.  Since
\(U,v\asymp L/\kappa\), the close window contains

\[
 O(1+\kappa D_L/L)=O(1)\qquad(\kappa<D_L)
\]

sites.  The fixed-height count gives \(YuX^\varepsilon\), while the
all-height determinant count gives \(D_LuX^\varepsilon\).  Combining them
with the accepted terminal/Fejer cost proves

\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_{2,<D}W)|
 \ll u\{\kappa+\min(Y,D_L)\}X^\varepsilon.
\]

The \(\kappa u\) term is target-safe.  The precise unresolved
positive-capacity multiplier is therefore

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa}.
\]

Consequently the packet subrange
\(\min(Y,D_L)\le H_B\mathfrak m\kappa\) is already target-safe.  The
exact open packet complement is

\[
 \kappa<D_L,\qquad \min(Y,D_L)>H_B\mathfrak m\kappa.
\]

With positive far defect \(\eta\), the determinant fibres are

\[
 2h=v\eta+U\delta-\kappa(U^2-v^2)\quad(+),
\]

\[
 2h=U\eta-v\delta+\kappa(U^2-v^2)\quad(-).
\]

Increasing \(\eta\) by two changes height by \(v\) or \(U\), comparable
with the live height scale \(L/\kappa\).  A fixed primitive row therefore
has only \(O(1)\) far samples in one height block.  The minus
anchor-character factor is constant along its legal parity step because
\(U=\mathfrak m q\).  At a fixed retained plus mode the exact ratio is
\((-1)^{c_+(h;v)}e(a/q)\), where the canonical anchor wrap
\(c_+(h;v)\in\{0,1\}\); the full pre-Fourier parity flip is recovered only
after all modes recombine.  Neither level supplies a long within-row
orthogonality gain.

The exact event Gram must first recombine all same-site channels.  Current
phase channels form an all-ones \(2\times2\) block and previous phase
channels an all-ones \(3\times3\) block; their signed recombination returns
the original masked jump.  Treating source labels as orthogonal instead
makes the final all-ones summation functional restore the same capacity.
Across rows, the full \(++,+-,-+,--\) Gram retains actual endpoint
coefficients, square-root phases, Fejer factors, selectors, carries,
births/deaths, mask commutators, and cross-event terms.  Only Cauchy's
positive-capacity bound is currently justified.

The first open seam is therefore a coefficient-sensitive cross-row
four-block Gram estimate for the actual literal vectors on the strict open
packet region displayed above.
This is a scoped no-go for coefficient-blind or within-row
determinant/anchor dispersion.  It is not a literal lower bound and does
not disprove complete \(P_2\).

## 4. Blind post-unmask reconciliation

The blind report correctly rederived the two orientation fibre equations,
their divisor/quadratic-congruence forms, and the need for a joint literal
Gram.  Its proposed large minus fibre and quantitative counterexample are
not live-packet evidence:

1. the inherited normalization is \(U\mid u\), in fact \(u=gU\), with
   \(u\asymp v\asymp L/\kappa\); the choice
   \(\mathfrak m=\kappa=u=1,q=U=p^2\) loses both row length and the factor
   \(u\) in the target;
2. its choice \(Y=2QU\) has \(Y>h\), and \(L=p^2,X=p^4\) violates the live
   connector \(L\ll X^{1/4}\);
3. its fixed divisor \(\kappa gU=p^2\) is not squarefree, so the literal
   endpoint coefficient vanishes; the residual, shell, core, endpoint, and
   zero-extension masks were also not verified;
4. after restoring only \(u=gU\), a coherent \(O(\sqrt U)\) family is
   already smaller than the target \(Q\mathfrak m\kappa uX^\varepsilon\).

On nonzero live support, \(\kappa gU\) is squarefree, hence \(U\) is
squarefree and \((\kappa,U)=1\).  The minus quadratic congruence therefore
has at most

\[
 2^{\omega(U)}\ll_\varepsilon U^\varepsilon
\]

roots modulo \(U\) for fixed \((\kappa,U,h,\delta)\); the plus divisor
fibre has the analogous divisor-bound control.  These are useful algebraic
cross-checks but do not price the anchor denominator or the actual
cross-row coefficient Gram, so they do not close \(P_{2,<D}\).

The arbitrary bounded-coefficient construction is retained only as a
mechanism control, not as evidence of literal lower mass.  No blind live
large-fibre, literal lower-bound, target violation, or exponent claim is
promoted.

## 5. Conductor decision before seam review

Formalize one candidate strict-sector lemma for the whole
\(P_{2,\ge D_L}\) sector and the absolute-capacity packet sector
\(\kappa<D_L,\min(Y,D_L)\le H_B\mathfrak m\kappa\), with their exact open
packet complement and the scoped within-row self-return.  Do
not promote complete \(P_2\), complete original \(t=1\), the hard-M1 owner,
M9-M1, M9, any bridge, the Gauss-circle target, or any exponent.  Promotion
requires independent count/power/operator review, literal Gram/no-go
review, blind post-unmask review, final candidate-kernel consistency, and a
mechanically valid State Patch.

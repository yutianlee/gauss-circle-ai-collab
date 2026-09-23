# Round 181 blind post-unmask radical review

- Campaign: m9-m1-hard-top-high-squarefree-radical-gate
- Task: blind_post_unmask_radical_review
- Role: blind post-unmask seam reviewer
- Generated: 2026-08-27T08:44:04.7412815Z
- Starting graph SHA-256: 6e3a87d42844a9a2150aad652b2f08a7b0584c3de17e6386311688552f6d7c16
- Status: review evidence only; no shared proof-state edit

## 1. Result

### Pre-unmask ledger

After reading only protocol.md, blind_statement.md, and the blind report,
I recorded these isolated conclusions before opening the brief, campaign,
strategy, graph, or either selected-context report.

1. Grouping by \(r=hn\) and writing uniquely \(r=st^2\), with \(s\)
   squarefree, are exact and multiplicity preserving.
2. The low-radical incidence has sharp power

   \[
   I_{\leq L}\ll_\eta L^{3/2+\eta},
   \qquad I_{\leq L}\gg L^{3/2}
   \]

   on a full standard dyadic shell. The lower bound concerns incidence
   capacity, not the literal signed coefficient.
3. Under only \(|a(h,n)|\leq\mathcal X\), the high-radical aggregate has
   exact capacity \(\asymp L^2\mathcal X\). Thus neither the
   \(L^{3/2}\mathcal X\) target nor the fixed-\(t\)
   \(S_t^{3/4}\mathcal X\) target follows for arbitrary complex
   coefficients.
4. The obstruction is already present at \(t=1\): a positive-density
   squarefree-coprime interior cone can be dechirped site by site.
5. Uniform fixed-\(t\) bounds \(S_t^{3/4}\mathcal X\) would imply the
   aggregate target because
   \(\sum_t(L^2/t^2)^{3/4}\ll L^{3/2}\), but the packet does not prove
   those bounds.
6. The shifted-correlation condition (R181.23) is a concrete sufficient
   hypothesis for the fixed-\(t\) estimate. It is not necessary and is not
   proved for the literal family.
7. The fixed literal hard coefficient remains unresolved; the adversarial
   examples supply no literal lower bound.

### Post-unmask verdict

The two selected-context reports agree with all substantive conclusions.
The blind mathematics is sound after one minor parity repair in its
written \(t=1\) density argument and one scope correction to the wording
around (R181.23).

The provenance is acceptable as an independent derivation from the finite
packet, but not as independent discovery of the campaign ledger. The
assigned blind brief itself repeats the low/high capacities, the missing
\(L^{1/2}\), and the mandatory \(t=1\) face.

The literal high-radical estimate (181.HR) is neither proved nor refuted.
Promote only the exact reductions and strict target-safe sectors; record
capacity and self-return statements only with mechanism scope; leave
M9-M1-top-endpoint-signed-cone open.

## 2. Exact statement and hypotheses

Let

\[
\mathcal D_L=\{(h,n):c_0L\leq h\leq c_1L,\ n\ {\rm odd},\
4h<n<16h\},
\]

where \(0<c_0<c_1\) are fixed. Suppose
\(a:\mathcal D_L\to\mathbb C\) and
\(|a(h,n)|\leq\mathcal X\). Define

\[
C(r)=
\sum_{\substack{h\mid r,\ h\asymp L\\
r/h\ {\rm odd},\ 4h<r/h<16h}}
\chi_4(r/h)a(h,r/h).
\]

The following statements are certified.

1. Exactly,

   \[
   \sum_{h,n}\chi_4(n)a(h,n)e(\sqrt{Xhn})
   =\sum_rC(r)e(\sqrt{Xr})
   =\sum_{\mu^2(s)=1}\sum_{t\geq1}C(st^2)e(t\sqrt{Xs}).
   \]

2. Literal support gives \(st^2\asymp L^2\), hence
   \(s\ll L^2\), \(t\asymp L/\sqrt s\), and
   \(s>L\Rightarrow t\ll\sqrt L\).
3. For every \(\eta>0\),

   \[
   I_{\leq L}:=
   \#\{(h,n)\in\mathcal D_L:\operatorname{sf}(hn)\leq L\}
   \ll_\eta L^{3/2+\eta}.
   \]

   If the shell contains a fixed-width dyadic interior, then
   \(I_{\leq L}\gg L^{3/2}\). This certifies sharpness of the exponent,
   not a naked \(O(L^{3/2})\) upper bound.
4. For every product-determined \(E\subseteq\mathcal D_L\),

   \[
   \sup_{|a|\leq\mathcal X}
   \left|\sum_{(h,n)\in E}\chi_4(n)a(h,n)e(\sqrt{Xhn})\right|
   =\mathcal X\#E.
   \]

   Thus the high-radical arbitrary-coefficient capacity is
   \(\Theta(L^2\mathcal X)\), including at \(t=1\).
5. With \(S_t\asymp L^2/t^2\), a uniform literal estimate

   \[
   \left|\sum_sC(st^2)e(t\sqrt{Xs})\right|
   \ll S_t^{3/4}\mathcal X
   \]

   would imply the aggregate target. It is a sufficient strengthening,
   not an equivalent or necessary reformulation.

For the graph-owned literal coefficient, one additionally has
\(|a_{L,X}^{\rm lit}|\ll1\) and a polynomial relation between \(L\) and
\(X\). These absorb the divisor loss into \(X^\varepsilon\). None of the
universal lower controls is then a literal lower bound.

## 3. Proof and post-unmask audit

### 3.1 Provenance

The required read order was respected in this review: the pre-unmask
ledger in Section 1 was fixed before any selected context was opened.

The blind report transparently lists protocol.md, the blind statement, and
its assigned brief. It lists no graph, campaign, strategy, earlier round,
or sibling report. File chronology supports this: the blind report was
last written at 16:17:15 local time, while the connector report was created
at 16:17:53 and the signed-attack report at 16:20:41. The blind report also
contains material absent from both siblings, notably the explicit
low-sector sharpness boxes and (R181.23), while it omits their distinctive
\((h,n)\mid t\), large-\(t\), and squarefree-Mobius self-return results.
This is positive, though not cryptographic, evidence against sibling
contamination.

There is one qualification. The active campaign declares only protocol.md
and blind_statement.md as external blind context, but the administrative
brief repeats answer-level campaign facts. The report correctly discloses
using that brief. It is therefore an independent proof audit of those
facts, but should not be cited as independent discovery or as having seen
literally only the two external files.

The current proof-obligation file has exactly the campaign hash recorded
above.

### 3.2 Low-sector bound and sharpness

The upper bound is

\[
I_{\leq L}
\leq
\sum_{\substack{s\leq L\\\mu^2(s)=1}}
\sum_{t\ll L/\sqrt s}\tau(st^2)
\ll_\eta
L^\eta\sum_{s\leq L}\left(1+\frac L{\sqrt s}\right)
\ll_\eta L^{3/2+\eta}.
\]

The blind lower construction is valid at power precision. Choose

\[
d\in[3,3.1]\sqrt L,\qquad
u\in[1/3,0.34]\sqrt L,\qquad
v\in[8/3,2.7]\sqrt L,
\]

with \(d,v\) odd and \((u,v)=1\), and put \(h=du,n=dv\). Then
\(h\in[L,1.054L]\), \(n\in[8L,8.37L]\), the cone is strict, and

\[
\operatorname{sf}(hn)=\operatorname{sf}(d^2uv)
=\operatorname{sf}(uv)\leq uv<0.918L.
\]

Moreover \(d=(h,n)\), so the parametrization is injective. There are
\(\gg\sqrt L\) choices of \(d\) and \(\gg L\) coprime
\((u,v)\)-pairs. This proves \(I_{\leq L}\gg L^{3/2}\), but not a
log-free matching upper bound and not a literal signed lower estimate.

### 3.3 High capacity and the \(t=1\) repair

Triangle inequality gives at most \(\mathcal X\#E\), while

\[
a(h,n)=\mathcal X\chi_4(n)e(-\sqrt{Xhn})
\]

on \(E\) makes every summand equal to \(\mathcal X\). This proves the
exact capacity identity. Since the full cone has \(\asymp L^2\)
incidences and the low sector has \(o(L^2)\), the high sector has
\(\asymp L^2\) incidences.

At \(t=1\), \(r=s\) is squarefree, equivalently \(h,n\) are squarefree
and coprime. The blind report's phrase “among its odd pairs” must mean
that both \(h\) and \(n\) are first restricted to be odd. Otherwise,
excluding only odd-prime squares does not remove \(4\mid h\). Restricting
both coordinates to be odd, or separately excluding \(4\mid h\), repairs
the proof and leaves \(\gg L^2\) squarefree-coprime sites. The conclusion
is promotable, but the written argument should be quoted with this repair.

Post-unmask, the selected reports give the compatible exact refinement

\[
h=Gda^2,\qquad n=Geb^2,\qquad s=de,\qquad t=Gab,
\]

so \((h,n)=G\mid t\). They also prove by incidence that the literal sectors
\(t\geq\lceil\sqrt L\rceil\) and \(G\geq\sqrt L\) are target-safe. The
retained complement still contains the full \(t=G=1\) face.

### 3.4 Literal versus adversarial scope

The blind report maintains the essential separation. Dechirping,
character erasure, perfect-square centres, one-site and one-fibre examples,
and the positive-density \(t=1\) construction apply to arbitrary bounded
coefficients. They show that support, pointwise size, divisor
multiplicity, the phase alone, and averaging only over \(t\) cannot prove
a coefficient-uniform theorem. They do not show that the fixed literal
coefficient is large.

The selected reports preserve this distinction. Their large-\(t\) bound
is a literal upper estimate. Their squarefree-Mobius calculation is an
actual-coefficient identity returning the high-radical aggregate to the
original hard scalar plus a target-safe correction. The central Mellin
cancellation is confined to one mode; restoring the noncentral modes
restores the literal incomplete divisor coefficient. These are scoped
self-returns, not disproofs of (181.HR).

### 3.5 The shifted-correlation condition

For fixed \(t\), zero-extend

\[
z_t(s)=C(st^2)e(t\sqrt{Xs})
\]

to an interval of length \(N\asymp S_t\), and take
\(H=\lfloor N^{1/2}\rfloor\). The divisor estimate gives

\[
\sum_s|z_t(s)|^2\ll_\eta NL^\eta\mathcal X^2.
\]

Van der Corput differencing gives

\[
\left|\sum_sz_t(s)\right|^2
\ll\frac{N+H}{H}
\left(
\sum_s|z_t(s)|^2+
\sum_{1\leq q<H}
\left|\sum_sz_t(s+q)\overline{z_t(s)}\right|
\right).
\]

Thus (R181.23), whose correlation right side is
\(\ll HN^{1/2}L^\eta\mathcal X^2\), implies

\[
\left|\sum_sz_t(s)\right|
\ll N^{3/4}L^{\eta/2}\mathcal X.
\]

It is a valid sufficient condition, with bounded \(N\) handled trivially.
It is not necessary. A small linear sum need not have small absolute
short-shift correlations; alternating or block-balanced sequences already
show this. Nor must an aggregate proof work fixed \(t\): cancellation
between \(t\)-layers, higher correlations, sparsity, or exact telescoping
could suffice. What is necessary is only additional literal information
that excludes the sitewise phase-aligned arbitrary class. The report's
claim that a shifted cross-radical relation is “indispensable” is too
strong if read formally.

### 3.6 Graph scope

The graph confirms that M9-M1-top-endpoint-transform and the physical
one-count assembly are proved, while M9-M1-top-endpoint-signed-cone is
open. Even a proof of (181.HR) would close only the hard residual child
after the accepted transform. The independent smooth residual child would
remain. No conclusion follows for full M9-M1, GAR, M9-M2, endpoint
uniformity, M9, either bridge, the quarter theorem, or an exponent
improvement.

## 4. First doubtful or unproved step

The first mathematical step still unproved is

\[
\left|
\sum_{\substack{s>L\\\mu^2(s)=1}}
\sum_tC_{L,X}^{\rm lit}(st^2)e(t\sqrt{Xs})
\right|
\ll_\varepsilon L^{3/2}X^\varepsilon,
\]

already on its \(t=1\) squarefree-coprime face. Neither the blind report
nor either selected report supplies the actual-direction \(L^{1/2}\)
contraction.

The first local defect in the blind report is the omitted parity clause in
the \(t=1\) density proof. The first conceptual overstatement is treating a
shifted cross-radical relation as necessary rather than merely sufficient
and illustrative. Neither issue changes the capacity no-go or the open
status of the literal target.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| blind read order | **Pass.** Isolated conclusions were recorded before unmasking. |
| blind provenance | **Pass with qualification.** Chronology and asymmetric content support independence from sibling derivations; the brief preloaded answer-level campaign facts. |
| graph hash | **Pass.** The authoritative graph hash matches the campaign hash. |
| exact product fibre | **Pass.** Signs, phase, boundaries, and multiplicities are retained. |
| low-radical sharpness | **Pass at exponent precision.** Upper \(L^{3/2+\eta}\), lower \(L^{3/2}\); no naked upper bound. |
| high-radical capacity | **Pass for arbitrary coefficients.** Exact capacity is \(\Theta(L^2\mathcal X)\). |
| high-radical \(t=1\) | **Pass after parity repair.** Positive-density squarefree-coprime sites remain. |
| dechirping and character erasure | **Pass as adversarial controls only.** No literal lower mass follows. |
| fixed-\(t\) summation | **Pass conditionally.** The proposed bounds sum correctly but remain unproved literally. |
| shifted correlation | **Pass as sufficient only.** Necessity is rejected. |
| perfect-square centre | **Pass.** Exact squares lie in the paid low-radical sector. |
| downstream scope | **Pass.** All broader parents remain open. |

No numerical experiment or external theorem was used.

## 6. Dependencies and exact artifacts used

The blind statement and blind report were read first, after protocol.md.
Only afterward were the following unmasked materials read:

1. rounds/codex-managed/m9-m1-hard-top-high-squarefree-radical-gate/briefs/blind_hard_m1_radical_rederivation.md;
2. the two sibling reports in that campaign;
3. state/active_campaign.yml;
4. strategy/round181_m1_hard_top_high_squarefree_radical_strategy.md;
5. strategy/round181_selection/conductor_round181_selection_decision.md;
6. strategy/round181_selection/m1_gar_frontier_selection.md;
7. state/proof_obligations.yml, restricted to the named Round-181 owners,
   connectors, normalizations, and no-repeat obstructions.

Filesystem metadata and a SHA-256 check were used only for provenance.

## 7. Recommended state effect

Promote, after the remaining conductor seam checks, only:

1. the exact product-fibre identity, squarefree-kernel split, support
   relations, and multiplicity preservation;
2. the literal low-radical absolute estimate
   \(\ll_\varepsilon L^{3/2}X^\varepsilon\) in the inherited graph range,
   together with \(L^{3/2+o(1)}\) sharpness of universal incidence
   capacity only;
3. the exact \(G,d,e,a,b\) parametrization, \((h,n)\mid t\), and the
   target-safe literal sectors \(t\geq\sqrt L\) and
   \((h,n)\geq\sqrt L\);
4. the arbitrary-coefficient high-sector and \(t=1\) capacity obstruction,
   scoped only against coefficient-uniform, character-erased,
   product-triangle, and \(t\)-averaging arguments;
5. the fixed-\(t\) capacity ledger and the conditional implication from
   all \(S_t^{3/4}\) bounds to the aggregate \(L^{3/2}\) target;
6. the actual-coefficient squarefree-Mobius and central-Mellin
   self-returns, only with the mechanism scopes proved in the selected
   report.

Retain (R181.23) only as an illustrative sufficient research hypothesis.
Do not promote it as necessary or as verified for the literal coefficient.

Reject any claim that (B181.3), or the fixed-\(t\)
\(S_t^{3/4}\mathcal X\) estimate, follows from support and the pointwise
coefficient bound. Also reject any transfer of adversarial lower examples
to the literal coefficient and any claim of pristine independent discovery
from the campaign-preloaded blind brief.

Leave open (181.HR), its small-\(t\) complement, the literal \(t=1\)
scalar, and M9-M1-top-endpoint-signed-cone. Make no change to smooth M1,
GAR, full M9-M1, M9-M2, endpoint uniformity, M9, either bridge, GC-target,
or the exponent ledger.

The most informative single authorized exit label is
hard_m1_high_radical_capacity_or_self_return_no_go, understood strictly as
mechanism-scoped and not as rejection of the literal high-radical target.

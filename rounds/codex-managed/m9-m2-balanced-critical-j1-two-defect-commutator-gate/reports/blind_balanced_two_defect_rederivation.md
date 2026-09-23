# Blind balanced two-defect rederivation

- Campaign: `m9-m2-balanced-critical-j1-two-defect-commutator-gate`
- Task: `blind_balanced_two_defect_rederivation`
- Role: statement-only blind rederivation
- Generated: 2026-08-26
- Graph hash: deliberately unavailable in the statement-only packet; not inspected
- Exact context used: `protocol.md`; `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/blind_statement.md`

## 1. Result: exact identity and capacity no-go

Let \(S=\operatorname{supp}a\), with every alias, star, floor, endpoint
convention, and support crossing already absorbed into the literal value of
\(a(h,k)\). The change of variables

\[
 ((h,k),(h',k'))\longmapsto (h,k,p,q)=(h,k,h'-h,k'-k)
\]

is a multiplicity-one bijection from ordered pairs in \(S^2\) to

\[
 \mathcal D=\{(h,k,p,q):(h,k)\in S,\ (h+p,k+q)\in S\}.
\]

On this exact, generally nonrectangular domain,

\[
 \Delta=hq+pk+pq,\qquad \rho=hq-pk,
\]

and hence

\[
 \Delta+\rho=q(2h+p),\qquad
 \Delta-\rho=p(2k+q).
\]

There is a canonical exact two-direction commutator, obtained by independently
swapping the two \(h\)-coordinates and the two \(k\)-coordinates. It applies
without boundary terms only on the four-corner-complete subdomain. On that
subdomain the complete zero-subtracted scalar is **not** its double
commutator: it is the double-commutator projection plus three exact parity
complements. The rest of the original domain is an additional exact support-
crossing boundary term. In particular, the double commutator vanishes
identically when \(p=0\) or \(q=0\), whereas the original scalar and both far
gates can be nonzero there.

Consequently, a scalar commutator or scalar two-variable summation-by-parts
identity alone does not prove (171.B1). With the supplied positive capacity
\(L^4X^\varepsilon\), every unestimated parity complement, support-crossing
term, gate-jump term, or endpoint term still has capacity
\(L^4X^\varepsilon\). The missing factor \(L^{-1}\) must come from a proved
property of the literal coefficient (or a proved count/variation estimate for
all of those corrections). No such property is present in the statement-only
packet. This is an identity/capacity no-go for the proposed scalar route; it
does not assert that the literal target is false.

## 2. Exact statement and hypotheses

Write

\[
 z_{ij}=e\!\left(\sqrt X\sqrt{(h+ip)(k+jq)}\right),
 \qquad i,j\in\{0,1\},
\]

whenever the corresponding point belongs to the literal support, and put

\[
 H=z_{00}\overline{z_{11}}-1,
 \qquad W=a(h,k)\overline{a(h+p,k+q)}.
\]

The only scalar facts used below are finiteness of \(S\) and \(|z_{ij}|=1\).
Set

\[
 G=\mathbf 1_{\{|\Delta|>L\}}\mathbf 1_{\{|\rho|>L\}}.
\]

The exact complement of the far gate is

\[
 1-G=
 \mathbf 1_{\{|\Delta|\le L\}}+
 \mathbf 1_{\{|\rho|\le L\}}-
 \mathbf 1_{\{|\Delta|\le L,\ |\rho|\le L\}}.
 \tag{2.1}
\]

Define the four-corner-complete domain

\[
 \mathcal D_\square=
 \{(h,k,p,q): (h,k),(h+p,k),(h,k+q),(h+p,k+q)\in S\}
\]

and the support-crossing boundary

\[
 \mathcal D_\times=\mathcal D\setminus\mathcal D_\square.
\]

If \(I_{10}=\mathbf1_S(h+p,k)\) and
\(I_{01}=\mathbf1_S(h,k+q)\), then its indicator has the exact disjoint
description

\[
 \mathbf1_{\mathcal D_\times}
 =\mathbf1_{\mathcal D}\big[(1-I_{10})+I_{10}(1-I_{01})\big].
 \tag{2.2}
\]

On \(\mathcal D_\square\), define the commuting involutions

\[
 \tau_h(h,k,p,q)=(h+p,k,-p,q),\qquad
 \tau_k(h,k,p,q)=(h,k+q,p,-q),
\]

and the two difference operators

\[
 D_h=I-\tau_h,\qquad D_k=I-\tau_k.
 \tag{2.3}
\]

For \(\epsilon,\eta\in\{+1,-1\}\), let

\[
 P_{\epsilon\eta}={1\over4}(I+\epsilon\tau_h)(I+\eta\tau_k).
 \tag{2.4}
\]

The exact claim proved here is

\[
 \begin{split}
 \sum_{\mathcal D}GWH
 &=\sum_{\mathcal D_\times}GWH\\
 &\quad+\sum_{\epsilon,\eta\in\{\pm1\}}
 \sum_{\mathcal D_\square}G
 (P_{\epsilon\eta}W)(P_{\epsilon\eta}H).
 \end{split}
 \tag{2.5}
\]

Thus the exact double-commutator contribution is the \((-- )\) term, with

\[
 P_{--}H={1\over4}D_hD_kH,
 \tag{2.6}
\]

and the exact complement is

\[
 \sum_{\mathcal D_\times}GWH+
 \sum_{(\epsilon,\eta)\ne(-1,-1)}
 \sum_{\mathcal D_\square}G
 (P_{\epsilon\eta}W)(P_{\epsilon\eta}H).
 \tag{2.7}
\]

No conclusion is claimed for any other balanced label or for a global
theorem.

## 3. Proof and derivation

### 3.1 Coordinates, inverse, multiplicity, character, and axes

The inverse coordinate map is

\[
 (h,k,p,q)\longmapsto ((h,k),(h+p,k+q)).
\]

Both compositions are the identity, so the multiplicity is exactly one; no
rectangular enlargement of \(\mathcal D\) is legitimate without a correction.
Direct expansion gives

\[
 \Delta=(h+p)(k+q)-hk=hq+pk+pq,
 \qquad
 \rho=h(k+q)-(h+p)k=hq-pk,
\]

which proves (171.B2).

On nonzero character support, both \(h\) and \(h+p\) are odd, hence
\(p=2s\). Since \(\chi_4\) is real and, for odd \(n\),
\(\chi_4(n)=(-1)^{(n-1)/2}\),

\[
 \chi_4(h)\chi_4(h+p)=(-1)^s.
 \tag{3.1}
\]

For fixed \(p\), this factor is constant throughout the whole
\((h,k,q)\)-fibre. It supplies no cancellation in that fibre.

The axial sectors are exact and cannot be divided by \(p\) or \(q\):

\[
 \begin{array}{c|c|c|c}
 \text{sector}&\Delta&\rho&\mathrm{df}\\ \hline
 p=0&hq&hq&|hq|>L,\\
 q=0&pk&-pk&|pk|>L.
 \end{array}
 \tag{3.2}
\]

Their intersection \(p=q=0\) is not far, but either punctured axis may be
far and has generally nonzero \(H\).

### 3.2 The exact swap commutator and all complements

Under the two swaps, the defect pair transforms as

\[
 (\Delta,\rho)\stackrel{\tau_h}{\longmapsto}(\rho,\Delta),
 \qquad
 (\Delta,\rho)\stackrel{\tau_k}{\longmapsto}(-\rho,-\Delta),
 \qquad
 (\Delta,\rho)\stackrel{\tau_h\tau_k}{\longmapsto}(-\Delta,-\rho).
 \tag{3.3}
\]

Therefore \(G\) is exactly invariant under both swaps. Also
\(\mathcal D_\square\) is invariant and each swap is a multiplicity-one
permutation there. There are consequently no hidden gate-boundary terms in
the swap identity. The only domain boundary is precisely
\(\mathcal D_\times\) from (2.2).

The four scalar transforms are

\[
 \begin{aligned}
 H&=z_{00}\overline{z_{11}}-1,\\
 \tau_kH&=z_{01}\overline{z_{10}}-1,\\
 \tau_hH&=z_{10}\overline{z_{01}}-1,\\
 \tau_h\tau_kH&=z_{11}\overline{z_{00}}-1.
 \end{aligned}
\]

Thus the double commutator is exactly

\[
 D_hD_kH
 =z_{00}\overline{z_{11}}-z_{01}\overline{z_{10}}
  -z_{10}\overline{z_{01}}+z_{11}\overline{z_{00}}
 =2\Re\!\left(z_{00}\overline{z_{11}}
              -z_{01}\overline{z_{10}}\right).
 \tag{3.4}
\]

If \(p=0\), then \(\tau_h=I\); if \(q=0\), then \(\tau_k=I\).
Therefore (3.4) vanishes identically on both axes. This proves directly that
the complete zero-subtracted scalar cannot equal its two-direction
commutator.

For completeness, with the bilinear pairing

\[
 \langle U,V\rangle_G=
 \sum_{\mathcal D_\square}GUV,
\]

both swaps are self-adjoint and the four operators (2.4) are mutually
orthogonal projections. Hence

\[
 \langle W,H\rangle_G
 =\sum_{\epsilon,\eta}\langle
 P_{\epsilon\eta}W,P_{\epsilon\eta}H\rangle_G,
\]

which, after adding the support-crossing sum, proves (2.5). Equivalently, the
double-commutator summation-by-parts piece is

\[
 \langle P_{--}W,P_{--}H\rangle_G
 ={1\over16}\langle D_hD_kW,D_hD_kH\rangle_G,
 \tag{3.5}
\]

but (3.5) is only one of four parity pieces, not the original sum.

The character product in (3.1) is invariant under both \(\tau_h\) and
\(\tau_k\): the swaps do not change the unordered pair \(\{h,h+p\}\).
It therefore cannot turn the actual weight into a double-antisymmetric
weight. An antisymmetric sign needed to isolate (3.5) is absent.

### 3.3 Anchored and local two-variable differences

The same obstruction appears for coordinate differences. Put

\[
 H_{s,q}=e\!\left(\sqrt X
   (\sqrt{hk}-\sqrt{(h+2s)(k+q)})\right)-1.
\]

The two anchored operators

\[
 \mathcal A_sF(s,q)=F(s,q)-F(0,q),\qquad
 \mathcal A_qF(s,q)=F(s,q)-F(s,0)
\]

commute, and the complete exact identity is

\[
 H_{s,q}=\mathcal A_s\mathcal A_qH_{s,q}
          +H_{s,0}+H_{0,q},
 \qquad H_{0,0}=0.
 \tag{3.6}
\]

The last two terms are the exact axial complement; neither is killed by the
far gate in (3.2). Moreover, using (3.6) inside the original sum does not
restrict those complements to axial pairs: \(H_{s,0}\) and \(H_{0,q}\)
are evaluated for every original \((s,q)\).

For a genuine local summation by parts, the character-compatible difference
in the first direction and the unit difference in the second are

\[
 \delta_sF(s,q)=F(s+1,q)-F(s,q),\qquad
 \delta_qF(s,q)=F(s,q+1)-F(s,q).
 \tag{3.7}
\]

For fixed \((h,k)\), zero-extend

\[
 b_{s,q}=a(h,k)\overline{a(h+2s,k+q)}G(s,q)
\]

outside its exact finite support. Choose any bounding rectangle
\([m,n]\times[r,t]\). With

\[
 B_{i,j}=\sum_{s=m}^{i}\sum_{q=r}^{j}b_{s,q},
\]

two-dimensional Abel summation gives the exact formula

\[
\begin{split}
 \sum_{s=m}^{n}\sum_{q=r}^{t}b_{s,q}H_{s,q}
 &=B_{n,t}H_{n,t}
 -\sum_{i=m}^{n-1}B_{i,t}\,\delta_sH_{i,t}
 -\sum_{j=r}^{t-1}B_{n,j}\,\delta_qH_{n,j}\\
 &\quad+\sum_{i=m}^{n-1}\sum_{j=r}^{t-1}
 B_{i,j}\,\delta_s\delta_qH_{i,j}.
\end{split}
 \tag{3.8}
\]

The first term and the next two sums are, respectively, the corner and both
edge corrections. They do not vanish merely because \(H_{0,0}=0\).

To display every gate correction, in \((s,q)\)-coordinates

\[
 \Delta=hq+2s(k+q),\qquad \rho=hq-2sk.
\]

Writing \(J(u)=\mathbf1_{\{|u|>L\}}\), one has exactly

\[
\begin{split}
 \delta_sG={}&[J(\Delta+2(k+q))-J(\Delta)]J(\rho-2k)\\
 &+J(\Delta)[J(\rho-2k)-J(\rho)],\\
 \delta_qG={}&[J(\Delta+h+2s)-J(\Delta)]J(\rho+h)\\
 &+J(\Delta)[J(\rho+h)-J(\rho)],\\
 \delta_s\delta_qG={}&G_{s+1,q+1}-G_{s+1,q}-G_{s,q+1}+G_{s,q}.
\end{split}
 \tag{3.9}
\]

If differences are transferred onto \(b=cG\), the full product rule is

\[
\begin{split}
 \delta_s\delta_q(cG)
 ={}&(\delta_s\delta_qc)T_sT_qG
 +(\delta_qc)T_q\delta_sG
 +(\delta_sc)T_s\delta_qG
 +c\,\delta_s\delta_qG,
\end{split}
 \tag{3.10}
\]

where \(T_s,T_q\) are the forward shifts. Zero extension makes every entry
and exit of the literal block an additional, fully included support-boundary
jump in the corresponding difference of \(c\). Thus (3.8)--(3.10) leave no
unlisted endpoint, gate, or support correction.

### 3.4 Complete power ledger

Let

\[
 M_{\mathrm{df}}=
 \sum_{\mathcal D}G|W|.
\]

The frozen packet states the direct positive capacity
\(M_{\mathrm{df}}\ll_\varepsilon L^4X^\varepsilon\). Since

\[
 |H|\le2,\qquad |D_hD_kH|\le4,
 \qquad |\delta_sH|,|\delta_qH|\le2,
 \qquad |\delta_s\delta_qH|\le4,
\]

the ledger is:

| piece | positive information supplied | resulting capacity |
|---|---:|---:|
| original far sum | \(|H|\le2\) | \(L^4X^\varepsilon\) |
| four-corner \((-- )\) commutator | bounded four-term scalar | \(L^4X^\varepsilon\) |
| other three parity projections | bounded scalar, no cancellation estimate | \(L^4X^\varepsilon\) |
| support-crossing boundary (2.2) | submass of \(M_{\mathrm{df}}\) only | \(L^4X^\varepsilon\) |
| axial complement (3.6) | each scalar bounded by \(2\) | \(L^4X^\varepsilon\) absent an axial mass lemma |
| Abel corner and two edges | trivial prefix bound only | no gain over \(L^4X^\varepsilon\) |
| gate/support jumps (3.9)--(3.10) | jumps are \(0,\pm1\), but no sparse-count or variation lemma | no gain over \(L^4X^\varepsilon\) |

The target is \(L^3X^\varepsilon=M_{\mathrm{df}}/L\). Coordinate
bijection, averaging by four involutions, and bounded finite differences cost
or save only absolute constants. Formula (3.8) could save \(L\) only after a
new bound for the relevant rectangular prefix sums \(B_{i,j}\), together
with all edge, gate-jump, and support-jump contributions. Trivially
\(|B_{i,j}|\le\sum|b_{s,q}|\), which supplies no \(L^{-1}\). Hence the power
ledger stops exactly at \(L^4X^\varepsilon\).

## 4. First doubtful or unproved step

The first unsupported step in a purported commutator proof is the replacement
of the complete scalar by its \((-- )\) projection, equivalently the omission
of (2.7). This happens before any analytic estimation. It is already false on
the exact sectors \(p=0\) and \(q=0\), where \(D_hD_kH=0\) but \(H\) can be
nonzero and \(G=1\).

If one instead starts with coordinate Abel summation, the first unsupported
step is a claimed \(L^{-1}\) saving for the prefix sums \(B_{i,j}\) while
discarding the corner, both edges, and the gate/support jumps in
(3.8)--(3.10). The fixed-\(p\) character product (3.1) gives no such prefix
estimate. Proving the required literal coefficient estimate would be a new
input, not a consequence of the zero-subtracted scalar.

## 5. Required control tests and outcomes

### 5.1 Constant character product

Replace \(\chi_4(h)\chi_4(h+p)=(-1)^s\) by \(1\). Equations
(2.1)--(3.10) are unchanged. In fact, the true character product is itself
invariant under both coordinate swaps, so it cannot isolate the \((-- )\)
projection. **Outcome: the scalar route survives the false constant-character
control and therefore has not isolated the required literal cancellation.**

### 5.2 Erased gcd and slanted structures

Replace the low-gcd weight and the slanted/block factors by arbitrary bounded
arrays, or by constants on the same support. All scalar, gate, swap, and Abel
identities remain exact; the power ledger remains \(L^4X^\varepsilon\).
**Outcome: the route survives erasure of precisely the structures from which
a literal saving would have to come.**

### 5.3 Arbitrary phase-adapted coefficients

As an adversarial algebraic control, put

\[
 a_x=c_x\overline{z_x},\qquad c_x\ge0,
 \qquad z_x=e(\sqrt X\sqrt{h_xk_x}).
\]

Because the far relation is symmetric in the ordered pair,

\[
 \sum_{x,y:\,\mathrm{df}}a_x\overline{a_y}
 (z_x\overline{z_y}-1)
 =\sum_{x,y:\,\mathrm{df}}c_xc_y
   [1-\cos(\arg z_x-\arg z_y)]\ge0.
 \tag{5.1}
\]

Whenever a positive proportion of the far mass has phase separation bounded
away from zero, (5.1) has positive-order capacity rather than a forced
factor-\(L\) cancellation. Every identity above still holds. **Outcome: the
scalar identities are compatible with phase-adapted positive accumulation;
positive norms cannot manufacture the missing saving.** This is a diagnostic
control of the method, not a claim that the literal coefficient equals this
adversarial model.

No numerical experiment was needed: all three controls are exact finite
algebraic tests.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m2-balanced-critical-j1-two-defect-commutator-gate/blind_statement.md`.

No proof graph, active campaign, strategy file, prior round, barrier packet,
source material, sibling report, synthesis, validation matrix, proof draft,
or web source was inspected. The derivation depends only on the displayed
definition of \(a\), finiteness of its support, the displayed phase and gates,
and the stated direct positive capacity.

## 7. Recommended state effect

**Reject the scalar-only two-direction commutator/summation-by-parts route in
its present form; retain (171.B1) as unresolved.** Record the exact no-go:
the complete scalar equals a double-commutator piece only after adding three
parity complements and the support-crossing boundary; the axial sectors are
annihilated by the commutator but not by the far gate; and the full positive
ledger remains \(L^4X^\varepsilon\). Promotion would require a new literal
coefficient lemma that saves \(L\) simultaneously for the parity complement,
support crossings, Abel edges, axes, and gate/support jumps.

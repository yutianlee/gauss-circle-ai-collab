# Round 122 report: literal two-adic complementary-divisor attack

- Campaign: `m9-m1-near-square-complementary-divisor-gate`
- Task: `literal_two_adic_complementary_divisor_attack`
- Role: discovery, selected context
- Starting graph: `3e85caebbaf6c69d0019009bee3ce8f720f34f579bfb0cfa2035b92be0fb2c13`
- Status: candidate evidence only

## 1. Result: uniform localization, strict safe strata, and an exact self-return

Write (e(t)=e^{2\pi i t}), (R=X^{1/4}),
(y=\lfloor\sqrt X\rfloor), (N=\lfloor X\rfloor), and use

\[
 \widehat f(k)=\int_{\mathbb T}f(t)e(-kt)\,dt.
\]

The exact Round-121 weight has two distinct uniform Fourier scales.  If

\[
 F(k)=\widehat J(k),\qquad
 W(k)=F(k)-F(k+1)=\widehat K(k),\qquad
 K(t)=J(t)(1-e(-t)),
\]

then, for every integer (A\ge 2),

\[
 \boxed{
 |W(k)|\ll_A
 \min\left(R^{-1},(1+|k|)^{-1},
 {y^{A-1}\over(1+|k|)^A}\right)
 \ll_A {1\over R+|k|}
 \left(1+{|k|\over y}\right)^{1-A}.}
\tag{1.1}
\]

The (1/|k|) middle range is real: cancellation of the formal (1/t)
singularity does not remove the one-sided (1/y) transition.  Also

\[
 \boxed{|F(k)|\ll_A
 \min\left(\log(2R),{y^A\over(1+|k|)^A}\right).}
\tag{1.2}
\]

Put (M=\lfloor yR\rfloor\asymp R^3=X^{3/4}).  Uniformly in real (X),

\[
 \sum_{|k|>M}D_N(k)W(k)=O(1).
\tag{1.3}
\]

Exact Abel summation and sample exactness give the second, more useful,
form

\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{k\in\mathbb Z}A_y(N+k)F(k)
 =\sum_{|k|\le M}A_y(N+k)F(k)+O(1),}
\tag{1.4}
\]

where (A_y(m)=\sum_{d\le y,\ d\mid m}\chi _4(d)), with the accepted
(d\mid0) convention.  Every retained (m=N+k) is positive and

\[
 m=X+O(X^{3/4}),\qquad \sqrt m=y+O(R).
\tag{1.5}
\]

For (m>0), write (m=2^a m_0), (m_0) odd, and put

\[
 \sigma=\chi _4(m_0)\in\{1,-1\},\qquad z={m_0\over y},
 \qquad S(m_0)=\sum_{d\mid m_0}\chi _4(d)={r_2(m)\over4},
\]

\[
 L_z(m_0)=\sum_{\substack{q\mid m_0\\q<z}}\chi _4(q).
\]

The exact formula for every (a\ge0) is

\[
 \boxed{A_y(m)=S(m_0)-\sigma L_z(m_0)
 =\sigma\sum_{\substack{q\mid m_0\\q\ge z}}\chi _4(q).}
\tag{1.6}
\]

Thus the full (r_2/4) coefficient and the complementary tail occur
together, exactly once.  For (sigma=-1), (S(m_0)=0) and
(A_y(m)=L_z(m_0)).  For (sigma=+1), the complement reinforces rather
than cancels.

There are two genuine target-safe deletions.

1. If (a_0=\lceil\log _2R\rceil), the complete aggregate with
   (v_2(N+k)\ge a_0), retaining (A_y) rather than separating its two
   terms in (1.6), is

   \[
    \ll_\varepsilon RX^\varepsilon.
   \tag{1.7}
   \]

2. On the odd branch (a=0, \sigma=+1), the central complementary band
   has total Fourier mass (O(\log(2R))).  Consequently that branch is,
   at target scale, one half of its full (r_2/4) wave.  All square fixed
   points in this band are included once.  The hard sample (d=y), if it
   is nonzero, and all remaining square fixed-point atoms separately have
   total (O(\log ^2(2X))) mass.

After these deletions the low-two-adic survivor still has absolute
capacity (y=R^2), not (R).  Re-expanding (1.6) proves an exact return:
the full divisor wave minus its complementary (d>y) tail is precisely
the original (d\le y) Round-121 wave.  No genuinely signed
noninvertible inequality for the remaining complete wave was obtained.
The outcome is therefore a **strict target-safe subpackage plus a rigorous
self-return**, not the lower-GAR estimate.

## 2. Exact statement and hypotheses

The hypotheses are exactly those of the Round-121 reduction.  In
particular, (eta) and (V_{\rm low}) are the fixed smooth profiles used
there, (J) is supported on the small positive arc, and

\[
 J(t)=\eta(yt){V_{\rm low}(4R^2t^2)\over t}.
\tag{2.1}
\]

There are fixed profile-dependent constants (c,C>0) such that the
nonzero part lies in (c/y\le t\le C/R); the extension by zero is smooth
and periodic.  No seminorm is asserted to be uniform without its displayed
power of (y).

For the exact central formulas define

\[
 C_-(m_0)=\sum_{\substack{d\mid m_0\\z\le d\le y}}\chi _4(d)
 \quad(z\le y),
\qquad
 C_+(m_0)=\sum_{\substack{d\mid m_0\\y<d<z}}\chi _4(d)
 \quad(z>y).
\tag{2.2}
\]

Then

\[
\begin{array}{c|c|c}
 &\sigma=+1&\sigma=-1\\ \hline
 z\le y&A_y=(S+C_-)/2&C_-=0,\quad A_y=L_z\\[2mm]
 z>y&A_y=(S-C_+)/2&C_+=0,\quad A_y=L_z.
\end{array}
\tag{2.3}
\]

The inequalities in (2.2) are literal.  The original cutoff is (d\le y),
the tail is (d>y), and hence its complementary cutoff is (q<z).
If (y\mid m_0), the original hard divisor (d=y) is included and its
partner (q=z) is excluded from (L_z).  A fixed point
(d=q=\sqrt{m_0}) occurs only on the (sigma=+1) branch and is counted
once in the appropriate central band.  Formula (2.3) does not divide that
fixed point twice.

On the retained window, if (s=N-y^2), then (0\le s\le2y) and

\[
 z={y\over2^a}+{s+k\over2^ay},\qquad
 \left|z-{y\over2^a}\right|\le {R+3\over2^a}.
\tag{2.4}
\]

In particular (z=y+O(R)) for (a=0), whereas (z<y) for every
(a\ge1) once (X) is large.

Here is the capacity table; logarithms are absorbed into (X^\varepsilon)
in the third column.

| Stratum | Exact coefficient | Absolute Fourier capacity | Outcome |
|---|---:|---:|---|
| (a=0, \sigma=+1, z\le y) | ((S+C_-)/2) | central (C_-): (O(\log X)); (S): (yX^\varepsilon) | central safe; half-full wave survives |
| (a=0, \sigma=+1, z>y) | ((S-C_+)/2) | central (C_+): (O(\log X)); (S): (yX^\varepsilon) | central safe; half-full wave survives |
| (a=0, \sigma=-1) | (L_z), (S=0) | (yX^\varepsilon) | cutoff merely moves from (y) to (z=y+O(R)); self-return |
| (1\le a<a_0, \sigma=+1) | (S-L_z=(S+C_-)/2) | ((y/2^a+1)X^\varepsilon) | full and tail both unresolved |
| (1\le a<a_0, \sigma=-1) | (L_z), (S=0, C_-=0) | ((y/2^a+1)X^\varepsilon) | strict smaller threshold, but still above target |
| (a\ge a_0), either residue | complete (A_y) | total over all such (a): (RX^\varepsilon) | target-safe by two-adic sparsity |
| hard (d=y) and square fixed points | literal boundary atoms, once | (O(\log^2X)) | target-safe; no boundary loss |

For a concise target-equivalent survivor, let ({\cal O}_\pm) denote the
retained odd (m) with (sigma=\pm1).  Then

\[
\begin{split}
 \mathfrak S_M={}&{1\over2}
 \sum_{\substack{|k|\le M\\m=N+k\in{\cal O}_+}}
 S(m)F(k)
 +\sum_{\substack{|k|\le M\\m=N+k\in{\cal O}_-}}
 L_{m/y}(m)F(k)\\
 &+\sum_{\substack{|k|\le M\\1\le a=v_2(m)<a_0}}
 \left\{S(m_0)-\chi _4(m_0)L_{m_0/y}(m_0)\right\}F(k).
\end{split}
\tag{2.5}
\]

The proved conclusion is

\[
 \boxed{\mathcal B_{\rm flat}^{(N)}=\mathfrak S_M
 +O_\varepsilon(RX^\varepsilon).}
\tag{2.6}
\]

The separately priced hard and square atoms may be deleted from
(\mathfrak S_M) as well, with an additional (O(\log^2X)), provided an
owner order deletes each atom only once.

## 3. Proof and derivation

### 3.1 Uniform Fourier norms

Set

\[
 q(t)={1-e(-t)\over t},
\]

with its smooth value at (t=0).  Thus
(K(t)=\eta(yt)V_{\rm low}(4R^2t^2)q(t)).  The lower transition has width
(O(1/y)), the upper radial transition has width (O(1/R)), and (q)
has bounded derivatives on the fixed small arc.  Direct differentiation
therefore gives

\[
 \|K\|_1\ll R^{-1},\qquad
 \|K^{(r)}\|_1\ll_r y^{r-1}\quad(r\ge1).
\tag{3.1}
\]

The factor (1/t) in (J) instead gives

\[
 \|J\|_1\ll\log(2R),\qquad
 \|J^{(r)}\|_1\ll_r y^r\quad(r\ge1).
\tag{3.2}
\]

For example, on the (1/y) transition a term with (r) derivatives has
height (O(y^{r+1})) for (J) and (O(y^r)) for (K), over length
(O(1/y)).  On the remaining arc, integration of (t^{-r-1}) gives the
same (y^r) bound for (J).  The (R)-scale terms are smaller because
(y\asymp R^2).

Repeated periodic integration by parts in (3.1)--(3.2) proves (1.1)--(1.2).
This also explains why fixed-(X) Schwartz decay alone was insufficient:
its constants grow exactly as the powers of (y) displayed above.

For every (d),

\[
 \left\lfloor{N+k\over d}\right\rfloor-
 \left\lfloor N/d\right\rfloor-{k\over d}
 =\{N/d\}-\{(N+k)/d\},
\]

so (|D_N(k)|\le y).  Taking (A=3) in (1.1) gives

\[
 \sum_{|k|>M}|D_N(k)W(k)|
 \ll y\,y^2M^{-2}\ll1,
\]

which proves (1.3).

### 3.2 Exact Abel identity and the positive window

Let (c_y=\sum_{d\le y}\chi _4(d)/d).  For every integer (k),

\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y.
\tag{3.3}
\]

The fixed-(X) decay is enough to justify exact two-sided Abel summation,
and hence

\[
 \sum_kD_N(k)(F(k)-F(k+1))
 =\sum_k(A_y(N+k)-c_y)F(k).
\tag{3.4}
\]

Poisson sampling gives
(\sum_kF(k)=\sum_{n\in\mathbb Z}J(n)=0): the support contains no
nonzero integer and the one-sided cutoff makes (J(0)=0).  This proves the
first equality in (1.4).  Since (|A_y(m)|\le y), taking (A=5) in
(1.2) yields

\[
 \sum_{|k|>M}|A_y(N+k)F(k)|
 \ll y\,y^5M^{-4}\ll1,
\]

which proves the second equality.  Finally,
(N-M>0) for all sufficiently large (X), and
(N-y^2\in[0,2y]), proving (1.5) and (2.4).

### 3.3 Every two-adic and character branch

Only odd divisors contribute to (A_y(2^am_0)), so its divisors are
exactly the divisors of (m_0).  Under (d\mapsto q=m_0/d),

\[
 d>y\quad\Longleftrightarrow\quad q<{m_0\over y},
 \qquad
 \chi _4(d)=\chi _4(m_0)\chi _4(q)=\sigma\chi _4(q).
\tag{3.5}
\]

Consequently

\[
 \sum_{\substack{d\mid m_0\\d>y}}\chi _4(d)=\sigma L_z(m_0),
\]

which proves (1.6).  The same involution on the full divisor set gives
(S=\sigma S); hence (S=0) when (sigma=-1).

If (z\le y), split the divisors into
(d<z), (z\le d\le y), and (d>y).  The last sum is (sigma L_z),
so

\[
 S=(1+\sigma)L_z+C_-,\qquad A_y=L_z+C_-.
\]

This is the first line of (2.3).  If (z>y), then
(L_z=A_y+C_+) and

\[
 S=A_y+\sigma L_z=(1+\sigma)A_y+\sigma C_+,
\]

which is the second line.  These partitions prove all strict/weak boundary
claims, including the fixed-point convention.

### 3.4 The target-safe strata

The envelope (1.2) implies the progression-sampling bound, uniformly in
(b\) and (Q\ge1),

\[
 \sum_{k\equiv b\ ({\rm mod}\ Q)}|F(k)|
 \ll_A \left(1+{y\over Q}\right)\log(2R).
\tag{3.6}
\]

Indeed there are (O(1+y/Q)) points with (|k|\le y), and the dyadic
annuli (|k|\asymp2^jy) contribute a convergent geometric tail by (1.2).
On the localized window (m\asymp X), the elementary divisor bound gives
(|A_y(m)|\le\tau(m)\ll_\varepsilon X^\varepsilon).  The set
(v_2(m)=a) is contained in (k\equiv-N\pmod {2^a}).  Summing (3.6) for
(a\ge a_0) gives

\[
 \sum_{\substack{|k|\le M\\v_2(N+k)\ge a_0}}
 |A_y(N+k)F(k)|
 \ll_\varepsilon X^\varepsilon\log(2R)
 \left(\log(2X)+{y\over2^{a_0}}\right)
 \ll_\varepsilon RX^{2\varepsilon},
\]

which is (1.7) after relabelling (\varepsilon).

For the odd (sigma=+1) central band, write (s=N-y^2\in[0,2y]).
When (m\le y^2), the condition (z\le d\le y) is equivalent, after
(m=dq), to (d,q\le y).  Put (d=y-u,q=y-v).  Localization forces
(u,v=O(R)), and

\[
 |dq-N|=s+y(u+v)-uv.
\]

Apart from (u=v=0), the right side is
(\gg y(u+v)).  There are (n+1) ordered pairs with (u+v=n), so (1.2)
with (A>2) gives a convergent (sum n^{1-A}), plus one
(O(\log(2R))) term.

When (m>y^2), the central condition is (d,q>y).  Put
(d=y+u,q=y+v), (u,v\ge1).  Then

\[
 dq-N=y(u+v)+uv-s.
\]

Only the finitely many (u+v\le3) can have size (O(y)); for
(u+v\ge4) it is (\gg y(u+v)).  The same summation proves

Define \(C_{\rm cent}(m)=C_-(m)\) for \(m\le y^2\) and
\(C_{\rm cent}(m)=C_+(m)\) for \(m>y^2\).  Then

\[
 \sum_{\substack{|k|\le M\\a=0,\ \sigma=+1}}
 |C_{\rm cent}(m)F(k)|\ll\log(2R).
\tag{3.7}
\]

This argument counts ordered complementary pairs and counts (d=q)
only once, so it includes every square tie correctly.

If (y) is odd, the hard (d=y) atoms have the form
(m=2^ayq), (q) odd.  Applying (3.6) with modulus (2^ay) and summing
over (a) gives (O(\log^2(2X))); if (y) is even their character is
zero.  For a square fixed point (m_0=r^2), consecutive admissible (r)'s
near (2^ar^2\asymp X) are separated in (m) by
(\gg2^{a/2}y).  Equation (1.2), followed by summation over (a), again
gives (O(\log^2(2X))).  These are boundary prices, not additional copies
of atoms already included in (2.3).

For reference, expanding the complementary tail directly also gives, on
the (a)-th slice,

\[
 \sum_{\substack{q,d\ {\rm odd}\\d>y,\ |2^aqd-N|\le M}}
 |F(2^aqd-N)|
 \ll {y\over2^a}\log^2(2X),
\tag{3.8}
\]

because (q\ll y/2^a) and (3.6) is applied with modulus (2^aq).
This proves the capacities in the table.  It reaches the target only once
(2^a\gg R); below that threshold it leaves a positive power loss.

### 3.5 Exact one-count return

Inside the positive localized window define

\[
 \mathfrak F_M=
 \sum_{\substack{a\ge0,\ d,q\ {\rm odd}\\
 |2^adq-N|\le M}}
 \chi _4(d)F(2^adq-N)
\tag{3.9}
\]

and

\[
 \mathfrak T_M=
 \sum_{\substack{a\ge0,\ d,q\ {\rm odd}\\
 d>y,\ |2^adq-N|\le M}}
 \chi _4(d)F(2^adq-N).
\tag{3.10}
\]

Expanding (S(m_0)) gives (3.9).  In the tail term
(sigma L_z), put (d=m_0/q).  Then (d>y) and
(sigma\chi _4(q)=\chi _4(d)), giving (3.10).  Therefore, coefficient
by coefficient,

\[
 \boxed{
 \mathfrak F_M-\mathfrak T_M
 =\sum_{\substack{a\ge0,\ d,q\ {\rm odd}\\
 d\le y,\ |2^adq-N|\le M}}
 \chi _4(d)F(2^adq-N)
 =\sum_{|k|\le M}A_y(N+k)F(k).}
\tag{3.11}
\]

This is the literal Round-121 sharp cone.  Thus full (r_2/4) completion
followed by exact complementary subtraction is not a contraction; it is a
partition of the same product incidences.  Fourier inversion or crossing
Abel summation of the right side returns to the Round-121 cone and to the
Round-65 unmatched-crossing obstruction class.  Equations (1.7) and (3.7)
are lawful inequalities that remove strict subpackages, but (3.11) proves
that the remaining complement operation itself is an exact self-return.

## 4. First doubtful or unproved step

There is no unproved step in (1.1)--(3.11).  The first genuinely unproved
inequality is

\[
 \boxed{\mathfrak S_M\ll_\varepsilon RX^\varepsilon.}
\tag{4.1}
\]

The low slices (2^a<R) have separate absolute capacities
(y/2^a), whose sum is still (\asymp y=R^2).  In particular:

- the odd (sigma=+1) branch retains a full (r_2/4) wave after its
  narrow central band is removed;
- the (sigma=-1) branch retains the complementary prefix (L_z), and
  at (a=0) its threshold is merely (y+O(R));
- the (1\le a<a_0), (sigma=+1) branches retain the full coefficient
  and the broad central/complement term jointly.

A proof of (4.1) must be jointly signed across (k), the low two-adic
levels, residue branches, and full-versus-tail labels.  Bounding
(mathfrak F_M) alone by a quarter-scale circle discrepancy would import
the desired theorem (or an unaudited short-interval equivalent); bounding
(mathfrak F_M) and (mathfrak T_M) separately is not provided by any
accepted input.  Recombining them without an inequality is exactly
(3.11).

## 5. Required controls and outcomes

| Control | Outcome | Reason |
|---|---|---|
| `exact_Round121_discrepancy` | PASS | Started from (122.D1)--(122.D5); (3.3)--(3.4) preserve the Fourier sign, density subtraction, and all integers. |
| `uniform_wavelet_envelope` | PASS | (3.1) prices the (1/y) transition and proves the three-range envelope (1.1). |
| `far_k_tail_budget` | PASS | With (M=yR), the original (DW) tail and the Abelized (A_yF) tail are both (O(1)). |
| `positive_near_square_window` | PASS | (N-M>0), (m=X+O(X^{3/4})), and (sqrt m=y+O(R)). |
| `two_adic_divisor_involution` | PASS | (1.6) holds for every (a\ge0) and uses (m_0/y), never (m/y), on even (m). |
| `character_residue_branches` | PASS | (sigma=-1) annihilates (S) and the central band; (sigma=+1) reinforces it as in (2.3). |
| `square_and_central_boundaries` | PASS | Strict/weak inequalities are explicit; fixed points are counted once; central odd mass is (O(\log X)), and all square atoms are (O(\log^2X)). |
| `full_divisor_and_complement_one_count` | PASS | (3.9)--(3.11) insert the full coefficient and subtract exactly the (d>y) tail, leaving (d\le y) once. |
| `signed_k_aggregation` | PASS for hygiene; estimate OPEN | No norm is taken on the unresolved survivor.  Absolute values occur only after a stratum is proved target-safe. |
| `circle_problem_noncircularity` | PASS | The only analytic inputs are profile norms, progression sampling, and the elementary divisor bound.  The full (r_2) wave is left unestimated. |
| `old_return_map_nonduplication` | PASS | (3.11) is explicitly classified as the Round-121/Round-65 return, not as a new gain. |
| `false_unsigned_control` | PASS | With (chi _4) replaced by (1), central pairs reinforce and (3.11) remains a capacity-preserving incidence partition.  No sign-insensitive target conclusion is claimed. |
| `one_count_downstream_scope` | PASS | Only the lower-GAR child is refined; no blockwise or M2 implication is asserted. |

## 6. Dependencies and exact artifacts used

Analytical dependencies used:

- the accepted Round-121 exact discrepancy and sample-exact periodic
  interpolant;
- the elementary identity
  (r_2(m)/4=\sum_{d\mid m}\chi _4(d));
- the accepted elementary divisor bound
  (\tau(n)\ll_\varepsilon n^\varepsilon);
- elementary periodic Fourier integration by parts, Poisson sampling, Abel
  summation, and divisor complementation.

Exact files read and used:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `strategy/conductor_0821_full_proof_strategy.md`;
- `rounds/codex-managed/m9-m1-reciprocal-product-wavelet/synthesis.md`;
- `rounds/codex-managed/m9-m1-product-wavelet-local-discrepancy/synthesis.md`;
- `rounds/codex-managed/m9-m1-unmatched-crossing-fourier-modes/synthesis.md`;
- `rounds/codex-managed/m9-m1-global-lower-height-kernel-gate/synthesis.md`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/derivation_packet.md`;
- `rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/briefs/literal_two_adic_complementary_divisor_attack.md`.

No sibling Round-122 report, unpermitted historical report, web source, or
numerical experiment was used.

## 7. Recommended state effect

**Promote, after independent seam review, only the following scoped
package:**

1. the uniform envelopes (1.1)--(1.2), (M=yR) target-safe localization,
   and positive near-square window;
2. the exact all-(a), all-residue complement formulas
   (1.6), (2.3), including hard and square boundaries;
3. the target-safe high-two-adic aggregate, odd central band, hard sample,
   and square-tie packages;
4. the exact complementary-divisor self-return (3.11) as an obstruction to
   claiming a gain from full (r_2) completion alone.

**Retain open** `M9-M1-global-lower-radial-signed-estimate` with (4.1), or
its boundary-deleted version, as the smallest surviving inequality.
Consequently retain open `M9-M1-global-angular-radial-estimate` and GAR.
This report does not prove either direct blockwise `M9-M1` parent, any
`M9-M2` parent, endpoint uniformity, `M9`, or the Gauss-circle quarter
bound.  The internal (1/3) exponent and the separately audited external
(0.3144831759740614\ldots) benchmark are unchanged.

## Addendum A: second-stage audit of the conductor candidate

### A1. Result

I audited
'candidates/conductor_wavelet_localization_and_two_adic_split.md',
especially (122.C4)--(122.C15) and the revised cumulative central-factor
argument (122.C25)--(122.C28).

**Verdict.**  Every displayed mathematical estimate from (122.C4) through
(122.C28) is valid under one common fixed choice
\[
 0<\delta<\frac18
\tag{A.1}
\]
and sufficiently high integration-by-parts order.  The candidate proves
four target-safe packages: the far Fourier tail, the central Fourier-index
window, the complete high-two-adic cumulative projection, and the odd
positive-character cumulative central correction.  Its exact complement
formula is correct in every two-adic and residue branch.

There is no invalid displayed line in (122.C4)--(122.C28).  There are two
repairs:

1. the transition from (122.C15) to (122.C16) needs one explicit
   localized-centering/owner-order line;
2. the prose description of the “smallest survivor” after (122.C28) must
   incorporate the proved deletion of \(\Gamma/2\).  On the odd
   \(a=0,\chi _4(n)=1\) branch, the survivor is one half of the full
   coefficient, not the unreduced full-minus-complement pair.

Both repairs are target-safe and are given exactly below.  They do not
prove the remaining signed estimate.

### A2. Exact audited statement and corrected smallest survivor

To avoid using \(M\) both for a derivative order and a Fourier cutoff, let
\(B\ge3\) be the integration-by-parts order and put
\[
 K_\delta=yX^\delta.
\]
For the fixed Round-121 profiles, (122.C4)--(122.C6) give
\[
 \|G\|_1\ll R^{-1},\qquad
 \|G'\|_1\ll1,\qquad
 \|G^{(B)}\|_1\ll_B y^{B-1},
\tag{A.2}
\]
\[
 |W(k)|\ll_B
 \min\!\left(R^{-1},(1+|k|)^{-1},
 {y^{B-1}\over(1+|k|)^B}\right),
\tag{A.3}
\]
\[
 \sum_k|W(k)|\ll\log(2X),\qquad
 \sum_k|kW(k)|\ll y.
\tag{A.4}
\]

Define the oriented cumulative operator
\[
 {\cal I}_k f=
 \begin{cases}
  \displaystyle\sum_{1\le j\le k}f(N+j),&k>0,\\[2mm]
  0,&k=0,\\[2mm]
  \displaystyle-\sum_{k<j\le0}f(N+j),&k<0.
 \end{cases}
\tag{A.5}
\]
Then \(\widetilde D_N(k)=D_N(k)+kc_y={\cal I}_kA_y\).
Let
\[
 A_0=\lceil\log _2R\rceil.
\]
For a retained positive integer \(m=2^an\), \(n\) odd, define
\[
 H(m)=
 \begin{cases}
  \frac12\,a(n),
    &a=0,\ \chi _4(n)=1,\\[1mm]
  T_{n/y}(n),
    &a=0,\ \chi _4(n)=-1,\\[1mm]
  a(n)-\chi _4(n)T_{n/y}(n),
    &1\le a<A_0,\\[1mm]
  0,&a\ge A_0.
 \end{cases}
\tag{A.6}
\]
Here
\[
 a(n)=\sum_{d\mid n}\chi _4(d)=\frac{r_2(n)}4,\qquad
 T_z(n)=\sum_{\substack{q\mid n\\q<z}}\chi _4(q).
\]
The corrected smallest-survivor statement certified by the candidate is
\[
 \boxed{
 \mathcal B_{\rm flat}^{(N)}
 =\sum_{R<|k|\le K_\delta}W(k)\,{\cal I}_kH
 +O_{\varepsilon,\delta}(RX^\varepsilon).}
\tag{A.7}
\]
All full-divisor and complementary terms remain together in the third
line of (A.6); the negative-character odd branch remains the exact
noncontracting prefix; only the positive-character odd central correction
has been removed by (122.C25)--(122.C28).

### A3. Proof audit

For (122.C8), (A.3) and \(|D_N(k)|\le y\) give the exact exponent
\[
 \sum_{|k|>K_\delta}|D_N(k)W(k)|
 \ll_B y^B K_\delta^{1-B}
 \ll_B X^{\,1/2-\delta(B-1)}.
\tag{A.8}
\]
Thus an \(O(RX^{-A})\) tail follows whenever
\[
 \delta(B-1)\ge A+\frac14.
\tag{A.9}
\]
For the centering tail (122.C13a), the exact exponent is
\[
 \sum_{|k|>K_\delta}|kW(k)|
 \ll_B y^{B-1}K_\delta^{2-B}
 \ll_B X^{\,1/2-\delta(B-2)},
\tag{A.10}
\]
so it is \(O(RX^{-A})\) whenever
\[
 \delta(B-2)\ge A+\frac14.
\tag{A.11}
\]
A common valid integer choice is
\[
 B\ge
 \left\lceil2+\frac{A+1/4}{\delta}\right\rceil.
\tag{A.12}
\]
Equations (122.C8) and (122.C13a) therefore have the claimed arbitrary
power tails.  The displayed restriction \(\delta<1/4\) in (122.C9) is
more than sufficient for positivity; \(\delta<1/2\) would already make
\(K_\delta=o(X)\).  The later condition (A.1) is the operative common
choice.

For \(|k|\le R\), the recurrence
\[
 D_N(k)-D_N(k-1)=A_y(N+k)-c_y
\]
and the divisor bound give (122.C11).  Hence
\[
 \sum_{|k|\le R}|D_N(k)W(k)|
 \ll_\varepsilon R^{-1}X^\varepsilon
 \sum_{|k|\le R}|k|
 \ll_\varepsilon RX^\varepsilon,
\]
which verifies (122.C12).

The centering identity in (122.C13) has the correct sign:
\[
 \sum_k k\{F(k)-F(k+1)\}=\sum_kF(k)=J(0)=0.
\tag{A.13}
\]
Moreover, if \(Q=2^{A_0}\), each oriented interval contains at most
\(1+|k|/Q\) multiples of \(Q\).  Equations (A.4) and (122.C14) give
\[
 \sum_{|k|\le K_\delta}
 |\widetilde D_{\ge A_0}(k)W(k)|
 \ll_\varepsilon X^\varepsilon
 \left(\log(2X)+{y\over2^{A_0}}\right)
 \ll_\varepsilon RX^\varepsilon.
\tag{A.14}
\]
This verifies (122.C15) and, because it is an absolute estimate, also
verifies its restriction to \(R<|k|\le K_\delta\).

All two-adic thresholds can be stated without asymptotic ambiguity.  Put
\(s=N-y^2\), so \(0\le s\le2y\).  On \(m=N+j=2^an\),
\[
 {n\over y}
 ={y\over2^a}+{s+j\over2^ay},\qquad
 \left|{n\over y}-{y\over2^a}\right|
 \le {2+X^\delta\over2^a}.
\tag{A.15}
\]
Thus:

- at \(a=0\), the complementary threshold is
  \(y+O(1+X^\delta)\), so the negative-character branch does not
  contract;
- for every \(a\ge1\), \(m<2y^2\) and hence \(n<y^2\), so
  \(n/y<y\);
- the complementary tail is empty exactly when \(n/y\le1\), equivalently
  \(n\le y\); a uniform empty-tail condition over the window is
  \(2^a\ge(N+K_\delta)/y\asymp y\);
- target-safe two-adic sparsity starts much earlier, at
  \(2^a\ge2^{A_0}\asymp R\).  These intermediate high strata may still
  have a nonempty complement, but (A.14) removes their complete
  \(A_y\)-increment before any full/tail separation;
- the unresolved levels \(2^a<R\) have capacity
  \(y/2^a>R\) up to endpoint constants.

Finally, (122.C25)--(122.C27) are exact.  For a central occurrence
\((d,n/d)\), both ordered factors lie in an interval of length
\(O(1+X^\delta)\) adjacent to \(y\), and the occurrence-to-ordered-pair
map is injective.  The square pair \((y,y)\) is counted once.  Therefore
\[
 \sum_{|j|\le K_\delta}|\Gamma(N+j)|
 \ll(1+X^\delta)^2.
\tag{A.16}
\]
Its cumulative \(E={\cal I}\Gamma\) satisfies
\[
 \sum_{|k|\le K_\delta}|E(k)W(k)|
 \ll X^{2\delta}\log(2X)
 \ll_\varepsilon RX^\varepsilon
\tag{A.17}
\]
for (A.1).  This verifies the revised cumulative estimate (122.C28)
without truncated-Abel boundary terms.

### A4. First missing seam and repair

There is no false displayed estimate in the audited range.  The first
logical seam omitted from the prose occurs between (122.C15) and
(122.C16).  Equation (122.C12) controls the central window for \(D_N\),
whereas the high-two-adic split is made for \(\widetilde D_N\).  Insert
\[
 \left|
 c_y\sum_{|k|\le R}kW(k)\right|
 \le |c_y|R^{-1}\sum_{|k|\le R}|k|
 \ll R,
\tag{A.18}
\]
so the central window is target-safe for \(\widetilde D_N\) as well.
Then apply the absolute estimate (A.14) only on
\(R<|k|\le K_\delta\).  With owner order
\[
 \text{far tail}\ \longrightarrow\
 \text{central \(k\)-window}\ \longrightarrow\
 \text{medium-\(k\) high-\(v_2\) projection}\ \longrightarrow\
 \text{medium-\(k\), low-\(v_2\) \(\Gamma\)-correction},
\tag{A.19}
\]
no package is deleted twice.

The first substantive wording repair is later, in the “smallest survivor”
paragraph.  After (122.C26)--(122.C28), saying that *all* full and
complementary pieces remain together is too coarse if it includes the odd
positive-character branch.  Replace that sentence by (A.6)--(A.7).
The typographical string 'm=2^a n,qquad' before (122.C17) should also be
changed to \(m=2^an,\ n\) odd, but it has no mathematical effect.

### A5. Control outcomes

| Seam | Outcome | Audit |
|---|---|---|
| C4--C6 norms and moments | PASS | The \(1/y\) transition gives \(y^{B-1}\); both \(\ell^1\) moments have the stated sizes. |
| C8 far-tail exponent | PASS | Exact exponent is \(1/2-\delta(B-1)\), with condition (A.9). |
| C9 localized positivity | PASS | The final \(\delta<1/8\) gives \(K_\delta=o(X)\) and \(0<N+k<2X\). |
| C10--C12 central window | PASS | The recurrence is valid for both oriented signs and costs \(RX^\varepsilon\). |
| C13--C13a centering | PASS after explicit seam (A.18) | Exact exponent is \(1/2-\delta(B-2)\); no zero-mode or sign error occurs. |
| C14--C16 high two-adic projection | PASS after owner order (A.19) | It is a cumulative increment projection, not a terminal-index condition. |
| C18 strict complement | PASS | \(d\le y\) corresponds to \(q\ge n/y\); the omitted tail is strictly \(q<n/y\). |
| C19--C24 residue and thresholds | PASS | Negative character kills the full and central sums; positive character reinforces; (A.15) distinguishes all \(a\). |
| C25--C28 cumulative central factors | PASS | Ordered-pair counting gives \(X^{2\delta}\), and \(\delta<1/8\) is target-safe. |
| Hard \(d=y\) and square ties | PASS | \(d=y\) stays in the weak original cutoff and out of the strict tail; fixed points occur only for positive character and are counted once. |
| Strict packages | PASS with disjoint owner order | Four packages are safe; none estimates the low-two-adic medium-index survivor. |
| Smallest survivor | REVISE wording | The exact survivor is (A.6)--(A.7), not an unreduced odd positive-character full/tail pair. |

### A6. Dependencies and artifacts

This addendum used only:

- the initial report and its permitted Round-121 context;
- 'rounds/codex-managed/m9-m1-near-square-complementary-divisor-gate/candidates/conductor_wavelet_localization_and_two_adic_split.md';
- the accepted elementary divisor bound already recorded in
  'state/proof_obligations.yml'.

No sibling report, state file mutation, candidate edit, source import, or
numerical experiment was used.  The candidate was read-only.

### A7. Recommended state effect after the audit

Recommend **promote after the remaining independent reviews**:

1. (122.C4)--(122.C15), with exact exponent conditions
   (A.9)--(A.12) and the localized-centering seam (A.18);
2. (122.C18)--(122.C24), with the threshold distinctions in (A.15);
3. (122.C25)--(122.C28), including the cumulative—not pre-Abel—central
   factor estimate;
4. the disjoint strict-package decomposition and corrected survivor
   (A.6)--(A.7).

Recommend **revise**, not reject, the candidate's smallest-survivor prose
and insert owner order (A.19).  Retain
'M9-M1-global-lower-radial-signed-estimate',
'M9-M1-global-angular-radial-estimate', and GAR as open.  There is still
no implication for blockwise 'M9-M1', any 'M9-M2' parent, endpoint
uniformity, 'M9', or any exponent.

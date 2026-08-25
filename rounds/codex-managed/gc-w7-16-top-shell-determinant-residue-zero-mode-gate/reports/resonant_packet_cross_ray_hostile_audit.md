# Round 131 hostile audit: resonant packets do not yet define a cross-ray bank

Campaign: `gc-w7-16-top-shell-determinant-residue-zero-mode-gate`  
Task: `resonant_packet_cross_ray_hostile_audit`  
Role: hostile seam reviewer  
Starting graph SHA-256:
`23e7bfacbf6abc5582769fbe8d427cbca2379e1d265b99df21d93a65ec504825`  
Status: candidate review evidence only; no shared proof state is changed.

## 1. Result

The selected record supports a **strict-scope degeneracy verdict**, not a
residue bank and not a physical obstruction.

Three pieces of algebra are certifiable.

1. After physical Möbius reassembly, the fixed-ray chart
   \[
   n=aq-bp,\qquad b'=\frac{b(a+p)+n}{a},\qquad
   n\equiv-bp\pmod {|a|}
   \tag{131.H1}
   \]
   is exact and has bounded $p$-multiplicity on the stated top-shell
   support.  This remains a per-ray coordinate fact, not cancellation and
   not a cross-ray multiplicity bound.
2. The two M1 quarter branches translate a residue Fourier label by
   $h=\pm1\pmod {4|a|}$ on each fixed-$a'$ chart branch.  The physical
   M2 numerator-character product is the quarter mode $e(p/4)$; when
   $b$ is a unit modulo $4|a|$ and $q\pmod4$ is fixed, its induced
   $n$-mode is
   \[
   h_2\equiv-|a|\bar b\pmod {4|a|}.
   \tag{131.H2}
   \]
   Without that unit/parity branch, the determinant congruence does not
   determine $p\pmod4$, so there is no universal M2 mode in $n$.
3. The accepted same-denominator controls are literally aligned.  Their
   determinant-tapered mass is of order
   \[
   R:=\frac DW=Y^{1/16}=Y^{3/48}
   \tag{131.H3}
   \]
   per resonant packet, not $O(1)$.  The M2 identity survives the
   numerator sign convention exactly; however, a genuine opposite-sign
   M2 pair with both numerators of top size is excluded by the determinant
   support by the factor $Y^{5/48}$.

What is not certifiable is the first operation needed for a residue
estimate: the selected files do not give the physically reassembled
weight as a finite periodic-arithmetic/BV-envelope decomposition with a
quantitative variation ledger.  The placeholders $P$ and $T$ retain
the relevant floors, thresholds, stars, tapers, aliases, cells, and
owners, but no formula or variation estimate for their pullback to
$n$ is supplied.  The bound $\sum_t|c_{i,t}|\ll1$ alone does not fill
that gap.  Consequently, no Fourier expansion of the **full physical
weight**, no complete Gauss/Salié sum, and no cancellation estimate is
licensed.

The aligned packets are hostile per-ray controls only.  Their special
centres depend on $b$, and neither their integer near-resonant occupancy
nor their actual $A_i(a,b)$-weighted sum over different outer rays is
controlled.  Even ideal one-term-per-ray collapse stops at
$DK_D/L=Y^{27/48+o(1)}$, so a strict global improvement needs an actual
cross-ray gain.  Positive energy cannot be substituted for that scalar
statement.

## 2. Exact statement and hypotheses

Put
\[
M=4|a|,\qquad
N=\frac{D^2}{W}=Y^{27/48},\qquad
Q_*=\frac{D^2}{WL}=Y^{19/48},\qquad N\asymp LQ_*.
\tag{131.H4}
\]
Work on one half-open (B\asymp D) shell, one orientation, one
moving-symbol stratum, and one physical M1 or M2 sign sector.  The
following is the weakest legal separation statement.

After all Möbius, complete-lift, M1 branch, Stieltjes, and physical
primitive-ray pieces have been reassembled, partition the resulting
support into disjoint owner cells (lambda) on which the admissible
(p)-lift is single valued.  Extend every cell weight by zero off its
half-open support.  A residue Fourier expansion is legal only if one has
an identity
\[
w_r(n)=\sum_{\lambda=1}^{J_r}
       \mathcal P_{r,\lambda}(n)\mathcal V_{r,\lambda}(n),
\qquad
\mathcal P_{r,\lambda}(n+M)=\mathcal P_{r,\lambda}(n),
\tag{131.H5}
\]
and a proved finite ledger
\[
\mathfrak B_r:=
\sum_\lambda \|\widehat{\mathcal P}_{r,\lambda}\|_1
\left(
 \|\mathcal V_{r,\lambda}\|_\infty+
 \sum_n|\mathcal V_{r,\lambda}(n+1)-
             \mathcal V_{r,\lambda}(n)|
\right).
\tag{131.H6}
\]
Here the zero extension makes every support birth, support death,
threshold equality, star, cell face, determinant-taper endpoint,
reciprocal-alias boundary, and half-open shell owner appear exactly once
in the variation.  If a face is retained as a separate boundary atom, it
must be removed from the variation sum; it cannot be charged twice.  The
equal-ray diagonal (n=0) is separately owned and is not the zero
Fourier mode of the one-sided (n>0) scalar.

With the normalized transform
\[
\widehat{\mathcal P}(h)=\frac1M\sum_{u\bmod M}
 \mathcal P(u)e(-hu/M),
\tag{131.H7}
\]
(131.H5) gives the exact identity
\[
\sum_n w_r(n)e(\Phi_r(n))
=\sum_{\lambda}\sum_{h\bmod M}
 \widehat{\mathcal P}_{r,\lambda}(h)
 \sum_n\mathcal V_{r,\lambda}(n)
 e\!\left(\Phi_r(n)+\frac{hn}{M}\right).
\tag{131.H8}
\]
Discrete Abel summation then costs at most (131.H6) times the maximal
partial sum of the corresponding shifted phase.  Thus (131.H5)--(131.H6),
not mere period-four character notation, are the hypotheses required
before (131.H8) may be used quantitatively.

The exact carrier conclusions below use only these additional local
hypotheses when stated:

- for the M1 (n)-mode, (a') is fixed on the chart branch;
- for the single M2 (n)-mode, (b) is odd (hence a unit modulo
  (4|a|), since ((a,b)=1)) and (q\pmod4) is fixed;
- for the aligned-packet mass, the packet lies in the interior of every
  literal support/threshold face and the remaining amplitude is not
  asserted to have a sign;
- for the sign-crossing exclusion, (b,b'\asymp D>0) and
  (|a|,|a'|\asymp L).

The supplied hypotheses establish neither (131.H5) nor (131.H6) for the
literal physical coefficient.  All conclusions involving them are
therefore conditional separation lemmas, not claims about the accepted
physical weight.

## 3. Proof or derivation

### 3.1 Ordering and the conditional separation identity

The displayed scalar is still expanded in
$(\rho,\eta,t,g,v)$.  In particular, $\rho\mid a+p$, the threshold
$g\le t/(\rho v)$, the star, $P_{i,a+p}(g)$, and
$T_{i;r,p,\rho,D}(v)$ are coupled.  Taking a Fourier transform or an
absolute value in an individual $\rho$- or $t$-piece would replace
the physical primitive incidence by several algebraic representations.
The determinant chart is therefore introduced only after those pieces
have reconstructed the physical coefficient, as required by (131.H1).

Once (131.H5) is actually proved, (131.H8) follows by finite Fourier
inversion.  Abel summation on a subinterval (I) gives
\[
\left|\sum_{n\in I}\mathcal V(n)e(\Psi_h(n))\right|
\le
\left(\|\mathcal V\|_\infty+
\sum_n|\mathcal V(n+1)-\mathcal V(n)|\right)
\sup_{J\subseteq I}\left|\sum_{n\in J}e(\Psi_h(n))\right|,
\tag{131.H9}
\]
where $\Psi_h(n)=\Phi_r(n)+hn/M$.  This proves the conditional
separation lemma and also shows why \(\sum_t|c_{i,t}|\ll1\) is not by
itself enough: it prices the Stieltjes coefficients, but it gives no
bound for the number or size of the jumps of the pulled-back threshold,
floor, star, or alias masks in (n).

The determinant taper itself is harmless only after a lift branch is
fixed.  For fixed (a'=a+p),
\[
b'=\frac{ba'+n}{a},\qquad
\frac{n}{b'}=\frac{an}{ba'+n},
\tag{131.H10}
\]
so on a positive interior branch the one-sided taper is monotone and has
total variation (O(1)).  This does not control the jumps created when
the admissible (p)-lift, threshold, star, or owner changes.  Those are
exactly the missing terms in (131.H6).

Nor does the phase in (131.H10) force a Salié sum.  Its exact form is
\[
e\!\left(\frac{can}{\kappa_i b(ba'+n)}\right).
\tag{131.H11}
\]
The selected record supplies neither a complete residue system, an
integer additive phase at modulus (M), an inverse-unit condition for
(ba'+n), nor a completion/boundary estimate.  Quarter carriers and
(\chi_4) alone do not manufacture those missing hypotheses.

### 3.2 Shifted M1 and M2 carrier modes

For M1 the two displayed branches combine algebraically as
\[
\begin{aligned}
&\frac{\mu(\rho)}{\pi a'}e(\rho v/4)
-\frac{\mu(\rho)}{\pi a'}e(-\rho v/4)\\
&\hspace{25mm}=
\frac{2i\mu(\rho)}{\pi a'}\chi_4(\rho v).
\end{aligned}
\tag{131.H12}
\]
This is the local branch algebra that, with the common lift character,
restores the physical M1 denominator carrier.  On a fixed-(a') branch,
\[
e(\pm b'/4)
=e\!\left(\frac{\pm ba'}{4a}\right)
 e\!\left(\frac{\pm n}{4a}\right).
\tag{131.H13}
\]
Hence the carrier has the two shifted labels (h=\pm1\pmod {4a})
for (a>0), and (h=\pm\operatorname {sgn}(a)\pmod {4|a|}) in the
orientation-free notation.  It is false to test only (h=0).
Equation (131.H13) does not say that the full weight has only two modes:
the coefficient depending on (a'), the lift rule, and every other
periodic factor must still be convolved into the full transform.

For M2, if (a,a'=a+p) are odd, then (p=2s) and the physical signed
numerator characters satisfy
\[
\chi_4(a)\chi_4(a+p)=(-1)^s=e(p/4).
\tag{131.H14}
\]
Here the physical convention
(\operatorname {sgn}(x)\chi_4(|x|)=\chi_4(x)) is essential.  Suppose
now that (b) is odd and let (\bar b b\equiv1\pmod {4a}).  On a fixed
branch (q\equiv\gamma\pmod4), (131.H1) yields
\[
p\equiv\bar b(a\gamma-n)\pmod {4a},
\tag{131.H15}
\]
and therefore
\[
e(p/4)=e(\bar b a\gamma/4)
       e\!\left(\frac{-|a|\bar b\,n}{4|a|}\right).
\tag{131.H16}
\]
This proves (131.H2).  If (b) is even, no (\bar b\pmod {4a})
exists.  The congruence (n\equiv-bp\pmod a) determines (p\pmod a)
but not (p\pmod4), so (131.H14) is then an extra lift bit rather than a
scalar function of (n\pmod {4a}).  The selected hypotheses do not
state the parity split needed to repair this.  Thus the M2 quarter shift
is exact in (p), while a universal scalar M2 (n)-mode is not.

### 3.3 Literal same-denominator packets

Let (R=b/W\asymp D/W).  For M1 take
\[
q=0,\qquad p=-t,\qquad n=bt,
\qquad c=mb.
\tag{131.H17}
\]
Then
\[
e\!\left(\frac{cn}{b^2}\right)=e(mt)=1,
\qquad
1-\frac{Wn}{b^2}=1-\frac tR.
\tag{131.H18}
\]
The two physical denominators coincide, so their nonzero M1 carrier
product is (chi_4(d)^2=1).  If
(T=\lceil R\rceil-1), the literal taper mass is
\[
\sum_{t=1}^{T}\left(1-\frac tR\right)
=T-\frac{T(T+1)}{2R}
=\frac R2+O(1).
\tag{131.H19}
\]
Thus this is a polynomial-length aligned packet, even though each
displayed (n) has multiplicity one.

For the positive-numerator M2 packet take (a>0) odd,
\[
q=0,\qquad p=-2j,\qquad a'=a-2j>0,
\qquad n=2bj,qquad c=(4m+1)b.
\tag{131.H20}
\]
Since (R=Y^{1/16}\ll L=Y^{1/6}), all
(1\le j<2R) remain in a fixed interior top-numerator cell when (a)
is chosen away from its faces.  The determinant phase and character are
\[
e\!\left(\frac{cn}{4b^2}\right)
=e((4m+1)j/2)=(-1)^j,
\qquad
\chi_4(a)\chi_4(a-2j)=(-1)^j.
\tag{131.H21}
\]
Their product is (1), while the taper is
\[
1-\frac{Wn}{4b^2}=1-\frac{j}{2R}.
\tag{131.H22}
\]
For (J=\lceil2R\rceil-1),
\[
\sum_{j=1}^{J}\left(1-\frac{j}{2R}\right)
=J-\frac{J(J+1)}{4R}=R+O(1).
\tag{131.H23}
\]
Equations (131.H20)--(131.H23) are the required literal aligned-packet
calculation.  They prove compatibility and mass, not a lower bound for
the physical scalar, because the retained Stieltjes/profile amplitudes
can still cancel or vanish.

The sign-crossing convention passes algebraically.  For example,
(a=1,a'=-1) gives (j=1): the phase in (131.H21) is (-1), the
signed character product
(chi_4(1)\chi_4(-1)) is (-1), and the product is (+1).  Dropping
(epsilon_{\rm sgn}) would replace the second factor by
(chi_4(|-1|)=1) and reverse the result.

But this algebraic example is not a top-shell packet.  If (a,a') have
opposite signs while (|a|,|a'|\asymp L) and (b,b'\asymp D>0), then
\[
|ab'-a'b|=|a|b'+|a'|b\asymp LD,
\tag{131.H24}
\]
whereas the triangular support permits only
\[
|n|\ll\frac{D^2}{W},
\qquad
\frac{LD}{D^2/W}=\frac{WL}{D}=Y^{5/48}.
\tag{131.H25}
\]
Therefore opposite numerator signs are disjoint from the fixed
top-shell near-collision interior for large (Y).  A crossing through
(a'=0) belongs to a support face or a lower numerator cell and must be
owned there, not inserted into (131.H20).

### 3.4 Resonant-window mass and family scope

The small width of a resonant denominator window does not by itself
save a power.  For M1, write
\[
\frac cb=m+\delta.
\tag{131.H26}
\]
On the packet (1\le t\ll R), the residual phase is (e(\delta t)),
so (|\delta|\ll R^{-1}) is a coherent window.  Since
(c\asymp Y\asymp D^2), the real (b)-window about (b=c/m) has
length
\[
\left|\frac{db}{d(c/b)}\right|R^{-1}
\asymp\frac{b^2}{cR}\asymp R^{-1}=\frac WD.
\tag{131.H27}
\]
There are (asymp D) relevant integers (m), and their real centres
are separated by order one.  Hence their total continuous (b)-measure
is (asymp D/R=W).  Multiplying by the packet mass
(R=D/W) gives
\[
(\hbox{resonant }b\hbox{-window measure})
\times(\hbox{packet mass})\asymp W\frac DW=D.
\tag{131.H28}
\]
For M2 the centres are (c/b=4m+1), and after (131.H21) the residual
phase is (e(\delta j/2)); the same calculation, up to constants, gives
(131.H28).  Thus a window-count argument cannot declare the resonant
part lower order.  On the integer (b)-lattice, however, (131.H27) has
length (<1), so its occupancy and the signs of the actual outer
coefficients are a genuine cross-ray arithmetic problem.  The selected
record proves neither a lower occupancy nor cancellation.

A single periodic Fourier label is likewise not one residue class.  The
determinant range contains (N/M\asymp Q_*) full periods, and the M1
carrier coefficients in (131.H12) have constant size.  After Fourier
inversion such a mode is evaluated on the whole envelope; it is not
automatically divided by (M\asymp L).  Confusing “one mode” with “one
term” would manufacture the ideal (L)-gain.

At the post-inner scale, one (p)-lift costs (K_D/L).  Consequently the
capacity ladder is
\[
\begin{array}{c|c|c}
\text{mechanism} & \text{outer-triangle capacity} & \text{exponent}\\ \hline
\text{no residue gain} & DK_D & 35/48\\
\text{formal }\sqrt L\text{ per-ray gain} & DK_D/\sqrt L & 31/48\\
\text{one aligned packet of length }R & DK_D R/L & 30/48\\
\text{one term per ray} & DK_D/L & 27/48\\
\text{determinant target} & D & 24/48.
\end{array}
\tag{131.H29}
\]
The exact centre conditions (c=mb) and (c=(4m+1)b) vary with (b),
so (131.H17) and (131.H20) are not coherent-family lower bounds.  For a
fixed common (c), exact resonance restricts (b) to divisors of (c)
with the indicated quotient class; near resonance leads back to the
unresolved windows (131.H27).  The actual outer phases and
(A_i(a,b)) can therefore neither be aligned nor discarded from the
selected hypotheses.

Even granting the ideal per-ray floor, the stated outer norms only give
\[
\left|\sum_r A_i(r)F_r\right|\le
\left(\frac DL\right)^{1/2}
\left(\sum_r|F_r|^2\right)^{1/2}
\le \frac{DK_D}{L}=Y^{27/48+o(1)}
\tag{131.H30}
\]
when (|F_r|\le K_D/L) on (LD) rays.  A strict persistence
improvement needs (Y^{-\eta}) beyond (131.H30); the determinant target
needs the further factor (Y^{-3/48}=Y^{-1/16}).  This must be an
actual-family cross-ray theorem, not another per-ray Fourier relabelling.

Finally, the exact positive objects remain
\[
\mathbf1^*H^*H\mathbf1,
\qquad
b^*K_{B,+}^*K_{B,+}b,
\tag{131.H31}
\]
while (b^*G^2b) belongs only to the fully completed symmetric row.
None equals the single physical scalar, and no Loewner comparison to
(G^2) is supplied.  A positive energy theorem would control all
directions and may imply a scalar estimate by Cauchy; failure or
saturation of a coefficient-blind energy does not prove a lower bound
for the actual scalar.

## 4. First doubtful or unproved step

The first unproved step is the claimed **physical periodic/BV
separation**, before any complete-sum estimate.  The selected packet does
not display the reassembled weight (w_r(n)), a disjoint lift/owner
partition, or the variation quantity (131.H6).  In particular:

1. (sum_t|c_{i,t}|\ll1) does not control the pulled-back jumps of
   (g\le t/(\rho v)), frequency floors, stars, reciprocal aliases, or
   moving support faces;
2. bounded (p)-multiplicity does not make the lift single valued and
   does not determine (p\pmod4) in the even-(b) M2 branch;
3. separate (\rho)-piece Fourier expansions precede physical Möbius
   reassembly and can destroy the primitive coefficient;
4. the exact phase (131.H11) is incomplete and generally non-modular, so
   neither a quadratic Gauss sum nor a Salié sum follows from the carrier
   identities.

Only after these points are closed could one ask for cancellation of the
shifted complete sums.  After a per-ray estimate, the next independent
unproved step would still be (131.H30) with a strict actual-family gain.

## 5. Required control tests and outcomes

| Seam | Exact hostile test | Outcome |
|---|---|---|
| literal top-shell dictionary | Keep $W=Y^{7/16}$, $D=Y^{1/2}$, $L=Y^{1/6}$, $B\asymp D$, $\kappa_1=1$, $\kappa_2=4$, $n>0$, the determinant taper, and $K_D=Y^{11/48+o(1)}$. | **Pass.** Used in (131.H3)--(131.H4), (131.H19), (131.H23), and (131.H29). |
| physical Möbius reassembly | Attempt to expand a $(\rho,t,g,v)$ atom before reconstructing the physical primitive coefficient. | **Fail if attempted.** The chart and any residue Fourier expansion come only after reassembly. |
| periodic/BV separation before Fourier | Demand (131.H5), the full variation/face ledger (131.H6), and then apply (131.H8). | **Not established by the selected data.** This is the first missing identity. |
| shifted M1 mode modulo $4|a|$ | Combine the $\eta=\pm$ branches and substitute (131.H1). | **Pass with branch scope.** Modes $h=\pm\operatorname {sgn}(a)$; not a claim that the full weight has only those modes. |
| shifted M2 mode modulo $4|a|$ | Pull $e(p/4)$ through the determinant congruence. | **Conditional.** If $b$ is odd and $q\pmod4$ is fixed, $h=-|a|\bar b$; for even $b$, an extra lift bit remains. |
| same-denominator M1 alignment | Insert $q=0,p=-t,c=mb$. | **Pass exactly.** Phase and denominator carrier align; taper mass $R/2+O(1)$. |
| positive-numerator M2 alignment | Insert $q=0,p=-2j,c=(4m+1)b$. | **Pass exactly.** Phase and numerator-character product both equal $(-1)^j$; taper mass $R+O(1)$. |
| M2 sign-crossing convention | Replace $\chi_4(a')$ by $\operatorname {sgn}(a')\chi_4(|a'|)$, then test opposite signs. | **Pass algebraically; empty on the fixed top shell.** Dropping the sign reverses the control, while (131.H24)--(131.H25) exclude a top-size crossing. |
| resonant-window mass | Use coherence width $R^{-1}=W/D$ in $b$ and packet length $R=D/W$. | **No sparse-error saving.** Continuous phase-space mass is $D$; integer occupancy and actual signs remain a cross-ray problem. |
| thresholds, faces, stars, diagonal, owners | Zero-extend each half-open owner cell and charge all jumps in (131.H6); keep $n=0$ separate. | **Unpriced.** The selected placeholders name these data but do not supply their pullback or total variation. |
| scalar versus positive energy | Compare the physical scalar with (131.H31) and with full $G^2$ completion. | **Strict scope correction.** No equality or positive-order connector is available; energy saturation is not a scalar obstruction. |
| per-ray versus cross-ray capacity | Compare every proposal with (131.H29)--(131.H30). | **No cross-ray theorem.** The ideal per-ray floor is exactly $27/48$; strict improvement and the $24/48$ target require further actual-family gains. |
| complete Gauss/Salié identification | Check modulus, complete residue support, additive-integrality, inverse unit, and boundary completion for (131.H11). | **No-go from the supplied algebra.** All decisive hypotheses are missing. |
| global/M9 scope | Try to propagate any packet identity to a complete block, M9 component, endpoint, bridge, or quarter result. | **Forbidden and unsupported.** No such promotion follows. |

The controls are analytic/algebraic.  No numerical experiment was used.

## 6. Dependencies and exact artifacts used

This review used only the permitted Round-131 context:

1. `protocol.md`;
2. `state/proof_obligations.yml`, in particular the accepted top-shell
   chart, post-inner energy obstruction, complete (Y^{35/48}) ledger,
   and rejected same-denominator/positive-energy shortcuts;
3. `state/active_campaign.yml`;
4. `strategy/conductor_0823_full_proof_strategy.md`;
5. `rounds/codex-managed/gc-w7-16-top-shell-determinant-residue-zero-mode-gate/blind_statement.md`;
6. `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/reviews/hostile_determinant_residue_gram_addendum.md`; and
7. `rounds/codex-managed/gc-w7-16-post-inner-outer-bilinear-gate/synthesis.md`.

No sibling Round-131 report, computation, web source, or external theorem
was used.  The review was 100% analytical/algebraic.

## 7. Recommended state effect

**Retain with strict scope** the fixed-ray bounded-multiplicity chart,
the M1 carrier shifts (131.H12)--(131.H13), the conditional M2 unit-branch
shift (131.H15)--(131.H16), the aligned-packet calculations
(131.H17)--(131.H23), and the top-shell sign-crossing exclusion
(131.H24)--(131.H25).

**Revise or reject** any sentence asserting that the supplied data already
give a periodic/BV decomposition of the full physical weight, a universal
M2 mode modulo (4|a|), a complete Gauss/Salié sum, a sparse resonant
error, per-ray exact vanishing, or a family-level obstruction.  Also
reject every replacement of the scalar by (K_{B,+}^*K_{B,+}) or
(G^2) without the missing connector.

For this hostile seam, the terminal label is **`degenerate`**: the exact
carrier algebra exposes the correct shifted controls, but the first
physical separation identity and the required cross-ray theorem are not
present, while the aligned packets do not furnish an actual-family lower
bound.  Make no graph edit and no promotion of the (Y^{35/48}) block,
any global exponent, M9-M1, M9-M2, endpoint uniformity, M9, the
conditional bridge, or the quarter target.

## 1. Result: scoped radical-frequency no-go

The nonsquare radical dictionary and the product-incidence dictionary are both exact, but they do not by themselves close the target.  The rigorous result of this rederivation is the following scoped method obstruction.

For the literal coefficient in (161.BL5), a squarefree-radical channel has a (D)-dependent coefficient vector (B_D=(B_D(t))_t).  The canonical common-test decompositions (by rows, by (t)-columns, or by individual product incidences), together with the full available (ell^2), channel-(ell^1), collision, and projective-norm ledger, give only (L^{2+o(1)}).  On the (t=1), (D\asymp L^2) layer the radical-frequency test space is one-dimensional, so a large-sieve/Bessel argument has evaluation norm exactly the square root of the number of active radicals, independently of exact frequency separation.  Reaching (L^{3/2}X^\varepsilon) therefore requires a new signed estimate for the actual close-factor coefficient (or an exact cancellation-preserving decomposition with a strictly better proved norm).  Neither follows from (161.BL6)--(161.BL8).

This is not a counterexample to (161.BL4).  It is a no-go for promoting the proposed radical-frequency coupling from the stated inputs.  Exact resonance is harmless, while near resonance is not controlled by the multiplicity of exact resonance.

## 2. Exact statement and hypotheses

Assume exactly (161.BL1)--(161.BL8), including the zero extensions, the literal half-open height profile, the hard cone endpoints, the odd-(h) restriction, and arbitrary real (J=\sqrt X>0).  Write the fixed support assertion (n\asymp L^2) as

\[
 c_0L^2\le n\le C_0L^2
\]

with fixed positive constants; replacing this ambient interval by the smaller literal nonzero support only decreases all capacity bounds below.  For a squarefree (D>1), put

\[
 I_D=\{t\ge1:Dt^2\asymp L^2\text{ and }B_D(t)\ne0\}.
\]

Then the following claims hold.

1. Every nonsquare product has exactly one representation (n=Dt^2), (D>1) squarefree, and (161.BL3) is exactly
   \[
   \sum_{D>1\ {\rm sf}}\sum_{t\in I_D}B_D(t)e(tJ\sqrt D).
   \]
2. Literal pairs ((h,m)) in a fixed fibre (hm=Dt^2) are in bijection with the tuples displayed in Section 3.  The bijection retains every coprimality, parity, cone, profile, and endpoint condition.
3. At a fixed (J), at most one squarefree (D>1) can contain even one exactly phase-one entry.  If (J\sqrt D=p/q) in lowest terms, the exactly phase-one entries are precisely (t\in I_D\cap q\mathbb Z); the whole channel is phase one precisely when (q=1).  An exact modulo-one frequency class (J\sqrt D\pmod 1) has at most two distinct squarefree radicals.
4. These exact multiplicities imply no bound for near collisions at the natural resolution (1/|I_D|).  The relevant collision parameter is
   \(
   \|J(\sqrt{D_1}-\sqrt{D_2})\|
   \)
   on moving ranges of length (O(1+L/\sqrt D)).
5. All channels (D\le L) are target-safe by absolute summation, but this is not owner-complete.  The remaining short-channel range includes the (t=1) close-factor layer.  No strict polynomial (L)-range for the whole scalar follows from the stated estimates.

## 3. Proof and derivation

**Unique radical linearization and square ownership.**  For a positive integer (n), let (D=\operatorname{sf}(n)), the product of the primes occurring in (n) to odd exponent, and let (t=\sqrt{n/D}).  Then (D) is squarefree, (t\) is a positive integer, and uniqueness follows prime by prime.  Moreover (D=1) if and only if (n) is a square.  Thus the square removal deletes the entire (D=1) product fibre, not an (h=m) diagonal.  For example, (h=9,m=4) is an allowed-cone odd-(h) pair with square product (36), although (h\ne m).  For (D>1),

\[
 \sqrt n=t\sqrt D,
 \qquad
 L^{3/2}n^{-3/4}C_L(n)=B_D(t),
\]

so substituting into (161.BL6) proves the exact radical scalar.

**Incidence bijection.**  Given a literal pair ((h,m)), set

\[
 g=(h,m),\qquad A=h/g,\qquad M=m/g.
\]

Then ((A,M)=1).  There are unique squarefree (d_1,d_2) and unique positive (u,v) such that

\[
 A=d_1u^2,\qquad M=d_2v^2.
\]

Coprimality is equivalently

\[
 (d_1u,d_2v)=1.
\]

Consequently

\[
 D=d_1d_2,\qquad t=guv,\qquad
 h=gd_1u^2,\qquad m=gd_2v^2.                 \tag{3.1}
\]

Here (d_1,d_2) are squarefree, (d_1d_2=D>1), and hence ((d_1,d_2)=1).  Since (h) is odd, and only for that reason,

\[
 g,d_1,u\quad\hbox{are odd}.                \tag{3.2}
\]

There is no additional coprimality condition involving (g).  The integer cone is exactly

\[
 d_2v^2\le d_1u^2\le4d_2v^2,                \tag{3.3}
\]

because (m\le h) and (m\ge\lceil h/4\rceil) are equivalent to (m\le h\le4m).  Conversely, any tuple satisfying (3.1)--(3.3), ((d_1u,d_2v)=1), and the literal nonzero profile/support conditions produces an allowed pair, and its gcd is exactly (g).  Recovering (g,A,M) and then their squarefree kernels proves injectivity.  This is therefore a bijection.

The parity consequences are also exact.  If (D) is even, then (d_1) is odd and the prime (2) lies in (d_2); such channels are not removed.  If (D) is odd, then (d_2) is odd, while (v) may still be even.  Since (u) is odd,

\[
 \chi_4(h)=\chi_4(gd_1u^2)=\chi_4(gd_1).
\]

The literal contribution of a tuple to (B_{d_1d_2}(guv)) is

\[
 \begin{aligned}
 \beta(g,d_1,d_2,u,v)
  ={}&\frac{L^{3/2}\chi_4(gd_1)}
  {g^{3/2}(d_1d_2)^{3/4}(uv)^{3/2}}
  \eta_L(gd_1u^2)
  \Phi\!\left(\frac{gd_1u^2}{H+1}\right)\\
 &\times
 W\!\left(\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}}\right),              \tag{3.4}
 \end{aligned}
\]

and (B_D(t)) is the sum of (3.4) over all tuples with (d_1d_2=D) and (guv=t).  Formula (3.4) displays the obstruction to an automatic separated tensor: the height profiles depend on (gd_1u^2), the endpoint profile and cone depend on the ratio (d_1u^2/(d_2v^2)), the coprimality condition couples the two sides, and the maps to (D) and (t) use two different products.  Splitting (3.4) into individual incidences also splits the fibrewise (chi_4)-cancellation inside (C_L).

When (D=1), (3.1) instead forces (d_1=d_2=1) and leaves all coprime pairs (u,v) in the cone.  This verifies directly why the removed square fibre cannot be restored as an orthogonal diagonal.

**Exact phase-one channels and exact collisions.**  Put (\alpha_D=J\sqrt D).  An entry is phase one exactly when (t\alpha_D\in\mathbb Z).  Thus such an entry exists only if (\alpha_D\in\mathbb Q).  If (\alpha_D=p/q) in lowest terms, the exact entries are precisely the multiples of (q), with multiplicity

\[
 \#(I_D\cap q\mathbb Z)\le 1+O\!\left(\frac{L}{q\sqrt D}\right).
\]

If two distinct squarefree (D_1,D_2) both had rational (\alpha_D), then (\sqrt{D_1/D_2}\) would be rational.  Comparing prime valuations in a rational square forces (D_1=D_2), a contradiction.  Hence there is at most one such channel; its whole absolute mass is

\[
 \sum_t|B_D(t)|\ll_\varepsilon(1+L/\sqrt D)L^\varepsilon
 \ll_\varepsilon L^{1+\varepsilon},                         \tag{3.5}
\]

which is target-safe.  In particular, the whole channel is phase one only when (q=1), and there is at most one whole phase-one channel.

For completeness, an exact common frequency satisfies

\[
 J(\sqrt{D_1}-\sqrt{D_2})\in\mathbb Z.                       \tag{3.6}
\]

No exact congruence class can contain three distinct squarefree radicals.  Otherwise, for distinct (D_1,D_2,D_3), division of the two nonzero integers in (3.6) gives a nontrivial rational linear relation among (\sqrt{D_1},\sqrt{D_2},\sqrt{D_3}).  These three radicals are rationally independent: after isolating one radical and squaring, a putative three-term relation with all coefficients nonzero produces a nonzero rational multiple of (\sqrt{D_iD_j}), which is irrational because distinct squarefree (D_i,D_j) have nonsquare product; the cases with a zero coefficient reduce to the impossible rational ratio of two distinct squarefree radicals.  Thus exact collision classes have size at most two.  This statement is deliberately not extended to near collisions.

**Moving ranges and the near-collision ledger.**  The ambient (t)-range is

\[
 c_0^{1/2}\frac L{\sqrt D}\le t\le C_0^{1/2}\frac L{\sqrt D},
 \qquad |I_D|\ll1+\frac L{\sqrt D}.                           \tag{3.7}
\]

It is an annular, (D)-dependent interval, not a common initial interval.  On a common consecutive overlap of length (T), the pure exponential vectors have Gram entry

\[
 \left|\sum_{t=a}^{a+T-1}e\!\left(tJ(\sqrt{D_1}-\sqrt{D_2})\right)\right|
 \le \min\!\left(T,\frac1{2\|J(\sqrt{D_1}-\sqrt{D_2})\|}\right).       \tag{3.8}
\]

Thus the resolution is (1/T), with (T\asymp L/\sqrt K) on a dyadic radical scale (D\asymp K).  If (M) active frequencies lie in that scale and

\[
 A_K(T)=\max_\theta\#\{D:\|J\sqrt D-\theta\|\le c/T\},
\]

then a normalized Dirichlet-kernel test supported on (T) consecutive integers shows that the squared common-test evaluation norm is at least (c'A_K(T)T).  Pigeonholing (M) circle points into (O(T)) arcs already gives (A_K(T)\gg M/T).  At (K\asymp L^2), (T=O(1)), so a bounded-length test cannot resolve a set of up to (L^2) radical frequencies at all.

There is no uniform modulo-one separation supplied by the algebraic real-line spacing of square roots.  For any prescribed pair (D_1\ne D_2), choosing

\[
 J=\frac{k}{|\sqrt{D_1}-\sqrt{D_2}|}
\]

gives an exact collision, and (k) can be taken large enough to retain (L\ll H).  More strongly, for any finite set (\mathcal D) of (M) squarefree radicals and any integer (Q\ge2), the pigeonhole proof of simultaneous Dirichlet approximation gives an integer (1\le q\le Q^M) with

\[
 \max_{D\in\mathcal D}\|q\sqrt D\|\le Q^{-1}.                \tag{3.9}
\]

Indeed, two of the (Q^M+1) points (r(\sqrt D)_{D\in\mathcal D}\pmod1), (0\le r\le Q^M), lie in the same one of (Q^M) boxes.  Taking (J=q) makes (X=q^2), (q_X=1), and, along unbounded such denominators, eventually (L\ll H=\lfloor\sqrt q\rfloor).  Hence arbitrarily many fixed finite channels can be simultaneously near phase one while none is exactly phase one.  This qualitative capacity test is not a counterexample to the target: its denominator may be very large relative to (L), (X^\varepsilon) must still be priced, and the literal coefficients may cancel.  It does prove that exact multiplicity cannot be used as a near-resonance bound.

**Norm, common-test, and restored-power ledger.**  The map (n\leftrightarrow(D,t)) is bijective and (L^{3/2}n^{-3/4}\asymp1) on the support.  Therefore (161.BL7) gives

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L).                         \tag{3.10}
\]

There are (O(L^2)) possible entries, so direct Cauchy--Schwarz gives (L^2\log(2L)^{1/2}).  Summing (161.BL8) over (D\ll L^2) also gives (L^{2+o(1)}).  The target needs a genuine factor (L^{1/2-o(1)}).

The (D)-varying vectors cannot be inserted into a common-coefficient large sieve.  To make that step literal one must first prove

\[
 B_D(t)=\sum_r u_r(D)c_r(t)                                  \tag{3.11}
\]

before taking absolute values.  If (P=\inf\sum_r\|u_r\|_2\|c_r\|_2) is the corresponding Hilbert-projective (nuclear) norm and (\Lambda) is the squared common-test evaluation norm at the frequencies (\alpha_D), then the fully priced consequence is only

\[
 |S|\le \Lambda^{1/2}P.                                      \tag{3.12}
\]

For (M) frequency rows, (\Lambda\ge M): a common coefficient supported at one (t) evaluates with modulus one at every row.  Collision clusters can make it larger, not smaller.

The always-valid column decomposition makes this loss explicit.  Let

\[
 M_t=\#\{D>1\ {\rm sf}:Dt^2\asymp L^2\},\qquad
 E_t^2=\sum_D|B_D(t)|^2.
\]

Then (M_t\ll1+L^2/t^2), (t\ll L), and

\[
 \begin{aligned}
 |\mathcal T_L^{\rm ns}|
 &\le\sum_t\sqrt{M_t}\,E_t\\
 &\le\left(\sum_tM_t\right)^{1/2}
       \left(\sum_tE_t^2\right)^{1/2}
 \ll L^2\log(2L)^{1/2}.                                     \tag{3.13}
 \end{aligned}
\]

This is the exact Bessel price of the canonical projective tensor.  Decomposing into the incidence atoms (3.4) instead takes absolute values before the fibrewise character cancellation and returns the (L^{2+o(1)}) positive capacity.

The terminal obstruction is already visible at (t=1).  Here (g=u=v=1), so the literal layer is

\[
 \begin{aligned}
 S_1={}&L^{3/2}
 \sum_{\substack{d_1,d_2\ {\rm sf},\ (d_1,d_2)=1\\
 d_1d_2\asymp L^2,\ d_2\le d_1\le4d_2,\ d_1\ {\rm odd}}}
 (d_1d_2)^{-3/4}\chi_4(d_1)\eta_L(d_1)
 \Phi\!\left(\frac{d_1}{H+1}\right)\\
 &\hspace{22mm}\times
 W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
 e\!\left(J\sqrt{d_1d_2}\right).                            \tag{3.14}
 \end{aligned}
\]

This includes even (D=d_1d_2), for which the factor (2) belongs to (d_2).  It is a close-factor squarefree-product sum, not a radical-channel polynomial of positive length.  If (M_1) radicals are active, the common-test space is one-dimensional, its evaluation norm is exactly (\sqrt{M_1}), and the projective norm of the one-column coefficient matrix is exactly

\[
 \left(\sum_D|B_D(1)|^2\right)^{1/2}.
\]

The stated control bounds their product only by (L^{2+o(1)}).  Frequency separation cannot improve a one-coordinate evaluation.

This limitation is logical as well as numerical.  On (M\asymp L^2) formal (t=1) rows, choose real numbers (b_D=\cos(2\pi J\sqrt D)) if their squared cosines have total at least (M/2), and otherwise choose (b_D=\sin(2\pi J\sqrt D)).  Then (|b_D|\le1), the analogues of (161.BL7)--(161.BL8) hold, but

\[
 \left|\sum_D b_De(J\sqrt D)\right|\ge M/2.
\]

Thus support, reality, the (ell^2) control, and the channel-(ell^1) control cannot imply the target.  The actual incidence and (chi_4) structure must supply the missing cancellation; (3.14) is precisely that unsolved obligation.

Finally, the genuinely long small-radical range is harmless without any phase argument:

\[
 \sum_{D\le L}\sum_t|B_D(t)|
 \ll_\varepsilon
 \left(L+L\sum_{D\le L}D^{-1/2}\right)L^\varepsilon
 \ll_\varepsilon L^{3/2+\varepsilon}.                         \tag{3.15}
\]

The obstruction is therefore not a small-(D) exact channel but the owner-incomplete intermediate/large-(D) short-channel range, beginning with (3.14).  The residual (L^{1/2}) cannot be hidden in (X^\varepsilon) on any fixed polynomial relation (L=X^\theta), (\theta>0), uniformly for every (\varepsilon>0).

## 4. First doubtful or unproved step

The first unproved step in a target proof is the replacement of the actual family (B_D(t)) by a common coefficient test, or equivalently the assertion that (3.11) has a cancellation-preserving projective norm and collision constant strong enough to save (L^{1/2-o(1)}).  Equality (3.4) is not such a separation, and its atomic projective pricing destroys the character cancellation.

The failure is already exact on the one-column restriction (3.14).  A proof must establish, uniformly for arbitrary real (J) and with all hard profiles retained,

\[
 S_1\ll_\varepsilon L^{3/2}X^\varepsilon,                    \tag{4.1}
\]

by exploiting the signed close-factor structure, or must prove a stronger norm estimate such as

\[
 \left(\sum_{D\asymp L^2}|B_D(1)|^2\right)^{1/2}
 \ll_\varepsilon L^{1/2}X^\varepsilon
\]

(or an equally strong alignment-sensitive substitute).  Neither estimate is present, and a (t)-frequency large sieve cannot prove it because (t) is fixed.  Any bilinear theorem proposed for (3.14) would be genuinely new input and would have to audit its hard endpoints, squarefree and coprimality restrictions, even-(D) branch, (\chi_4) placement, arbitrary-(J) uniformity, and restored powers.

## 5. Required control tests and outcomes

| Control | Outcome |
|---|---|
| `literal_product_fibre_and_square_owner` | **Pass.**  (D=\operatorname{sf}(hm)) owns the full product fibre; (D=1) contains off-diagonal pairs such as ((9,4)) and stays removed. |
| `unique_radical_linearization` | **Pass.**  Prime valuations give the unique (n=Dt^2), and the phase becomes (e(tJ\sqrt D)) exactly. |
| `actual_coefficient_incidence` | **Pass.**  Equations (3.1)--(3.4) give a bijection and the literal coefficient, with no invented condition on (g). |
| `fixed_center_exact_resonance` | **Pass.**  At most one (D) has any exact phase-one entries; their multiples-of-(q) count and target-safe mass are explicit.  Exact common-frequency classes have size at most two. |
| `near_resonance_mod_one_collisions` | **Obstruction.**  Resolution is (1/T_D); exact multiplicity supplies no local-density bound.  Equations (3.8)--(3.9) exhibit the collision capacity. |
| `small_D_long_channels` | **Pass/target-safe.**  The complete range (D\le L) satisfies (3.15) absolutely. |
| `t1_large_D_singleton_layer` | **Obstruction.**  Formula (3.14) is literal; its one-dimensional test space returns the full (L^{2+o(1)}) Bessel capacity. |
| `coefficient_varying_large_sieve_applicability` | **Fail as a target step.**  The (B_D(t)) are not common coefficients.  Applying a common-coefficient theorem before proving (3.11) is invalid. |
| `projective_tensor_bessel_price` | **Fail as a target step.**  The exact canonical price is (3.13); on (t=1) it is (\sqrt{M_1}\|B_\bullet(1)\|_2). |
| `hard_profiles_parity_endpoints` | **Pass.**  (q_X,H,eta_L,Phi,W), zero extension, both cone equalities, odd (g,d_1,u), and the surviving even-(D) branch are retained. |
| `missing_L_half_power` | **Unclosed.**  Both stated norm routes stop at (L^{2+o(1)}), leaving exactly (L^{1/2-o(1)}) signed gain to prove. |
| `hard_top_owner_and_downstream_scope` | **Pass.**  Every conclusion is restricted to this one nonsquare polynomial intermediate hard-TOP scalar; no square fibre or downstream claim is restored. |

No numerical experiment was used; all controls are algebraic or analytic.

## 6. Dependencies and exact artifacts used

Only the following artifacts were read or used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/blind_statement.md`.
3. `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/briefs/blind_radical_frequency_rederivation.md`.

No state file, strategy file, conductor seed, sibling report, historical-round artifact, external source, web result, or computation was used.  The geometric-sum bound, the three-radical independence argument, and simultaneous approximation (3.9) were derived in the report.

## 7. Recommended state effect

Retain the radical and incidence dictionaries, the exact-resonance multiplicity, the small-(D) target-safe subrange, and the (t=1) projective/Bessel obstruction as candidate evidence.  Do not promote (161.BL4), do not claim an owner-complete strict polynomial range, and reject any application of a common-coefficient large sieve that does not first prove and fully price a literal decomposition of (B_D(t)).  The next admissible proof input would have to solve the signed close-factor estimate (4.1) or provide an equivalent cancellation-preserving norm theorem.  No conclusion transfers beyond the stated scalar.

Close label: `hard_top_radical_frequency_coupling_no_go`

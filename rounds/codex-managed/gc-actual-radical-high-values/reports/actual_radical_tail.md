# Actual radical tail: repeated classes paid, distinct-class correlation open

Campaign: gc-actual-radical-high-values. Round: 216.
Task: actual_radical_tail. Role: discovery; NONBLIND candidate evidence.
Generated: 2026-09-28T01:59:19+08:00.
Starting graph SHA-256:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.
Effort: 100 percent analytical/algebraic; zero experiments; no new source import.

## 1. Result: complete delimitation, not a high-value gain

The frozen actual high-value gate H216 remains unproved. A signed
regrouping does pay all configurations with a repeated squarefree class
collectively, including nonpairing relations, every harmonic, and all
unequal scales. It does not pay the twelve-distinct-class correlation.

For the exact class waves

\[
 f_d(R)=\sum_{s\ge1}a_{ds^2}(T)\cos(2\pi R s\sqrt d-3\pi/4),
 \qquad Z_Q=\sum_{d>Q}^{\rm sf}f_d,
\]

define the ordered signed polynomial

\[
 E_{12}(R)=
 \sum_{\substack{d_1,\ldots,d_{12}>Q\ {\rm sf}\\d_i\ne d_j\ (i\ne j)}}
                         \prod_{i=1}^{12}f_{d_i}(R).
\]

At \(Q=\lfloor T^{2/5}\rfloor\), the proved collective estimate is

\[
 \int w(R/T)|Z_Q(R)^{12}-E_{12}(R)|\,dR
 \ll_\epsilon T^{4/5+\epsilon}
                  +T^{8\beta-1/5+\epsilon},                 \tag{1}
\]

where \(\beta=2\theta_{LY}-1/2\). The accepted
\(1/8<\beta<27/208\) gives \(8\beta-1/5<109/130<29/25\).
This is a signed regrouping estimate, not a bound on the termwise
absolute twelve-frequency expansion.

With the completely paid head and low values below, H216 is equivalent
to the real signed upper bound

\[
 \mathcal C_{12}^{\rm distinct}(T):=
 \int w(R/T)E_{12}(R)\,dR
                  \le C_\epsilon T^{29/25+\epsilon}.         \tag{2}
\]

An upper bound suffices. At this target scale it is also equivalent to
an absolute bound, because (1) and \(M_{12}(Z_Q)\ge0\) give a smaller
negative lower bound for this real integral. Every frequency in (2) is
nonzero by squarefree radical independence, but its complete signed
estimate remains open. The strongest complete upper power obtained here
is still \(10\beta\). The new identity and its paid error are a rigorous
delimitation, not a gain in the complete moment or pointwise frontier.

## 2. Exact statement and hypotheses

Let \(T\ge2\) be real. Fix exactly the nonnegative real radial
unit-mass smooth mollifier supported in the unit disk from the strategy.
Its transform \(\Psi\) is real, even and Schwartz, with \(|\Psi|\le1\).
Let \(w\ge0\) be the prescribed smooth function supported in
\([1/2,2]\), equal to one on \([1/\sqrt2,\sqrt3]\). Set

\[
 a_n(T)=r_2(n)n^{-3/4}\Psi(\sqrt{n/T}),\qquad
 B_T(R)=\sum_{n\ge1}a_n(T)\cos(2\pi R\sqrt n-3\pi/4),
 \qquad V_0=T^{13/125}.
\]

The decomposition \(B_T=L_Q+Z_Q\) includes every \(s\ge1\) in
each class, where \(L_Q=\sum_{d\le Q}^{\rm sf}f_d\). No phase or
coefficient is changed. All series are absolutely convergent for each
fixed \(T\). Write

\[
 M_p(F)=\int w(R/T)|F(R)|^p\,dR,\qquad
 D_F(V)=\int w(R/T)1_{|F(R)|>V}\,dR.
\]

Only the accepted204 kernel's unweighted exponent-pair specialization
and the repaired final Li--Yang application are reused; none of their
qualifications is strengthened. The conductor supplied the sharper head
and masked-distribution observation during the task. It is independently
reproduced below and explicitly nonblind. The finite class identity
requires no external theorem.

## 3. Proof and complete power derivation

### A. Actual head and the masked distribution

The actual divisor identity proves, prime by prime, that for squarefree
\(d\)

\[
 r_2(ds^2)\le r_2(d)\tau(s^2).                               \tag{3}
\]

If \(d\) contains a prime congruent to three modulo four both sides
are zero. For a prime congruent to one modulo four of exponent \(e\)
in \(s\), the ratio of the local factors is \(2e+1\) if that prime
does not divide \(d\), and \(e+1\le2e+1\) if it does. The prime two
does not increase the ratio. These cases prove (3).

Since \(\tau(s^2)\le\tau_3(s)\),
\(\sum_s\tau(s^2)s^{-3/2}\le\zeta(3/2)^3\). Elementary lattice
counting in the enclosing square gives
\(\sum_{d\le x}r_2(d)\ll x\) for \(x\ge1\). Partial summation gives

\[
 \|L_Q\|_\infty
 \le C\sum_{d\le Q}^{\rm sf}r_2(d)d^{-3/4}
 \ll Q^{1/4}\ll T^{1/10}=o(V_0).                            \tag{4}
\]

There is no \(T^\epsilon\) loss or unaccounted harmonic sum in (4).
It follows that \(\|L_Q\|_\infty\le V_0/2\) for all sufficiently
large \(T\); fixed bounded \(T\) is covered by constants.

To reproduce the masked version of accepted204, truncate at
\(U=T^{3/2}\), with coefficient tail \(O_K(T^{-K})\) for any fixed
\(K\). Partition the retained indices into the singleton and
\(O(\log T)\) ambient dyadic intervals. Multiply each actual coefficient
by either squarefree mask. In a block this preserves

\[
 \sum |a_n\,1_{\rm mask}|^2\ll_\eta N^{-1/2+2\eta}
                              \ll_\eta T^{3\eta}N^{-1/2}.
\]

The proof's unweighted kernel, both signs, full Gram diagonal, and
covering argument are unchanged. Its local length has the full ceiling
\(1+T/h\), including one interval when \(h>T\). The finite duality
therefore gives the same block distribution. Union over the finite
blocks at level \(V/(C\log T)\), absorbing logarithms and the uniformly
small Schwartz tail, yields

\[
 D_F(V)\ll_\epsilon T^\epsilon(V^{-2}+TV^{-q}),
 \quad q=136/13,\quad V\ge1,\quad F=L_Q,Z_Q.                 \tag{5}
\]

This reapplies the finite proof; it does not assume that the printed
lower-index-cutoff theorem automatically covers every mask. For bounded
\(T\), the fixed Schwartz and divisor bounds supply the adjustment.

Layer cake using (4)--(5), with trivial measure \(O(T)\) below one,
gives

\[
 M_{12}(L_Q)\ll_\epsilon
 T^\epsilon\{T+Q^{5/2}+TQ^{5/13}\}
 \ll_\epsilon T^{15/13+\epsilon}.                          \tag{6}
\]

Here \(12-q=20/13\) and \(29/25-15/13=2/325>0\).
The accepted actual bound for \(B_T\) and (4), rather than a new
pointwise theorem for arbitrary masks, give

\[
 \sup_{R\in[T/2,2T]}|Z_Q(R)|\ll_\epsilon T^{\beta+\epsilon}.
\]

Put \(W\ll T^{\beta+\eta}\) for this ceiling. For fixed \(p>2\),
layer cake in (5) yields

\[
 M_p(Z_Q)\ll T^{1+\epsilon}
       +T^\epsilon W^{p-2}
       +T^{1+\epsilon}\int_1^W V^{p-1-q}\,dV.
\]

For \(p<q\) the last integral is bounded, for \(p=q\) it is
logarithmic, and for \(p>q\) its upper power is dominated by
\(W^{p-2}\), since the accepted \(\beta(q-2)>1\).
At \(p=2\) only an additional logarithm appears. Choosing the input
losses sufficiently small proves

\[
 M_p(Z_Q)\ll_{p,\epsilon}T^{1+\epsilon}
                         +T^{(p-2)\beta+\epsilon}
 \qquad(p\ge2\text{ fixed}).                               \tag{7}
\]

In particular this proves every lower moment used below, including
\(p=10<q\). The cases \(p=0,1\) needed for polynomial bookkeeping
are bounded by \(T^{1+\epsilon}\), the latter by Cauchy and \(M_2\).

### B. Both directions of the high-event and full-moment transfer

For the eventual threshold in (4),

\[
 \{|B_T|>V_0\}\subseteq\{|Z_Q|>V_0/2\},\qquad
 |B_T|\le2|Z_Q|\text{ on the former event}.                 \tag{8}
\]

Conversely \(|Z_Q|>2V_0\) implies \(|B_T|>V_0\) and
\(|Z_Q|\le(4/3)|B_T|\). The intervening fixed-factor threshold strip
costs, by (5), at most

\[
 T^\epsilon\{V_0^{10}+TV_0^{20/13}\}
       =T^{26/25+\epsilon}+T^{29/25+\epsilon}.              \tag{9}
\]

The low-value integral \(\int_{|F|\le V_0}w|F|^{12}\) for \(F=B_T\)
or \(Z_Q\) is bounded by the same powers plus \(T\): integrate
the distribution from one to \(V_0\), and use \(O(T)\) below one.
An upper bound by the truncated layer-cake integral is sufficient even
though it also counts part of the higher values.

Consequently H216 is equivalent to the complete target for \(B_T\).
By (6) and \(|x+y|^{12}\le2^{11}(|x|^{12}+|y|^{12})\), the latter
target is equivalent in both directions to the complete target for
\(Z_Q\):

\[
 {\rm H216}\quad\Longleftrightarrow\quad
 M_{12}(B_T)\ll_\epsilon T^{29/25+\epsilon}
 \quad\Longleftrightarrow\quad
 M_{12}(Z_Q)\ll_\epsilon T^{29/25+\epsilon}.                \tag{10}
\]

No mixed moment was deleted to make this transfer. The strict power gap
in (6) absorbs its adjustable epsilon. This is also why a smooth
complete moment may be used in place of the nonsmooth high-event mask.

### C. Uniform class bounds and the signed distinct-class identity

Let \(A_d=\sum_s|a_{ds^2}(T)|\). Uniformly in \(T\), the divisor
envelope and the convergent harmonic sum imply, for small \(\eta>0\),

\[
 A_d\ll_\eta d^{-3/4+\eta},\qquad
 \sum_{d>Q}^{\rm sf}A_d^h
       \ll_{h,\eta}Q^{1-3h/4+h\eta}\quad(2\le h\le12).      \tag{11}
\]

For the first inequality use
\(r_2(ds^2)\le4\tau(d)\tau(s^2)\) and \(|\Psi|\le1\).
The second is a convergent power sum in \(d\).
For each fixed \(T\), Schwartz decay additionally gives
\(\sum_d A_d<\infty\).

Define \(p_h(R)=\sum_{d>Q}^{\rm sf}f_d(R)^h\); thus \(p_1=Z_Q\).
Equation (11) gives

\[
 |p_h(R)|\ll_{h,\epsilon}Q^{1-3h/4+\epsilon}
                         \le C_{h,\epsilon}Q^{-h/4+\epsilon}
 \qquad(2\le h\le12).                                     \tag{12}
\]

For finite real variables \(x_d\), the exact partition identity is

\[
 \sum_{d_1,\ldots,d_k\ {\rm distinct}}\prod_i x_{d_i}
 =\sum_{\pi\in\Pi_k}\prod_{B\in\pi}
       \left((-1)^{|B|-1}(|B|-1)!\sum_d x_d^{|B|}\right).
                                                               \tag{13}
\]

To prove it, compare the coefficient of \(t^k\) in
\(\prod_d(1+t x_d)=
 \exp(\sum_{h\ge1}(-1)^{h-1}p_h t^h/h)\) and multiply by \(k!\).
This is formal polynomial algebra at degree \(k\); it assumes neither
an analytic logarithm nor positivity. It is also Möbius inversion on
set partitions.

Apply (13) with \(k=12\) and \(x_d=f_d(R)\).
The all-singleton partition contributes \(Z_Q^{12}\). Every other
partition has \(r\le10\) singleton blocks and some \(b\) blocks of
size at least two, whose total size is \(12-r\). Its exact bound from
(12)'s first inequality is

\[
 C_\epsilon |Z_Q|^r
          Q^{\,b-3(12-r)/4+\epsilon},\qquad
 b\le\lfloor(12-r)/2\rfloor.                               \tag{14}
\]

In particular it is at most
\(C_\epsilon Q^{-(12-r)/4+\epsilon}|Z_Q|^r\). There are finitely
many partitions. Distribute epsilon among their finitely many factors
and sum to obtain

\[
 \begin{split}
 |Z_Q^{12}-E_{12}|
 &\ll_\epsilon\sum_{r=0}^{10}
             Q^{-(12-r)/4+\epsilon}|Z_Q|^r\\
 &\ll_\epsilon Q^{-1/2+\epsilon}
                          (|Z_Q|+Q^{-1/4})^{10}.           \tag{15}
 \end{split}
\]

The binomial on the last line contains all the preceding monomials
with positive coefficients after factoring \(Q^{-1/2}\).
No individual original repeated-class frequency tuple is bounded in
modulus in this step. The cancellation is exact algebra among the
signed class waves.

All passages to infinite series are justified as follows. Truncate the
set of \(d\), apply the polynomial identity, and then let this set
increase. The majorant \(\sum_d A_d<\infty\) gives uniform absolute
convergence in \(R\) of each \(p_h\), \(Z_Q\), and the ordered
distinct-class product sum. Their finite-degree products converge
uniformly as well. The fixed finite-radius integration therefore
commutes with the limit. Infinite \(s\)-sums were already retained
inside each absolutely convergent \(f_d\). The uniform bound (11)
then applies to the limiting functions. There is no hidden finite
harmonic cutoff in (13)--(15).

Integrate (15) and use the explicitly derived tenth moment (7):

\[
 \begin{split}
 \int w|Z_Q^{12}-E_{12}|
 &\ll_\epsilon Q^{-1/2+\epsilon}(T+T^{8\beta})
                      +TQ^{-3+\epsilon}\\
 &\ll_\epsilon T^{4/5+\epsilon}
                       +T^{8\beta-1/5+\epsilon}.          \tag{16}
 \end{split}
\]

The floor causes only constants:
\(T^{2/5}/2\le Q\le T^{2/5}\) for every \(T\ge2\).
For an explicit ledger for every lower-order partition, the coarser
version of (14) and (7) give exponents

\[
 e_r=1-\frac{12-r}{10},\qquad
 e'_r=(r-2)\beta-\frac{12-r}{10}
          \quad(2\le r\le10).                             \tag{17}
\]

For \(r=0,1\) only \(e_r\) is needed.
Both expressions increase with \(r\); their maxima are \(4/5\)
and \(8\beta-1/5\), respectively, at \(r=10\). The exact exponent
in (14) is even smaller when \(12-r\) is odd or \(b\) is not
maximal. This accounts for every block size, not only pair partitions.
The \(r=10,b=1\) term is the familiar \(66p_2 Z_Q^{10}\);
retaining it explains the largest error scale.

### D. Remaining nonzero correlation and algebraic-separation failure

For context, the accepted exact-resonance kernel applied to (11) gives

\[
 S_Q=\sum_{d>Q}^{\rm sf}A_d^2\ll_\epsilon Q^{-1/2+\epsilon},
 \qquad
 0\le D_{12}(Z_Q)\ll_\epsilon TQ^{-3+\epsilon}
                         \ll_\epsilon T^{-1/5+\epsilon}.   \tag{18}
\]

It includes all nonpairing relations and sign imbalances within repeated
classes. Individual terms need not be positive. Its nonnegativity is
the even torus constant-coefficient fact, not finite-radius independence.

With \(\widehat w(\xi)=\int w(u)e(-u\xi)\,du\), absolute convergence
gives the exact remaining expression

\[
 \mathcal C_{12}^{\rm distinct}(T)=\frac{T}{2^{12}}
 \sum_{\varepsilon\in\{-1,1\}^{12}}
 \sum_{\substack{d_1,\ldots,d_{12}>Q\ {\rm sf}\\d_i\ne d_j}}
 \sum_{s_1,\ldots,s_{12}\ge1}
 e\!\left(-\frac38\sum_i\varepsilon_i\right)
 \prod_i a_{d_i s_i^2}(T)\,
 \widehat w\!\left(-T\sum_i\varepsilon_i s_i\sqrt{d_i}\right).
                                                               \tag{19}
\]

The actual displacement of the positive-radius window remains in this
transform. No translation to a centered window, absolute transform
majorant, phase choice, or torus independence is substituted. Every
radical difference is nonzero because the twelve squarefree classes
are distinct. Pairing a sign vector with its negative makes the total
real, without making any selected sector nonnegative.

The failure of exact independence to supply quantitative orthogonality
can be priced completely. Truncate only at \(U=T^{3/2}\).
The coefficient tail is \(O_K(T^{-K})\), while the full coefficient
mass is \(O_\epsilon(T^{1/4+\epsilon})\). Thus every twelvefold term
containing a tail index contributes in absolute value at most
\(O_\epsilon(T^{15/4+\epsilon-K})\) after integration.
Taking fixed \(K\) sufficiently large pays all such terms, including
unequal scales.

For a retained tuple put \(x_i=s_i\sqrt{d_i}\le\sqrt U\).
The product of the \(2^{11}\) expressions
\(x_1+\delta_2x_2+\cdots+\delta_{12}x_{12}\),
\(\delta_i=\pm1\), is a nonzero integer. Its polynomial is invariant
under changing any \(x_i\)'s sign (for \(x_1\), use the even number
of factors), hence is an integer polynomial in \(x_i^2=d_i s_i^2\).
None of its factors vanishes by radical independence. Each factor
has modulus at most \(12\sqrt U\), so this argument supplies only

\[
 |\Delta|\ge(12\sqrt U)^{-2047},\qquad
 T|\Delta|\ge12^{-2047}T^{-6137/4}.                         \tag{20}
\]

The lower bound tends to zero and gives no uniform decay of
\(\widehat w(-T\Delta)\) in the required range. This does not say
that actual tuples attain the bound. It identifies the precise failed
premise of the inference from nonzero radicals to effective
orthogonality. The lower restriction \(d>Q\) provides no improvement
within this algebraic argument.

By (10) and (16), an upper estimate (2) proves H216, and H216 conversely
implies (2). More explicitly,

\[
 -O_\epsilon(T^{4/5+\epsilon}+T^{8\beta-1/5+\epsilon})
 \le\mathcal C_{12}^{\rm distinct}(T)
 \le M_{12}(Z_Q)+
             O_\epsilon(T^{4/5+\epsilon}+T^{8\beta-1/5+\epsilon}).
                                                               \tag{21}
\]

Thus an upper bound is enough, while an absolute bound at exponent
\(29/25\) is equivalent because the negative side is already smaller.
The inherited \(M_{12}\) bound still yields only
\(\mathcal C_{12}^{\rm distinct}\ll_\epsilon T^{10\beta+\epsilon}\).
No improvement of this complete power follows from the separation.

Finally, both inherited high-level costs must remain visible.
Integrating (5) from a constant multiple of \(V_0\) to
\(W\ll T^{\beta+\epsilon}\) produces \(W^{10}\) and \(TW^{20/13}\).
Their exponents \(10\beta\) and \(1+20\beta/13\) both exceed \(29/25\).
Against the sufficient envelope \(T^{29/25}V^{-12}\),
the \(V^{-2}\) term is cheap only for \(V\le T^{29/250}\);
the \(TV^{-136/13}\) term only for \(V\le T^{13/125}\).
Deleting the former term alone would still fail H216. These are
diagnostics of upper bounds, not lower bounds on actual high values.

## 4. First doubtful or unproved step

The first unproved step is the complete signed estimate (2), with its
literal expression (19). The lower moments pay every repeated-class
configuration collectively, but do not control this remaining actual
twelve-distinct-class correlation. Exact radical independence fails to
give an effective finite-window estimate at (20). Declaring these
phases independent would simply erase the entire unproved input.

There is a separate regularity seam: replacing \(w(R/T)\) by
\(w(R/T)1_{|Z_Q|>V_0/2}\) does not preserve its Schwartz Fourier
decay. No smoothness of that event mask is known. Equivalence (10),
with all low values and the head paid, avoids this invalid replacement.

The conductor described a separate actual near-relation control during
this task. It is not needed as an unreviewed premise here, and no
isolated near-relation is turned into a moment lower bound.
This report proves a useful structural error estimate and leaves the
complete gate open. A new exact representation with its main term
unestimated is not counted as an arithmetic gain.

## 5. Required controls and outcomes

- Actual coefficients: (3) is checked from the representation-count
  identity; every class wave retains the original \(r_2(ds^2)\),
  transform, and cosine. No adversarial array substitutes for it.
- Absolute radius anchor: (19) keeps the original
  \(\widehat w(-T\Delta)\). No translation-invariant Gram substitute
  or freely modulated coefficient vector is used.
- All cosine signs: (19) includes all \(2^{12}\) signs and the exact
  coefficient \(2^{-12}e(-3\sum\varepsilon_i/8)\).
- Squarefree exact/nonzero distinction: (18) concerns only exact
  frequency; (19) has only nonzero frequencies, whose quantitative
  separation is not established by (20).
- Class one and nonpairing: \(d=1\) belongs to the paid head for
  every \(T\ge2\). All repeated-class nonpairing relations and all
  nonsingleton partition sizes remain in (13)--(18).
- Every harmonic and integer cutoff: all \(s\ge1\) are retained.
  The explicit \(Q\asymp T^{2/5}\) bounds pay the floor.
- Threshold constants: (8), its converse, (9), and (10) pay both
  event inclusion and integrand; a full moment is used only after
  proving equivalence.
- All blocks and tails: no favorable block is selected. Every
  infinite-series passage in (13)--(19) is justified. The sole
  truncation for the unsuccessful separation test has its full
  twelvefold tail cost restored.
- Signed certificate distinction: (16) estimates the repeated-class
  sum after exact signed regrouping. It does not bound the positive
  termwise Fourier certificate or lower-bound the actual moment.
- Source hypotheses: no new theorem or webpage is imported.
  Accepted204's finite proof is reapplied with its energy, correlation,
  and complete ceiling hypotheses. Li--Yang is used only as the
  repaired final pointwise estimate. The inherited thin-box and
  random-model exceptional-set gaps remain unrepaired.
- Real endpoints: all arguments hold for real \(T\), its exact
  integer \(Q\), and the prescribed smooth window. Bounded \(T\)
  is covered by uniform absolute convergence.
- Restored powers: head \(15/13\), repeated-class errors \(4/5\)
  and \(8\beta-1/5\), exact mass \(-1/5\), every lower partition
  exponent (14), (17), and both high-level deficits are explicit.
- Full-quarter and p-family scope: this argument uses the already
  accepted lower moments up to ten and addresses the fixed twelfth
  gate. It proves no improved family along unbounded fixed \(p\),
  and none with \(p\) growing with \(T\). Even proving (2) gives
  only \(102/325\), not quarter, M1/M2, GAR, or their endpoints.
- Statement-only control: this report is NONBLIND, and claims no
  independent validation. The finite identity (13), infinite passage,
  masked distribution, lower moments and full power ledger are
  explicit seams. No sibling report or isolated blind packet was read.

## 6. Dependencies and exact artifacts used

Read the assigned brief and only the permitted context:

- protocol.md.
- state/proof_obligations.yml, including the accepted exact-resonance,
  complete-distribution and repaired Li--Yang nodes and open
  GC-target/M1/M2 statuses. Its raw hash matches the frozen SHA-256.
- state/active_campaign.yml, round 216.
- strategy/round216_actual_radical_high_values.md.
- strategy/gauss_circle_strategy_checkpoint_round214_2026-09-28.md.
- rounds/codex-managed/gc-complete-localized-wave-moment/synthesis.md.
- proofs/kernels/gc_complete_square_root_large_values_moment_bound.md.
- rounds/codex-managed/gc-complete-signed-tenth-moment/reports/actual_tenth_high_values.md.
- rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md.
- proofs/kernels/gc_weighted_square_root_exact_resonance_mass.md.

The conductor's in-round messages supplied the sharper head observation,
asked for focus on signed correlations, described a separate actual
near-relation control, and requested complete identity and power seams.
The head and masked lower moments were independently checked above.
The separate near-relation control is not assumed. No historical source
named inside the permitted files was followed or separately read.
No numerical computation was used as mathematical evidence.

## 7. Recommended state effect

No change to the accepted complete moment power, pointwise benchmark,
or open H216/full-quarter obligations. Retain the finite signed identity
and collective error estimate (13)--(17) as candidate structural
evidence for independent validation; the conductor owns any graph
decision after that validation. Do not promote H216 from its paid head,
exact mass, repeated-class error, or distinct-class reformulation.

The complete actual signed estimate (19) remains open, and both
inherited high-level costs remain too large. This assigned report is
the only file written. Stop this task here; no shared-state, synthesis,
sibling, successor work, or additional mechanism is started.

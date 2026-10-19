# Round234 nonauthor actual-certificate review

Campaign: `gc-connected-cumulant-test`. Task: `certificate_review`.
Role: nonauthor lower-certificate and subtraction-scope reviewer.
Generated: 2026-10-12 Asia/Shanghai. Status: frozen review evidence.
Reviewed candidate SHA256:
`3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97`.
Starting graph SHA256:
`dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`.

## 1. Result and verdict

**PASS** for the assigned candidate Sections3A,3B,3D(C9-C10), and C2,
including the actual full-harmonic lower-certificate premise. The exact
permitted inherited Gram proof is valid once supplied with the squarefree
interval-mass lemma, and that lemma is proved by the permitted conductor
artifact's Section3A. The current certificate analyst's rederivation is
also sound, including its alternate harmonic-coherence proof.

The reviewed conclusions are, for the actual functions and sufficiently
large real T,

    C_harm = TW sum_d^* |m_[12](d)| >= c0 T^(5/2),
    TW sum_d^* |kappa12(d)-m_[12](d)| <<_epsilon T^(9/4+epsilon),
    C_conn = TW sum_d^* |kappa12(d)| >= c T^(5/2).

The final assertion refutes only the proposed tuplewise absolute connected
certificate at exponent29/25. It supplies no positive lower bound on signed
K12, signed I12 or any physical twelfth moment. No candidate edit is required
for this seam. The lower bound is understood with its explicitly proved
eventual-T quantifier, not as a positive bound on every bounded T window.

## 2. Exact statement and hypothesis matching

The candidate fixes the actual coefficients

    a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1) a_(ds^2)(T)cos(2pi R s sqrt(d)-3pi/4),

where d is squarefree, Psi is the real even Schwartz Fourier transform of
the fixed nonnegative radial smooth unit-mass mollifier, and |Psi|<=1,
Psi(0)=1. The smooth nonnegative radius window w is fixed, supported in
[1/2,2], with W=integral w>0. These imply every hypothesis of the inherited
Gram proof: continuity and a positive fundamental coefficient on a fixed
small interval; the uniform full-harmonic coefficient bound; summable
harmonic majorant; divisor growth; and positive mass in any fixed positive
squarefree shell, proved below. A stronger property such as positivity of
all higher Psi coefficients is not assumed.

The cutoff Q=floor(T^(2/5)) is harmless for the lower construction because
all selected labels lie in fixed positive intervals d~T and hence exceed Q
for every sufficiently large real T. Six disjoint boxes force internal
six-tuple distinctness. The repeated-label deletion enforces distinctness
also between the two six-tuples, producing an injective subset of the
candidate's ordered distinct twelve-tuples.

The upper correction uses the probability measure
dnu=w(R/T)dR/(TW). Thus m_C has Fourier kernel w-hat(-T lambda)/W, while
C_harm and C_conn have exactly one outer TW. In particular the unnormalized
J_d in the inherited files is precisely TW m_[12](d), without a missing
power of T or W.

## 3. Independent proof audit and seam derivation

### A. Squarefree lower mass is supplied by actual arithmetic

For each fixed 0<u<v, elementary lattice counting gives
sum_(uT<=n<=vT)r2(n)=pi(v-u)T+O_(u,v)(sqrt(T)). The actual prime factors
give r2(4m)=r2(m), and r2(p^2m)<=3r2(m) for odd p, including the cases
where either side vanishes. In particular an inert prime with odd exponent
remains at odd exponent after adding2; the inequality is not falsely
applied across a change from zero to nonzero representation count.

Every nonsquarefree norm has a prime-square divisor. Summing the rescaled
interval bounds over p<=sqrt(vT) removes at most main fraction

    1/4 + 3 sum_(p odd) 1/p^2
      <= 1/4 + 3(1/9+1/8) = 23/24.

Indeed, for k>=2, (2k+1)^(-2)<=1/(4k(k+1)), whose sum is1/8. The accumulated
area errors are bounded by sum_(p<=sqrt(vT)) O(sqrt(T)/p+1)
=O_(u,v)(sqrt(T)log(2T)), even after replacing primes by integers. Prime2
is priced by1 rather than3, preserving the positive margin. It follows that

    sum_(uT<=d<=vT; d squarefree)r2(d)
      >=pi(v-u)T/24-O_(u,v)(sqrt(T)log(2T)).

This proves the exact substantial arithmetic premise of the isolated Gram
report. It is a macroscopic weighted shell bound, not an assumed squarefree
density or a fine-scale resonance theorem. Real endpoints and the finite
number of small T exceptions are covered by the stated area errors.

### B. Full harmonic functions retain projected energy

For r2(d)>0 set a_d=r2(d)d^(-3/4), h_d=f_d/a_d. The actual prime-factor
inequality gives

    |h_d|<=B, |h_d-h_(d,H)|<=B_H,
    B=sum_s tau(s^2)s^(-3/2)<infinity,
    B_H=sum_(s>H)tau(s^2)s^(-3/2)->0.

When r2(d)=0 the entire class wave vanishes, so its exclusion is lawful.
Choose H first so that a six-factor telescoping tail 6B^5 B_H is sufficiently
small. Choose six disjoint frequency boxes in an interval where Psi>=3/4,
avoiding the finitely many nonzero integer relations with coefficients of
modulus at most2H. A finite union of proper hyperplanes cannot cover an
open box; shrinking around a point outside it provides a fixed positive
separation gamma. All choices precede T.

For a box tuple q=(d_1,...,d_6), let g_q=product_j h_(d_j). The formal
zero-frequency coefficient in g_(q,H)^2 is

    product_j [ (1/2)sum_(s<=H)b_(d_j,s)^2 ] >=(9/32)^6.

It remains positive for sign-changing higher coefficients. Every other
formal frequency is >=gamma sqrt(T) in absolute value; smooth radius
averaging makes its contribution O(T(1+gamma T^(3/2))^(-N)). The uniform
coefficient norm is B^12. Therefore ||g_(q,H)||^2>=cT uniformly in q.

On the scaled radius interval R=Tx, these truncated products have physical
frequencies of modulus O_H(T^(3/2)). Multiply by a smooth cutoff equal to1
on the window and use the ordinary periodic Fourier series on[0,3]. Its
coefficients decay uniformly as (1+|k/3-theta|)^(-L). Truncating at
K=ceil(6(F+1)T^(3/2)) produces an O(T^(3/2))-dimensional subspace V_T and
uniform approximation error O(K^(1-L)) in the scaled sup norm, hence
o(sqrt(T)) in L2(w(R/T)dR). No derivative of sqrt(w) is required.

The previously fixed harmonic tail is then applied to each SINGLE vector:
||g_q-g_(q,H)||<=6B^5B_H sqrt(WT). The triangle inequality for its orthogonal
projection P_T yields ||P_T g_q||^2>=rho T for fixed rho>0. This step retains
the full infinite g_q. It does not subtract a fixed per-tuple error after
summing O(T^12) Gram entries, which would have been inadequate.

### C. Gram positivity supplies the correct absolute mass

Let A_q=product_j a_(d_j). The shell lemma gives
sum_q A_q>=cT^(3/2). Form the Gram matrix G of sqrt(A_q)g_q in the full
Hilbert space, and its projected Gram matrix G_P. Both G_P and G-G_P are
positive semidefinite. Consequently

    tr(G^2)>=tr(G_P^2)>=(tr G_P)^2/dim(V_T)
      >=c T^2 (sum_q A_q)^2/T^(3/2).

The first inequality is a trace inequality, using tr(G_P(G-G_P))>=0;
it is not an unjustified entrywise inequality between truncated and full
correlations. Since |<g_q,g_q'>|<=B^12 WT,

    sum_(q,q') A_q A_(q') |<g_q,g_(q')>|
      >=c T (sum_q A_q)^2/T^(3/2) >=cT^(5/2).

The conversion from squared Gram entries to their moduli is the precise
place where this becomes an absolute certificate. The same argument makes
no assertion about the signed entry sum.

### D. Repeated labels and every harmonic are paid separately

The disjoint boxes allow only equalities d_j=e_j between the two tuples.
For a nonempty equality pattern there are m=12-|E|<=11 free labels. Expand
all twelve full harmonic series. For fixed harmonics and cosine signs,
the coefficient of a shared radical is the integer +/-s_j +/-t_j; an
unshared radical has a nonzero signed harmonic coefficient.

The absolute amplitude is at most

    C_eta T^(-9+12eta) product_(12 slots) tau(s^2)s^(-3/2).

If any combined integer coefficient k is nonzero, freeze the other m-1
labels. At the remaining n~T, consecutive T(k sqrt(n)+alpha) are spaced
by at least c|k|sqrt(T). Thus the Fourier-decay sum over this label is O(1),
uniformly even for arbitrarily large harmonic k. The other label counts
and the outer integral factor T give O(T^m). The resulting contribution
is at most T^(2+12eta) times the harmonic product.

If every combined coefficient vanishes, all six box pairs must be shared:
an unshared label has no second occurrence with which to cancel. There
are only six free labels, giving T^6 choices and a T-sized integral;
the amplitude then makes the contribution O(T^(-2+12eta)). All harmonic
weights sum absolutely to B^12, independent of these spacing constants.

Hence the entire overlap is O(T^(2+12eta)+T^(-2+12eta)). Choosing
eta=1/48 makes it O(T^(9/4)), which cannot erase the T^(5/2) mass. The
remaining pairs inject into ordered distinct twelve-tuples, proving C10.
This also covers zero, small and arbitrarily large common-harmonic
coefficients without dropping exact degeneracies.

### E. The alternate audit proof is consistent, with stronger arithmetic

The current certificate report also rederives the lower bound using a
positive shell fundamental coefficient and near-resonant root-sum bins.
Its special common-multiple majorant is actual arithmetic:
g(s)=product_(p=1 mod4)(2v_p(s)+1), and g(2)=g(3)=g(4)=1. Since the smallest
split prime is5, 2e+1<=3^e and 3^4<5^3 imply g(h)<=h^(3/4). Thus its
displayed exact bound on sum_(h>=2)g(h)^12 h^(-18) is valid and has the
stated positive margin. A generic divisor majorant at h=2 would not
justify that particular proof, but is not substituted there.

Weighted root-sum binning supplies T^(3/2) mass. Removing a specified label
repeat leaves one free root with coefficient +/-1 and at most one integer
completion. Removing a second bounded harmonic relation not proportional
to the fundamental vector uses a nonzero integer two-by-two minor; again
at most one ordered integer pair completes it. Both removal costs are
O(T^(1+2eta)), summed over only fixed finite sets. The proportional vectors
are exactly +/-h sigma and are retained. Their higher-harmonic budget,
the fixed Fourier tail and the per-tuple relative mixed-harmonic tail are
all smaller than the fundamental positive contribution. The chosen
delta<=1/12 is sufficient for Re w-hat>=W/2 because |R/T|<=2. Noneven w
and sign-changing Psi cause no gap. This alternate proof is consistent
with the Gram proof; only the latter plus shell arithmetic is necessary
for the candidate's cited lower-certificate route.

### F. Absolute correction and transfer to actual cumulants

Candidate C3 correctly truncates norm integers only as a proof device at
P=T^(3/2). Distinct squarefree labels imply unequal norm integers in every
harmonic pair. Their root difference is >=1/(2sqrt(P)), so the physical
Fourier argument is >=T^(1/4)/2. Schwartz coefficient tails and smooth w
then prove arbitrarily rapid A1,A2, with all omitted terms paid.

For C4, after expanding and taking moduli, the largest dyadic norm variable
has spacing cT/sqrt(N). Its Fourier-decay sum is O(1+sqrt(N)/T), uniformly
in the other frequencies. Coefficients produce

    product_j N_j^(1/4+eta) N^(-1)
      (1+N/T)^(-J)(1+sqrt(N)/T).

The maximal-scale dyadic sum below T gives T^(max(q/4-1,0)+epsilon), with
the q=3 bounded and q=4 logarithmic cases correctly included. The arbitrary
fixed Schwartz exponent J pays all scales above T, including N>T^2 where
the spacing factor grows. Dropping squarefree-core restrictions is done
only in this positive majorant. There is no assumed near-resonance density.

In C9, dropping cross-block distinctness from a NONNEGATIVE sum allows
factorization into product A_(q_b). Singleton/pair partitions are rapidly
small. The eight remaining shapes have maximal outer exponent9/4 at(9,3),
using one outer TW, and the set-partition coefficients are fixed constants.
The reverse triangle inequality yields

    C_conn>=C_harm-TW sum_d^*|kappa12-m_[12]|
           >=c0 T^(5/2)-C_epsilon T^(9/4+epsilon).

Choose a fixed epsilon<1/4 to obtain C2. This is a valid transfer to the
actual fully pooled cumulants, rather than reuse of an unrelated norm
certificate. It refutes the proposed bound for every-epsilon exponent29/25
while leaving all cross-tuple signed cancellation available.

## 4. First doubtful or unproved step

No unproved step was found in the reviewed certificate, correction, or
transfer under the exact frozen hypotheses. The shell lemma closes the
explicit arithmetic premise of the inherited isolated Gram proof. No
unverified external theorem is needed for this seam.

The first missing step toward complete improvement remains the actual
signed one-sided estimate K12<=C_epsilon T^(29/25+epsilon). The lower
bound for C_conn does not contradict that statement. The signed remainder
C1 and complete restoration are separate review seams; this review does
not claim that the absolute correction exponent9/4 pays the signed
remainder at the target budget.

## 5. Controls and outcomes

- Probability normalization: PASS. Inherited unnormalized Gram inner
  products equal TW times the normalized m_[12]; all lower and correction
  quantities restore this factor exactly once.
- Actual arithmetic and lower mass: PASS. Prime2 has exact factor1;
  odd prime-square removal costs at most3; positive23/24 union margin and
  O(sqrt(T)log T) accumulated errors were independently checked.
- Full harmonics and signs: PASS. Per-vector projected energy retains full
  g_q; overlaps separately sum all twelve harmonic tails with a convergent
  majorant. No sign restriction is imposed on higher Psi coefficients.
- Repeated-label deletion: PASS. At most eleven free labels in the
  nonzero-coefficient case; six in the completely canceled case. The
  twelve amplitude factors remain present even when labels coincide.
- Rapid singleton/pair and complete Schwartz tail: PASS. Only cross-class
  pairs are declared rapid, and both proof cutoffs and dyadic high scales
  have their full tails paid.
- Connected absolute correction: PASS. All eight proper nonrapid shapes
  are included, with maximal9/4 strictly below5/2.
- Signed-versus-absolute scope: PASS. Neither the Gram lower bound nor
  the selected positive tuple subset bounds a signed total from below.
- Exact controls: INSPECTED/PASS as diagnostic evidence. Current manifest
  and local JSON contain exact coefficient, partition, rational-margin and
  multiradius checks. Their finite outputs are consistent with the formulas
  reviewed here. No new experiment was needed or run during this review;
  no finite control is treated as an asymptotic proof.
- Independence: PASS for the assigned seam. The reviewer authored the
  separate signed-remainder discovery report, but did not author the
  certificate audit or either inherited lower proof. Expanded context was
  first opened only after all initial reports were frozen. This is selected
  context line review, not a new claim of statement-only isolation.
- Preservation: PASS by scope. Only this review is written; no candidate,
  initial report, shared state or legacy artifact was edited.

## 6. Dependencies, reviewed artifacts and exact hashes

All filesystem text reads used explicit UTF-8; this review is UTF-8.
Previously read protocol and accepted-kernel context was reused without
unnecessary rereading. The active manifest was read at its review-stage
version; graph bytes still match the frozen starting graph.

| Artifact | SHA-256 |
| --- | --- |
| rounds/codex-managed/gc-connected-cumulant-test/briefs/certificate_review.md | 8560813ee1ae1b4ae9e6f8be17a2acca8fc52bd650dbb18c4421ae9a9ecf2f37 |
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 7736f3050adba099c4ecbbb9eb78639f4a32b8ae9361ce7c05f5cc04f023a13b |
| rounds/codex-managed/gc-connected-cumulant-test/candidates/conductor_connected_test.md | 3a443b5e63e826511f99e9428438018e5fc41f358a014fc15d9b8bb75233ae97 |
| proofs/kernels/gc_complete_distinct_radical_moment_reduction.md | d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0 |
| rounds/codex-managed/gc-connected-cumulant-test/controls/control_manifest.md | 9254a1fcc8b0667539e4c150740e41c4d4c93e01777bf569958a268abde4240d |
| rounds/codex-managed/gc-connected-cumulant-test/controls/exact_local_controls.json | 89e888dfaf9c7e933ebeded4b165ae0598880aebcc29b1d30f3e18d46b780cd1 |
| rounds/codex-managed/gc-connected-cumulant-test/reports/connected_certificate_audit.md | 7e18113aef8099a1724256720d196eecec0d61dd9ab6bddf47590261d51783c6 |
| strategy/round231_harmonic_admission/reports/blind_harmonic_pooling.md | 16af77813be06098cc10ff77c1b176657953024c37ef52873d81f648a6f871f8 |
| strategy/round231_harmonic_admission/conductor_harmonic_obstruction.md | 83d83c24ef7030ec125c1755856222d5f09bf691f6f2ee8602c79aad6bd1ccc7 |

The review required no source search, imported theorem, additional numerical
test, or read of unlisted strategy/review artifacts. The graph is authoritative;
the inherited certificate remains reviewed admission evidence rather than
an automatically accepted graph theorem.

## 7. Recommended state effect

Retain the exact candidate's C3, C4, C9, C10 and C2 as reviewed evidence
for this bounded test. The assigned actual lower-certificate and subtraction
scope gate passes. No repair or second lower-proof cycle is required.

Support the candidate's proposed closure without complete gain and identity
State Patch, subject to the other separately assigned gates. Preserve the
accepted graph and proof draft. Keep the signed K12 target, all complete
improvement claims and all higher-order extrapolations open. This task
freezes here and does not design or start another round.

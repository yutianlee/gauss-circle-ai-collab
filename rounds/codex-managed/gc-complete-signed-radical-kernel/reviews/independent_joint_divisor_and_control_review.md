# Round218 independent divisor and conductor-control seam

## 1. Result and exact-hash verdict

Reviewer: `joint_lattice_kernel`, temporary NONBLIND same-round reviewer.
Campaign: `gc-complete-signed-radical-kernel`; round218; 2026-09-28.
Starting graph SHA256:
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

**GREEN for the stated local identities, complete cost diagnosis, and
narrow certificate scope.** Neither reviewed artifact proves the signed
I12 target. No mandatory mathematical correction is identified.

The following exact files were read and their supplied hashes were
independently reproduced before review:

| Artifact under `rounds/codex-managed/gc-complete-signed-radical-kernel/` | SHA256 |
|---|---|
| `reports/joint_divisor_kernel.md` | `81a983cbf4f3de82e0c88911d1569c26b3920c7b6cb4adaf7ebb71918cdcba87` |
| `controls/conductor_joint_rank_and_shell_cost.md` | `f865b9d69883b47d75cb1033b3aaf3f4a1ee9e6a9015ae5deb42f76eed570b2d` |

The divisor report's certificate (14) and the conductor's G_N both take
absolute values INSIDE the R integral. They are not the stronger
after-R, per-complete-dual-tuple certificate in this reviewer's frozen
discovery report. Their lower bounds are valid at their own stated
modulus placement. No implication between these certificate lower bounds
is used in this verdict.

## 2. Exact statements and hypotheses checked

The full actual B_T, mollifier transform Psi, displaced smooth w, real
T>=2, and fixed twelfth order are those of the accepted216 reduction.
The original character opening is r2=4(1*chi4). The divisor amplitude
is smooth on genuine positive d,m boxes with their sampled integer
partition retained, N=DM, N<=O(T^(3/2)). Every box has fixed derivative
bounds after rescaling d by D and m by M. The upper cutoff's discarded
Schwartz tail is explicitly included in the error ledger.

The reviewed conclusions are the exact character Poisson formula and
paired leading sine kernel; joint rank14 and nullity11 when an interior
critical set exists; the localized first stationary remainder and its
complete dual summation; the positive leading-packet cost T^7 N^-6 on
an equal box; the complete elementary bound M12(B_T)<<T^(7/3+epsilon);
and the equivalent normalized signed target exponent179/25.

The conductor control concerns only a positive certificate of leading
Gaussian-lattice packets on actual integer dual vectors. Its lower
bound uses fixed N=T^a with 0<a<1, including a=2/3. Its full truncated
upper range includes Schwartz block factors. It expressly leaves exact
stationary remainders and far frequencies to the discovery/application
analysis. No stronger exact-Poisson lower bound is asserted there.

## 3. Independent derivation and seam checks

### A. Character sign, coefficient and conjugate pairing

Under the minus-sign Fourier convention,

    chi4(d)=(e(d/4)-e(-d/4))/(2i).

The first branch gives Fourier labels h-1/4=(4h-1)/4, whose numerator
has chi4=-1, with coefficient1/(2i)=-i/2. The second gives h+1/4,
whose numerator has chi4=+1, with coefficient-1/(2i)=+i/2. Thus

    sum chi4(d)F(d,m)
      =(i/2) sum_(a odd,k integer) chi4(a) F-hat(a/4,k).

The original factor4 times the cosine's1/2 then leaves exactly the
factor i in divisor equation(2). There is no missing factor2 or sign.

For d=r exp(t), m=r exp(-t), the Jacobian is2r. For a,k>0,
the minimum of (a/4)exp(t)+k exp(-t) is sqrt(a k), attained at
t0=(1/2)log(4k/a). Hence the report's exact cosh phase is correct.
The transverse Hessian is negative, giving e(-1/8). Multiplying
2r, the original r^(-3/2), and the stationary factor(lambda r)^(-1/2)
leaves 2 lambda^(-1/2)dr/r, exactly the coefficient in equation(5).

The positive branch in(2) therefore contributes

    i chi4(a)e(-3/8)e(-1/8)K_A=-i chi4(a)K_A.

On replacing (sigma,a,k) by(-sigma,-a,-k), the integral is conjugated
and chi4(-a)=-chi4(a). The other contribution is
i chi4(a)conjugate(K_A). Their sum is

    2 chi4(a) Im K_A.

Thus the leading profile is the odd sine transform and vanishes at
R=lambda. This calculation uses the actual character and cosine phases;
it does not assume a real or even Fourier transform of w.

### B. Local remainder, crossings, and complete dual tails

Let U=T sqrt(N). In scaled box coordinates, the phase derivatives
are O(U); the relevant positive dual ranges have
aD~U and kM~U. Each dual range has length at least a fixed multiple
of T^(1/4) in the truncated range, and the product of their lengths
is O(T^2). These observations justify both the integer +1 terms and
the report's O(T^2) central-label count, including D or M bounded.

The exact change v=2sinh((t-t0)/2) makes the transverse phase
-lambda r v^2/2. The first omitted angular term gains(lambda r)^(-1).
After multiplying the original Jacobian/amplitude, its radial amplitude
has size lambda^(-3/2)r^(-2)dr. Its integral on r~sqrt(N) is
O(T^(-3/2)N^(-1/2)). Its scaled radial derivatives obey the same symbol
bounds. Factoring e((R-lambda)r) and integrating radially gives the
localized factor(1+sqrt(N)|R-lambda|)^(-A0). This verifies equation(6)
in the stated central range, not merely a pointwise error with an
unpaid interval-length factor. Smooth profiles extended through their
support edges supply a uniform stationary transition without hard
endpoint terms.

Outside an enlarged central dual rectangle, at least one scaled d or m
derivative is bounded below by a fixed fraction of U plus the excessive
dual coordinate. A fixed partition selecting such a derivative and
repeated integration by parts gives a bound of the form

    C_J C_N N^(1/4) U^(-J)
       (1+|a|D/U+|k|M/U)^(-J)

on those nonstationary pieces. The factor N^(1/4) is the original
box volume N times the coefficient size N^(-3/4). Summing the decay
in a,k costs O(T^2). Since N<=O(T^(3/2)), this is at most
C_J T^(19/8-J), up to a fixed profile/Schwartz factor. Choose J above
any requested tail order plus a fixed constant. Wrong-sign branches
and k=0 have a derivative of size at least cU and are covered by the
same reasoning. In the central rectangle, radial mismatch of size
comparable to T is paid by arbitrary powers of U after the transverse
step. Smooth lambda cutoffs only affect this nonstationary range.

These estimates make the report's complete far-label summation explicit.
Its constants require finitely many fixed smooth seminorms, available
from the stated profiles and Psi. No mathematical experiment or external
arithmetic theorem is needed.

For central labels put q=a k. On lambda~T, the actual shell of width
N^(-1/2) contains O(1+T/sqrt(N)) possible integer q. Each q has at
most tau(q) positive factorizations, even before the odd-a and ratio
restrictions. Dyadic mismatch bands with large A0 therefore prove
equation(10). The first angular remainder sums to

    T^(-3/2)N^(-1/2) * T^(1+epsilon)N^(-1/2)
      =T^(-1/2+epsilon)N^(-1),

as claimed. Summing original boxes costs only a logarithmic power.
The complete wave error has supremum O(T^(-1/2+epsilon)), and hence
twelfth moment O(T^(-5+epsilon)). It is legitimately paid by L12 norm
inequalities; no additive cancellation of mixed moment terms is assumed.

### C. Joint rank, unequal scales and profile control

For the divisor phase the twelve transverse Hessian entries are
-sigma_j R r_j. The R/radial Hessian is the block matrix with off-diagonal
vector sigma, of rank2. At an interior stationary point the angular
cross terms vanish. This gives rank14 and nullity11. After rescaling
radial variables the off-diagonal vector becomes sigma_j sqrt(N_j),
which remains nonzero and gives exactly the same rank. Only feasibility
of the signed radial balance changes. All-equal signs have no point.

At equal N, original joint measure/amplitude has size T N^3, and the
seven nondegenerate pairs/directions contribute(T sqrt(N))^(-7).
Their product is T^(-6)N^(-1/2). This agrees with twelve scalar
T^(-1/2) packets and their common width N^(-1/2). No full-rank estimate
is valid. Nonproduct smooth amplitudes alter seminorm constants but not
these phase ranks.

The conductor's Gaussian-lattice angular Hessian has the opposite
angular sign convention to the divisor cosh Hessian. Its signature
sum sigma_j combines with the original cosine multiplier to give
e(-sum sigma_j/4), as stated. This produces the same odd scalar sine
profile after the real branches combine, without identifying the two
intermediate Gaussian phases. For p even its pth integral is positive;
for p=1 no full common-R stationary point exists on positive radii.
The fixed-R rank-one control and the p=2 radial line control are correct.

### D. Modulus placement and actual multiplicity lower controls

In the divisor positive rectangle a~2T, k~T/2 with odd a, there are
comparable to T^2 actual pairs, lambda lies in the w=1 region, and t0
stays in a positive-profile interior. At N~T^(2/3), Psi tends to1 on
that box. On a small positive offset interval of length N^(-1/2),
Im K_A is at least cT^(-1/2). Each packet's integrated modulus is
therefore at least cT^(-1/2)N^(-1/2). If H(R) is the nonnegative
packet sum in(14), then

    integral wH >> T^(3/2)N^(-1/2),
    integral wH^12 >= (integral wH)^12/(integral w)^11
                    >> T^7 N^(-6).

The matching upper follows from the true factorization count, and for
unequal boxes keeps each N_j separately in equation(13). This lower
bound concerns exactly(14), with moduli before the R integration.
It does not prove the same lower bound after moving each modulus outside
an integrated signed twelve-tuple.

For the conductor G_N, the elementary disk comparison gives comparable
to T^2 integer vectors in J'. Its T-sized margin pays the packet tails
outside J. Each leading packet has integrated modulus comparable to
T^(-1/2)N^(-1/2), uniformly when its T-dependent actual mollifier profile
converges to the displayed nonzero S at fixed a<1. Holder therefore
gives T^(1+p/2)N^(-p/2). Upper shell counts use r2(q), so no norm
multiplicity is dropped. These conclusions are GREEN as statements
about the named leading positive certificate. They do not require an
exact-Poisson remainder lower bound, which the control does not assert.

### E. Complete restoration and179/25 normalization

The two scalar ceilings are N^(1/4) and T^(1/2)N^(-1/2).
The exact coefficient square sum is O(T^epsilon N^(-1/2)); frequency
spacing is at least c/sqrt(N). Since T/sqrt(N)>>1, the smooth-window
Gram row sum is O(T), and opposite cosine signs only increase the
frequency mismatch. Thus the actual second moment is
O(T^(1+epsilon)N^(-1/2)). Multiplying it by the tenth power of either
ceiling gives

    min(T N^2,T^6 N^(-11/2)).

The crossover N=T^(2/3) has cost T^(7/3). Smooth dyadic recombination
with the L12 triangle inequality pays every unequal mixed term by a
logarithmic power. The bounded initial blocks and full Schwartz tail
are paid explicitly. This reproduces the complete203 bound and gives
no improvement over the accepted204 T^(10 beta+epsilon).

Finally, equation(20) has the exact leading factor2T^(-1/2). Raising
its scaling to the twelfth power costs T^(-6). Its error has negligible
L12 norm in both directions of the norm inequality. Hence

    M12(B_T)<<T^(29/25+epsilon)
      iff integral w|D_T|^12<<T^(6+29/25+epsilon)
                             =T^(179/25+epsilon).

The factor2 is a fixed constant. This is an equivalence of unproved
target bounds, not an additive moment expansion. The subsequent216
transfer pays the head at15/13 and repeated classes at8 beta-1/5;
neither changes179/25 or supplies its missing arithmetic estimate.

## 4. First doubtful or unproved step and corrections

No mathematical correction is required for the two hashed artifacts
within the scopes just verified. The divisor report's opening phrase
about the common radius being integrated must be read with its exact
definitions(13)--(14): their positive closure places the packet moduli
inside that integral. The conductor's G_N has the same placement.
This review does not strengthen either statement by silently moving
moduli. The explicit formulas are sufficiently unambiguous to require
no text repair.

The first unproved analytic step remains the signed estimate(21) for
the complete D_T. None of the correct rank, odd-center cancellation,
individual profile bounds, divisor counting or leading positive
certificate estimates proves it. No source theorem is newly imported.

## 5. Controls and review outcomes

- Actual r2 and chi4 algebra, odd-quarter labels, the Gaussian factor,
  all conjugate signs, and the exact real sine pairing: GREEN.
- Localized first remainder, zero and wrong-sign labels, full far-dual
  summation, smooth support crossings and Schwartz tails: GREEN.
- Rank14/nullity11, incompatible signs, unequal radial scales and
  nonproduct smooth-amplitude rank scope: GREEN.
- True integer factorization/lattice multiplicity, real shell endpoints
  with +1, and the two inside-R positive certificate lower controls: GREEN.
- Complete second moment, unequal-block assembly, T^(7/3), and the
  normalized179/25 target: GREEN.
- Paid216 head/repeated-class transfer, no smooth arithmetic mask,
  signed-versus-certificate distinction, and fixed-order/full-quarter
  distinction: GREEN.

GREEN validates these named claims only. It does not certify the open
I12 target, permit deletion of a near-shell complement, or prove any
M1/M2/GAR parent. The lower controls are certificate lower bounds, not
lower bounds for a signed arithmetic moment. Zero experiments were run.

## 6. Dependencies, isolation and exact artifacts

Only the two specifically authorized current-round artifacts in Section1
were newly read. Their exact hashes were checked with SHA256. The
reviewer also used the original permitted context already read for its
discovery task: protocol, authoritative graph and218 manifest/strategy,
closed217 checkpoint, accepted204/216/217 kernels, and the closed203,
210 and215 syntheses. No other current-round file, sibling review or
isolated packet was read. The control's mention of another historical
round was not followed as a new dependency.

This reviewer is NONBLIND. Its own frozen discovery report at
`c3193b053d594b3a1599cdf707161b438f3387703f9e0f2010cf1d3b0101d41c`
was not edited. Its stronger after-R certificate is not used to prove
the different lower bounds under review. Elementary character algebra,
Gaussian stationary expansion, scaled integration by parts, divisor
counting and Holder provide the independent calculations above.

This review is the only file written on this assignment. No shared
state, synthesis, old artifact, new round, or experiment was modified
or created. All review effort was analytical/algebraic and provenance
checking.

## 7. Recommended state effect

Retain both exact-hash artifacts as GREEN bounded method evidence and
close their assigned seams. Apply no theorem promotion or exponent
change on their account. Keep the complete signed target and every
full-quarter parent open. The report gives a fully costed failed
closure, not a successful arithmetic estimate or a claim that genuinely
signed near-shell methods cannot work. This reviewer stops here.

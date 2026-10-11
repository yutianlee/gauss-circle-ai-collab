# Round220 independent reciprocal-source seam

Campaign: `gc-full-goal-arithmetic-source-review`. Date: 2026-09-28.
Reviewer: `full_frontier_sources`, reused agent; NONBLIND source/application
review. I authored this round's other source report and the earlier219
dispersion review. Neither authorship is statement-only independence.
This review independently checks the finite source applications and costs;
it does not supply a new proof of the external theorems.

## 1. Result

**GREEN** for the bounded conclusions of
`reports/reciprocal_energy_sources.md`, final SHA256
`9fbde8516f7b8524a3af2f0ae2605b63cb993deab537dff3ae9c700e1b6c82fd`.
The exact completion, multiplicity norm, stated theorem maps, excluded
sector fallbacks and restored powers check. Both enlarged-row controls
check with their explicitly limited scope. No correction to this frozen
report is required.

The conclusion is no complete source gain, not a no-go theorem for the
actual energy or for every possible application of these sources. The
corrected M2 UNBAL table uses the graph's `K=XL/D^2` and
`e(sqrt(X h k))`. The superseded report hash is not reviewed here.

## 2. Exact statement and hypotheses reviewed

The target is the actual real energy

    E=sum_k [sum_(j,a odd) sigma_j chi4(a) omega_(j,a)(k)
                                  sin(2 pi k R_j^2/a)]^2,
    E <= J^2 v^2 T K/256+C_eta T^(208/2625+eta) J A K,

where `K=N/D`, `A=T sqrt(N)/D`, `b0=D/sqrt(T sqrt(N))`,
`N<=T^(3/2)`, `R_j~T`, and every stationary interval and inherited
endpoint value belongs to the actual real weight. The original physical
signs are `sigma_j=sign H(R_j)`. Both modular difference and sum aliases
remain. The proof reviewed is a fully priced upper application, not a
proof of this target.

The external statements were checked against the exact primary texts:
[Blomer--Pascadi2607.24311v1, Theorem1.1](https://arxiv.org/html/2607.24311v1#S1),
and [Milicevic--Qin--Wu2511.07550v1, Theorem1.1](https://arxiv.org/html/2511.07550v1#S1).
BP uses unnormalized `S(m,n;q)`, a unit multiplier, interval lengths
at most `H<=q`, and a joint gcd restriction which the theorem explicitly
removes for the two origin intervals `[1,H]`. MQW uses normalized
`Kl2(z;q)=q^-1/2 sum_(x unit)e((zx+xbar)/q)`, origin-supported vectors,
and all three stated length restrictions. No additional source theorem
or factorability assumption is imported by this review.

## 3. Independent derivation and seam checks

### 3.1 Rounding, actual weights and endpoint operators

Writing `R_j^2=M_j+delta_j`, `|delta_j|<=1/2`, gives the exact factor
`e(delta_j k/a)`. Its exponential series has projective sup-norm mass
at most `exp(C K/A)`, bounded because `K/A=sqrt(N)/T<=T^-1/4`.
Each term separates in j, a and k. Thus its removal as an error is
unnecessary and was not used in the report.

The actual smooth amplitude becomes
`x^-1/2 z^-1 Psi(2 sqrt(N/T) xz/y)` on fixed positive compact ranges
of `x=R_j/T,y=a/A,z=k/K`. Each fixed derivative is controlled by
finitely many `s^r Psi^(r)(s)` seminorms. Smooth compact extension and
integration by parts yield a uniformly summable product Fourier series.
This works for `N>T` as well and retains the sign of `Psi`.

Both stationary inequalities are monotone in positive k, so their
intersection is an interval. At a fixed dyadic column scale, each row
interval uses at most two disjoint canonical intervals. Split these
into two lists; for each list the row groups and column intervals are
disjoint. Restriction of a matrix of norm `Lambda`, followed by Cauchy
over those groups, bounds that scale by `Lambda||x||_2||z||_2`.
Summing scales proves the claimed logarithmic norm price. The finitely
many possibly coincident endpoint corrections are bounded row-weighted
singleton masks and have the same price. No uniform endpoint separation
is needed.

This is a statement for arbitrary vectors in the actual row index. It
does not turn a j/a/k product coefficient theorem into a theorem on
arbitrary `(j,a)` rows. Indeed a bounded J-by-A mask has the safe
row-expansion projective l2 price `J sqrt(A)`, or `A sqrt(J)` by
columns; relative to its combined-row envelope `sqrt(JA)` this permits
the factor `sqrt(min(J,A))`. The report avoids this issue by obtaining
a genuine fixed-a j/k operator before masking, and paying the entire
a triangle sum.

The conductor's literal-deletion control also checks: an `O(K/A)`
error per row term gives `O(K)` per j,k after all a, hence an energy
error at most `O(J^2 K^3)`. Its ratio to `J^2 v^2 T K` is
`K^2/(T v^2)`, which is not uniformly certified small. This is an
upper error price only.

### 3.2 Completion and exact multiplicities

For fixed a set `g=gcd(M_j,a)`, `q=a/g`, `m_j=M_j/g`. When `q>1`,
`m_j` is a unit modulo q. Opening the Kloosterman sum gives

    q^-1 sum_(n mod q) S(k,n;q)e(-n mbar/q)
      =sum_(x unit)e(kx/q)1_(xbar=mbar mod q)
      =e(km/q).

This verifies the sign and factor in report(9) for every integer k,
including nonunits. All n residues, including zero, are indispensable.
Representing zero by q on `[1,q]` is exact. No ordinary reciprocal
has been silently replaced by a modular inverse.

For the completed vector `B_g(n)=sum_j x_j e(-n mbar_j/q)`, direct
orthogonality gives

    sum_(n mod q)|B_g(n)|^2
      =q sum_(r mod q)|sum_(j:mbar_j=r) x_j|^2
      <=q mu_g sum_j|x_j|^2.

Thus the multiplicity `mu_g` cannot be deleted. Cofactor folding has
at most `O(1+K/q)` original k's per residue; Cauchy proves its square
root l2 cost. The `q=1` rows have direct operator norm at most
`O(sqrt(J_g K))` and require no modular inverse. Gcd strata partition
the original anchors at fixed a, so their reconstruction adds no
unrecorded multiplicity.

### 3.3 BP: legal source application and complete cost

Use the exact source choice `H=q`, both intervals `[1,q]`, multiplier1.
The source's origin-interval clause removes its gcd restriction even
on the nonunit and residue-zero portions of the completed vectors.
At this length its three bracket exponents are `1/32,1/8,5/18`.
Consequently the combined completion/source/Parseval power is

    q^-1 q^(1+5/18) q^(1/2)=q^(7/9).

Including residue multiplicity and cofactor folding gives exactly
report(11): `q^(7/9+epsilon)sqrt(mu_g)sqrt(1+K/q)` times the two
original l2 norms. Since `q<=a` and `K<=C a`, its q/K factor is
`O(a^(7/9))`. Cauchy over strata uses `sum_g mu_g<=J`, while for
the actual bounded rows `sum_g sqrt(mu_g J_g)<=sum_g J_g=J`.
The q=1 term fits the same bound.

After actual smooth factors and stars, the fixed-a vector therefore
costs `T^epsilon J a^(7/9)`. The complete O(A)-term triangle sum and
squaring cost `T^epsilon J^2 A^(32/9)`. Passing from the sine norm
to the complex norm is a legitimate upper enlargement explicitly
identified in the report. The elementary bound `J^2 A^2 K` is better:
the ratio of the BP price to it is `A^(14/9)/K`, which is large on
the complete range `K/A<=T^-1/4`, `A>=T^(1/4)` up to fixed constants.
This establishes failure of this particular certificate, without a
failed BP hypothesis or a signed lower bound.

### 3.4 MQW: unit condition, all length failures and fallbacks

For `(k,q)=1`, change unit variables to obtain
`S(k,n;q)=sqrt(q)Kl2(kn;q)`; the completed factor becomes `q^-1/2`.
For nonunit k this substitution is not licensed. The alternative
`q^-1/2 sum_n Kl2(mkn;q)e(-n/q)` enforces `(mk)x=1` and is zero
on nonunits. The report correctly retains those omitted rows/sectors
for its elementary fallback.

On q sufficiently larger than K, set source lengths `M=ceil(2K)`
and `H=q`. The product restriction requires `K<<q^(1/4)`; its
`M^(7/5)H` condition additionally requires the exact stated strict
inequality, which is compatible in this power range for large q.
The reversed orientation would need simultaneously `K>>q^(3/4)`
and `K<<q^(1/10)`, so it is unavailable. Folding both variables to
length q gives product `q^2>q^(5/4)` for large q. Endpoint constants
and bounded q can be paid trivially and are not concealed by power
notation.

Inserting `sqrt(q mu_g)` and `q^-1/2` in the normalized source bound
produces, term by term,

    sqrt(mu_g)[q^(2/3)
        +K^(19/50)q^(2/5)+K^(5/16)q^(31/64)],

times `q^epsilon||x_g||_2||z||_2`, agreeing with report(15).
For `K<<q^(1/4)`, the leading term is already larger than `sqrt(K)`.
With the unexcluded worst case `mu_g=J_g`, the elementary operator
price `sqrt(J_g K)` is better. A specific small actual multiplicity
might improve a subcase, but no such uniform actual saving is claimed.

At the displayed compatible band `N~T^(2/3),D~T^(2/15)`, the lengths
are `A~T^(6/5),K~T^(8/15)`: a stratum `q~A` misses the condition
since `8/15>3/10`. This diagnoses a permitted parameter band and
does not assert high-point existence. The report partitions all legal
unit blocks, nonunit blocks, q=1 and the other length ranges. Taking
the minimum with the elementary bound on legal blocks and that bound
on every complement, then summing all actual a, proves the full cap
`E<<J^2 A^2 K`. Nothing is left unpaid.

### 3.5 Both enlarged-row controls

With `N~T,D~T^(1/4),A~T^(5/4),K~T^(3/4),J~T^(1/2)`, choose odd
`a0~A` and J integers q_j in an interval of length comparable to
`T^2/a0~T^(3/4)`. Then `R_j=sqrt(a0 q_j)` lie near T and have
spacing at least a fixed multiple of `a0/T~T^(1/4)`. The unmasked
complex rows at a0 equal1, so their submatrix norm squared is at
least `cJK`. The proposed report(16), divided by JK, instead tends
to zero as

    O(T^(rho-1/2+epsilon)+T^(-21/500)), rho=208/2625.

This disproves that enlarged complex operator assertion. The selected
sine rows are zero, exactly as the report warns.

For the shifted control take integer `r` nearest `a0/(4K)` and
`M_j=a0 q_j+r`. The radii remain integral-square anchors with the
same separation properties. On `K/2<=k<=K`,

    r k/a0=k/(4K)+O(K/A).

The main argument belongs to `[1/8,1/4]`, and `K/A` tends to zero.
Hence the identical sine rows have squared norm at least `cK`.
The real submatrix norm squared is again at least `cJK`, disproving
the enlarged real-row version at the same powers. This is an exact
algebraic control, not an experiment.

Both tests choose a row vector supported at a single a0, whereas the
actual vector includes all its character-weighted rows and stationary
masks. Neither construction proves high-point membership or the
required physical sign alignment. Thus neither refutes the actual
real energy target. The root rounding control contains the first
construction; the second is separately explicit in the frozen source
report and has been independently verified here.

### 3.6 Full physical and moment normalization

The common restoration factor is

    (K/N^(3/2))b0^2=D/(TN),       b0^2 JAK=JN.

It converts the raw BP certificate to
`T^epsilon J^2 T^(23/9)N^(7/9)D^(-23/9)`, and the elementary
source cap to `J^2 T K/D`. The already reviewed219 modular fallback
`E<<T^epsilon J^2 A^2 min(D,K)` instead restores to
`T^epsilon J^2 T min(D,K)/D`. For `D<=sqrt(N)` the latter is
`T^epsilon J^2 T`, missing `v^2` at the lowest level by `99/125`.
These are all upper certificates, not lower bounds for actual E.

The inherited transform-error absorption exponent also checks directly.
Its ratio is bounded by
`T^epsilon[sqrt(N)/(v^2 D^2)+1/(Tv^2)]`. Using report(1) and
`N>>v^4`, its first term is

    <=T^(13/21+epsilon)v^-6 N^(-4/21)
    <=T^(13/21+epsilon)v^(-142/21)
    <=T^(-221/2625+epsilon).

Thus the admitted uniform sharp-endpoint remainder is safely paid;
it cannot supply the missing energy cancellation. The reviewed219
sharp-interval transform is an inherited dependency, not reproved as
a new theorem in this source review.

The n-tail, singleton, partial interval, all dyadic rectangles and
level unions are explicitly retained. Their Schwartz or logarithmic
prices do not improve the unsupported middle estimate. Accepted204
therefore still supplies the complete high-tail exponent `10 beta`.
Conditionally, `42rho/13=32/125`, so `113/125+42rho/13=29/25`;
the fixed twelfth bridge gives `102/325`, not quarter. The sufficient
unbounded-fixed-order family, every complete M1/M2 parent, GAR's
separate total-M1 scope and endpoint assembly remain open.

## 4. First doubtful or unproved step

No proof defect was found in the frozen report's bounded assertions.
The first unproved target input is still its complete real energy
inequality(3). BP's exact application is too expensive; MQW fails
its length hypotheses on full permitted ranges and supplies no
uniform sufficient norm even on its eligible portion after completion.

A stronger structured-coefficient theorem or a different fully priced
map could change that conclusion. This review does not exclude such
work. In particular, the two enlarged-row counterexamples cannot be
used against actual high-point coefficients.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Exact primary statements and normalization | GREEN: both specified Theorem1.1 statements match, including BP's origin-interval gcd clause and MQW's normalized kernel. |
| Completion signs, units and zero residues | GREEN: orthogonality recovers the exact phase; q=1 and nonunit cofactor sectors have explicit fallbacks. |
| Parseval and full-residue norms | GREEN: `q mu_g`, cofactor folding, all n residues and reconstruction costs are retained. |
| Rounding and actual weights | GREEN: bounded exact multiplier mass, uniform Schwartz seminorms and logarithmic starred interval masks under a genuine row operator. |
| All modular aliases and real pairing | GREEN: sine-product difference-minus-sum identity remains exact; complex norms are labeled upper enlargements. |
| Enlarged complex and shifted-real rows | GREEN: both norm lower bounds are rigorous, and neither supplies actual high points or their coefficient vector. |
| Full restoration and excluded ranges | GREEN: raw BP, complete source cap, better inherited modular fallback, error absorption and full physical tail all accounted for. |
| Frontier normalization | GREEN: final hash contains both corrected UNBAL formulas and forward-only provenance. |
| Independence and computation | NONBLIND disclosed; no claim of statement-only status, no experiment or new source theorem. |

## 6. Exact dependencies and artifacts used

* Frozen source report: `reports/reciprocal_energy_sources.md`, SHA256
  `9fbde8516f7b8524a3af2f0ae2605b63cb993deab537dff3ae9c700e1b6c82fd`.
* `controls/conductor_rounding_and_operator_control.md`, SHA256
  `5d24c346a285958510dba55fc085d9a785c0099b3df2b03497cdc0bc325c790f`.
* `controls/conductor_frontier_normalization_correction.md`, SHA256
  `849601b500059325accaba60a559a3e941bf427b11e8cab0bea008ef46a210d8`.
* Exact primary theorem text linked in section2, versions
  BP2607.24311v1 and MQW2511.07550v1 only.
* Previously permitted protocol, graph, accepted204/216 kernels and219
  synthesis supply inherited scope and restoration; graph SHA256
  `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.
  My earlier219 dispersion review and my current full-frontier report
  are disclosed prior work, not additional independent source evidence.

The final source hash was recomputed after the conductor supplied it,
and its corrected table/provenance was read explicitly. The isolated
operator report and other current reviews were not read. Root control
references to that isolated report are not treated as having reviewed
its contents here.

## 7. Recommended state effect

Retain the frozen report as GREEN reviewed method evidence. Reject
only the stated enlarged arbitrary-row certificates, in both complex
and shifted real forms. Keep the actual signed target and all full
proof obligations open. No graph, proof draft or exponent change is
justified by these source applications.

Only this assigned review was written. No old report, shared state,
synthesis or successor artifact was edited. Stop after final hash.

# Round 177 hostile audit: primitive alias capacity and hybrid large-sieve self-return

## 1. Result

The primitive-modulus ledger is exact and yields one genuine target-safe
packet, but the proposed coefficient-uniform reciprocal large-sieve and
positive \(TT^*\) continuations do not close the remaining packet.  The
narrowest justified terminal verdict is

\[
 \boxed{\texttt{k17a\_joint\_inverse\_residue\_alias\_capacity\_or\_self\_return\_no\_go}.}
\tag{177.H1}
\]

More precisely, let

\[
 g=(u,n),\qquad u_0=u/g,qquad n=gn_0,qquad (n_0,u_0)=1.
\tag{177.H2}
\]

For fixed \((\kappa,u,u_0)\), in either orientation, the complete literal
stratum has

\[
 O(u_0)\quad n\text{-values},\qquad
 O(L/\kappa)=O(u)\quad v\text{-values},\qquad
 O(\kappa)\quad t\text{-sites},
\tag{177.H3}
\]

and hence exactly the available raw capacity

\[
 \boxed{O(Lu_0X^\eta).}
\tag{177.H4}
\]

There is no omitted gcd multiplicity in (177.H4).  Reduction from \(u\)
to \(u_0\) makes the \(v\)-interval repeat modulo \(u_0\) about \(g\)
times, while the fibre contributes \(\kappa\) repeats; their product is
\(\kappa g=L/u_0\), up to the fixed relative support constants.

The original \(u\)-alias packet folds exactly to the \(u_0\)-packet:

\[
 \boxed{
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell)
 \qquad(\ell\bmod u_0).}
\tag{177.H5}
\]

If

\[
 q={u_0\over(\ell,u_0)}
\tag{177.H6}
\]

is the exact additive conductor of the folded alias, then

\[
 \boxed{
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)=q}}
 |c_{u_0}(\ell)|
 \ll {q\over u_0}\log(2q).}
\tag{177.H7}
\]

Consequently, for every fixed \(A>0\), the complete literal alias packet
with \(q\le P=(\log X)^A\), summed over every exact gcd stratum, every
supported \((\kappa,u)\), and both orientations, is

\[
 \boxed{\ll_{A,\delta,\gamma,\varepsilon}L^2X^\varepsilon.}
\tag{177.H8}
\]

This is stronger than merely counting the physical sector
\(u_0\le P\): it is an exact target-safe alias-space packet for
\(q\le P\), even when \(u_0>P\), with exact complement \(q>P\).
It is owner-complete as a transform packet, although it is not a partition
of physical incidences.

For \(q>P\), positive fixed-conductor closure needs a full factor \(q\).
Even granting one square-root reciprocal saving leaves
\(L\sqrt q\,X^\varepsilon\), not \(L X^\varepsilon\).  Exact weighted
\(TT^*\) keeps the rank-one alias kernel and reconstructs the original
physical square.  Replacing that kernel by alias Cauchy and Parseval gives
a residue-bucket energy; positive off-diagonal recombination restores
\(Lu_0\), while even the optimistic certificate that disposes of every
off-diagonal still carries diagonal capacity \(u_0\sqrt L\) and therefore
cannot close \(u_0>\sqrt L\).  These are method capacities, not lower
bounds for the literal K17a sum.

The no-go covers only: one reciprocal square-root saving followed by
positive recombination; exact alias \(TT^*\) with no new signed input; alias
Cauchy followed by nonnegative diagonal/off-diagonal majorants; primitive
completion that ignores lift multiplicity; separate-orientation moduli;
and positive recombination of squarefree, endpoint, or stationary-mode
openings.  It does not exclude a selector-specific signed two-variable
estimate giving the full factor \(q\), cancellation across gcd or alias
conductors, a signed residue-bucket theorem, or a new non-complementary
two-orientation identity.

## 2. Exact statement and hypotheses

Assume the complete Round-177 range

\[
 J=\sqrt X,\qquad 1\ll L\ll H\le J^{1/2},\qquad
 R_0=\lceil L\rceil,
\tag{177.H9}
\]

fix \(0<\delta<1/2\) and \(0<\gamma<1\), and retain exactly

\[
 R_{\log}<2\kappa n<R_0,\qquad
 \kappa<\delta L,\qquad (u,n)<\gamma L,
\tag{177.H10}
\]

with \(\kappa,u\) odd, \((u,v)=1\), both opposing orientations, and all
literal displacement restrictions.  The coefficient is

\[
 \lambda_N(d)=\omega_L(N)\rho_N(d)A_N(d),
\tag{177.H11}
\]

with the exact squarefree shell and normalization, the canonical
selected-neither/both or no-pair field, both parity branches, profiles,
floors, stars, hard point values, endpoints, and full-line zero extension.
No periodicity, separability, density, variation norm, or cancellation is
assumed for (177.H11).

For a sign \(\sigma\in\{+,-\}\), split the exact hybrid block first by
\(g=(u,n)\), and write \(n=gn_0\), \(u=gu_0\).  Put

\[
 a_x^\sigma=
 \Lambda^\sigma_{\kappa,u,v,gn_0}(t)
 e\!\left(\Psi^\sigma_{\kappa,u,v,gn_0}(t)+{t\over2}\right),
 \qquad
 \phi_x^\sigma=[\sigma\bar v n_0]_{u_0},
\tag{177.H12}
\]

where \(x=(v,n_0,t)\) ranges only over the exact zero-extended literal
support.  The two orientations are combined by treating \(\sigma\) as
part of \(x\).  Define

\[
 B_a=\sum_{\substack{\sigma,x\\\phi_x^\sigma=a}}a_x^\sigma,
 \qquad
 H_\ell=\sum_{\sigma,x}a_x^\sigma e(\ell\phi_x^\sigma/u_0).
\tag{177.H13}
\]

Then the exact \((\kappa,u,g)\)-stratum is

\[
 S_{\kappa,u,g}
 =\sum_{\sigma,x}a_x^\sigma E_{u_0}(\phi_x^\sigma)
 =\sum_{\ell\bmod u_0}c_{u_0}(\ell)H_\ell.
\tag{177.H14}
\]

The claims proved below are:

1. (177.H3)--(177.H8), including both orientations and all divisor
   strata;
2. the exact weighted-\(TT^*\), alias-Parseval, diagonal, collision, and
   incomplete-interval ledgers (177.H24)--(177.H31) below; and
3. a route-scoped obstruction only for the positive or one-saving
   mechanisms named in Section 1.

No assertion is made that the literal amplitudes saturate any displayed
capacity.

## 3. Proof or derivation

### 3.1 Primitive-stratum count and the missing factor

Put \(Y=L/\kappa\).  Literal support gives \(u,v\asymp Y\),
\(n\ll Y\), and \(O(1+\kappa)=O(\kappa)\) fibre sites.  Once
\(g=(u,n)\) is fixed, \(g=u/u_0\) and

\[
 n_0\ll {Y\over g}\asymp u_0.
\tag{177.H15}
\]

Thus (177.H3) follows.  In particular,

\[
 \#\{(\sigma,v,n_0,t)\}_{\kappa,u,g}
 \ll \kappa u u_0\asymp Lu_0,
\tag{177.H16}
\]

where the factor two for \(\sigma\) is harmless.  The lower determinant
cutoff, the original-gcd cutoff \(g<\gamma L\), squarefreeness,
coprimality, displacement inequalities, selectors, and endpoints only
delete or downweight these atoms.  This proves (177.H4).

The count also exposes the exact primitive repetition.  The physical
\(v\)-interval has length \(O(u)=O(gu_0)\), hence at most \(O(g)\)
lifts of a residue modulo \(u_0\); the fibre has \(O(\kappa)\) sites.
Their combined multiplicity is

\[
 \kappa g={\kappa u\over u_0}\asymp {L\over u_0}.
\tag{177.H17}
\]

It is already present in (177.H16).  Collapsing to \(u_0\) while keeping
only one representative of \(v\) would incorrectly delete this factor.
The raw stratum (177.H4) must gain a full \(u_0\) to reach the sufficient
local scale \(L\).  A stratumwise square-root gain gives only
\(L\sqrt{u_0}\).

### 3.2 Exact folding of the original aliases

All of \(g,u_0,u\) are odd.  For \(0\le a<u_0\),

\[
 E_u(ga)=(-1)^{ga}=(-1)^a=E_{u_0}(a).
\tag{177.H18}
\]

Moreover the canonical residue of \(\sigma\bar v n\pmod u\) is
\(g[\sigma\bar v n_0]_{u_0}\).  Apply the two exact DFT expansions to
(177.H18):

\[
\begin{aligned}
 E_u(ga)
 &=\sum_{k\bmod u}c_u(k)e(ka/u_0)\\
 &=\sum_{\ell\bmod u_0}
   \left\{\sum_{j=0}^{g-1}c_u(\ell+ju_0)\right\}
   e(\ell a/u_0),\\
 E_{u_0}(a)
 &=\sum_{\ell\bmod u_0}c_{u_0}(\ell)e(\ell a/u_0).
\end{aligned}
\tag{177.H19}
\]

Uniqueness of the \(u_0\)-DFT proves (177.H5).  Thus the original aliases
must be folded before a primitive-modulus large sieve is applied.  In
particular, original aliases congruent modulo \(u_0\) are not independent
frequencies.

This also restores every imprimitive case.  For an original alias \(k\),

\[
 {u\over(kn,u)}
 ={u_0\over(k,u_0)}
 ={u_0\over(\ell,u_0)}=q,
 \qquad \ell\equiv k\pmod{u_0},
\tag{177.H20}
\]

because \((n_0,u_0)=1\).  The original \(k=0\) term is only one member
of the fold into the primitive zero alias; the whole fold has coefficient

\[
 c_{u_0}(0)=1/u_0.
\tag{177.H21}
\]

Also, since \(g\) is odd,

\[
 {u\pm1\over2}\equiv {u_0\pm1\over2}\pmod{u_0}.
\tag{177.H22}
\]

Hence the original near-half aliases fold to the primitive near-half
aliases; they do not disappear under conductor reduction.

### 3.3 Reduced alias-conductor mass and the target-safe packet

For odd \(m\),

\[
 |c_m(k)|={1\over m|\cos(\pi k/m)|}.
\tag{177.H23}
\]

Fix \(q\mid u_0\).  The aliases of exact conductor \(q\) are uniquely

\[
 \ell={u_0\over q}a\pmod{u_0},\qquad
 a\bmod q,\qquad (a,q)=1,
\]

with the unique zero alias when \(q=1\).  Therefore the reciprocal-cosine
harmonic sum gives

\[
\begin{aligned}
 \sum_{u_0/(\ell,u_0)=q}|c_{u_0}(\ell)|
 &= {1\over u_0}
    \sum_{\substack{a\bmod q\\(a,q)=1}}
       {1\over|\cos(\pi a/q)|}\\
 &\ll {q\over u_0}\log(2q),
\end{aligned}
\tag{177.H24}
\]

which proves (177.H7).  The reduced near-half values
\(a=(q\pm1)/2\) are coprime to odd \(q\), and each has
\(|c_{u_0}|\asymp q/u_0\).  For \(q=u_0\), these are the mandatory
constant-size aliases.  More explicitly,

\[
 e\!\left({(u_0\pm1)a\over2u_0}\right)
 =(-1)^a e\!\left(\pm{a\over2u_0}\right),
\tag{177.H25}
\]

so the main aliases are the physical sawtooth times a slowly varying
factor, not errors.

By (177.H4), \(|H_\ell|\ll Lu_0X^\eta\).  Hence the total positive
capacity of a fixed exact-conductor packet is

\[
 \sum_{u_0/(\ell,u_0)=q}|c_{u_0}(\ell)H_\ell|
 \ll Lq\log(2q)X^\eta.
\tag{177.H26}
\]

For \(P=(\log X)^A\), sum (177.H26) over \(q\le P\), over
\(u_0\mid u\), and then over supported \(u\) and \(\kappa\).  For fixed
\((\kappa,u)\),

\[
 \sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q\le P}}
 Lq\log(2q)
 \ll LP\log(2P)\tau(u)^2.
\tag{177.H27}
\]

Since there are \(O(L/\kappa)\) supported \(u\)'s,

\[
 \sum_{\kappa<\delta L}\sum_{u\asymp L/\kappa}
 LP\log(2P)\tau(u)^2X^\eta
 \ll L^2X^\varepsilon
\tag{177.H28}
\]

after the usual epsilon rebudgeting.  This proves (177.H8), with both
orientations, every gcd stratum satisfying (177.H10), and all literal
fields.  In particular, every stratum with \(u_0\le P\) is included, but
(177.H8) additionally removes the low-\(q\) imprimitive aliases of large
\(u_0\).

If one now grants a square-root saving \(q^{1/2}\) for every high-\(q\)
reciprocal sum, (177.H26) becomes only

\[
 L\sqrt q\log(2q)X^\eta.
\tag{177.H29}
\]

Thus a single reciprocal saving is quantitatively insufficient.  A full
factor \(q\), or an equivalent signed average across the retained labels,
is necessary for this positive fixed-conductor ledger.

### 3.4 Exact alias energy, diagonal, and off-diagonal restoration

From (177.H13), exact Parseval gives

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{a\bmod u_0}|B_a|^2
 =u_0\!\sum_{\substack{\sigma,x,\sigma',y\\
          \phi_x^\sigma=\phi_y^{\sigma'}}}
 a_x^\sigma\overline{a_y^{\sigma'}}.
\tag{177.H30}
\]

There are two incompatible \(TT^*\) choices.

First, keeping the exact rank-one alias matrix
\(c_{u_0}(\ell)\overline{c_{u_0}(\ell')}\) gives

\[
 \sum_{\ell,\ell'}c_{u_0}(\ell)\overline{c_{u_0}(\ell')}
 H_\ell\overline{H_{\ell'}}
 =\left|\sum_aE_{u_0}(a)B_a\right|^2
 =|S_{\kappa,u,g}|^2.
\tag{177.H31}
\]

This is exact but is the original physical block squared; it supplies no
estimate.

Second, alias Cauchy uses \(\|c_{u_0}\|_2=1\) and replaces the rank-one
matrix by the identity:

\[
 |S_{\kappa,u,g}|^2
 \le\sum_\ell|H_\ell|^2
 =u_0\sum_a|B_a|^2.
\tag{177.H32}
\]

The physical self-diagonal in the last expression is exactly

\[
 D=u_0\sum_{\sigma,x}|a_x^\sigma|^2,
 \qquad D\ \hbox{has available capacity}\ \ll Lu_0^2X^\eta.
\tag{177.H33}
\]

Thus any nonnegative diagonal/off-diagonal majorant that retains this
diagonal has square-root capacity \(u_0\sqrt L\,X^\eta\), already above
the required \(L\) when \(u_0>\sqrt L\), even if every off-diagonal is
otherwise disposed of perfectly.  This is a limitation of that positive
certificate, not a lower bound on (177.H32).

Positive treatment of the collisions fully self-returns.  For fixed
\(a\) and one orientation, the congruence

\[
 n_0\equiv \sigma av\pmod{u_0}
\]

allows \(O(1)\) values of \(n_0\) for each of the \(O(u)\) physical
\(v\)'s, and then \(O(\kappa)\) fibre sites.  Hence every residue bucket
has at most \(O(L)\) atoms, also after both orientations are included.
Consequently,

\[
 u_0\sum_a|B_a|^2
 \le u_0\max_a\#B_a\sum_{\sigma,x}|a_x^\sigma|^2
 \ll L^2u_0^2X^\eta,
\tag{177.H34}
\]

whose square root is the raw \(Lu_0\) scale.  A successful alias-energy
argument must therefore prove signed cancellation *inside* the buckets
\(B_a\), or keep and exploit the off-diagonal alias matrix in a way not
equivalent to (177.H31).  Merely naming the large sieve does neither.

### 3.5 Incomplete intervals and reduced-conductor repetitions

The literal \(v\)-range is not one complete primitive residue system.
For an alias of conductor \(q\), put \(h=u_0/q\).  Modulo \(q\), the
\(v\)-interval of length \(O(u)=O(ghq)\) has \(O(gh)\) lifts of a
residue; the \(n_0\)-interval of length \(O(u_0)=O(hq)\) has \(O(h)\)
lifts; and there are \(O(\kappa)\) fibre sites.  Thus a fixed pair of
residues modulo \(q\) can carry

\[
 O(\kappa g h^2)=O\!\left({Lh\over q}\right)
\tag{177.H35}
\]

literal labels before squarefree and endpoint deletion.  Completion to
modulus \(q\) must retain this repetition.  The usual spacing term or
reciprocal orthogonality does not turn the length-\(u\) interval into one
length-\(q\) interval.  Boundary completion adds no saving because the
zero-extended selector-dependent amplitude is not periodic in the lift.

Equation (177.H35) is another form of the same ledger: a product residue
modulo \(q\) has available multiplicity \(O(Lh)=O(Lu_0/q)\), and the
near-half coefficient at that conductor has size \(q/u_0=1/h\).  Their
product returns the \(L\)-scale per product residue and the \(Lq\) scale
over all \(q\) residues in (177.H26).

### 3.6 Two orientations do not pair on literal support

For \(u_0>1\), \(\bar v n_0\) is a nonzero unit.  Therefore

\[
 E_{u_0}(-a)=-E_{u_0}(a)\qquad(a\in(\mathbb Z/u_0\mathbb Z)^\times).
\tag{177.H36}
\]

This exact anchor antisymmetry is not an orientation cancellation.  The
only evident algebraic interchange sends

\[
 (u,v,s,w,+)\longmapsto(v,u,w,s,-),
\tag{177.H37}
\]

which replaces, at both endpoints, the chosen divisor by its complementary
factor.  On the odd--odd branch, the literal divisor window is the upper
near-square window \(\sqrt N\le d\le2\sqrt N\).  If a squarefree
\(N>1\) has a live divisor \(d\) in this window, then its complement
\(N/d<\sqrt N\); equality would make \(N\) a square.  Hence the
complementary divisor is in the zero extension.  On the even--even branch
the complement is even and is not an allowed odd divisor in the first
place.  Thus (177.H37) maps a live term to a nonlive complementary-divisor
term, not to the literal opposite orientation.

Accordingly \(\Lambda^+e(\Psi^+)\) and
\(\Lambda^-e(\Psi^-)\) have no proved matching relation.  Taking their
moduli separately loses a possible new interaction, but simply combining
them in (177.H30) adds cross-orientation collisions and proves no saving.

### 3.7 Restored-power table and remaining literal seams

| Mechanism at fixed \((\kappa,u,u_0)\) or conductor \(q\) | Restored certificate | Target-scale verdict |
|---|---:|---|
| Raw literal count | \(Lu_0\) | Needs full \(u_0\) |
| Exact-conductor alias packet, positive \(\ell^1\) | \(Lq\log(2q)\) | \(q\le(\log X)^A\) is target-safe after global summation |
| One granted reciprocal square-root at conductor \(q\) | \(L\sqrt q\log(2q)\) | Fails for power-size \(q\) |
| Exact weighted alias \(TT^*\) | \(|S_{\kappa,u,g}|^2\) | Tautological physical self-return |
| Alias Cauchy plus a nonnegative physical diagonal | \(u_0\sqrt L\) | Fails for \(u_0>\sqrt L\) even before off-diagonals |
| Alias Cauchy plus positive collision recombination | \(Lu_0\) | Full raw-capacity return |
| Incomplete completion with lift multiplicities restored | repetitions (177.H35) | No hidden conductor gain |
| Rowwise \(t\)-Poisson/B-process with positive dual modes | the \(O(\kappa)\) row length | No change to (177.H4) |
| Separate moduli for the two orientations | same powers, up to a constant | Destroys rather than proves a possible signed interaction |
| Positive squarefree, selector-class, or endpoint recombination | at best \(X^\eta\) times the same capacities | No factor \(q\) or \(u_0\) |

The squarefree openings do not repair the ledger.  Every relevant square
progression has odd modulus and preserves the half-frequency; positive
Möbius recombination costs only divisor factors and supplies no power.
Both two-adic branches leave \(u,g,u_0,q\) odd.  In the even branch the
fixed factor two changes only progression constants and does not alter
(177.H3)--(177.H35).

The selector is a more serious affirmative seam.  Selected and no-pair
rows remain jointly inside \(a_x^\sigma\), and no authorized theorem gives
their variation, Fourier norm, separability in \((v,n_0,t)\), or balance
on a residue bucket.  Treating them as arbitrary coefficients is legal for
a large-sieve upper bound, but then (177.H32)--(177.H34) is the available
ledger.  Splitting selector classes and summing positively has the same
capacity.  Signed selector correlation remains unexcluded.

Finally, the rowwise stationary-mode audit from the inherited fibre kernel
still applies: the \(t\)-phase has \(O(1+2Jn/L)\) half-lattice dual modes,
and absolute recombination returns the \(O(\kappa)\) row length.  For
\(\kappa=O(1)\), there is no internal \(t\)-length to save.  The
near-half reciprocal aliases (177.H25) can also align with a remaining
phase on subfamilies; no modulo-one separation is available.  Stationary
and endpoint modes must therefore remain in the joint coefficient until a
signed theorem is proved.

## 4. First doubtful or unproved step

After removal of the exact packet \(q\le(\log X)^A\), the weakest useful
new local theorem may average over gcd and alias conductors, but it must
prove, uniformly for supported \((\kappa,u)\),

\[
 \left|
 \sum_{u_0\mid u}
 \sum_{\substack{q\mid u_0\\q>(\log X)^A}}
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)=q}}
 c_{u_0}(\ell)H_{\kappa,u,u_0,\ell}
 \right|
 \ll_{A,\delta,\gamma,\varepsilon}LX^\varepsilon,
\tag{177.H38}
\]

with the exact gcd condition, both orientations, and all literal fields in
the definition of \(H\).  A stronger stratumwise theorem would have to
gain a full factor \(q\) on the positive capacity (177.H26).  One
square-root factor is not enough.

The first doubtful step in every audited affirmative implementation is the
claimed second contraction: no proof is supplied that the literal
selector-dependent amplitudes cancel inside the equal-inverse-residue
buckets in (177.H30), that the \(v\)- and \(n_0\)-coefficients separate,
that completion controls the \(g\), \(h\), and \(\kappa\) lift
multiplicities, or that the two orientations match despite the
complementary-divisor support failure in Section 3.6.

The following routes remain genuinely unexcluded:

1. a signed bucket theorem proving cancellation in \(B_a\) before
   Parseval positivity;
2. a bilinear or spectral inverse-residue theorem giving the full factor
   \(q\), possibly only after averaging over \(u_0,q,u,\kappa\);
3. signed cancellation across primitive-gcd strata or across alias
   conductors, rather than the positive sum in (177.H27);
4. a literal selector- and Möbius-sensitive correlation theorem;
5. a signed treatment of stationary dual modes and hard endpoints; or
6. a new two-orientation identity not based on complementary-divisor
   exchange.

No one of these is proved in the authorized context.  The report therefore
does not claim that (177.2) is false.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_residual_coefficient` | **GREEN.** It remains inside \(a_x^\sigma\); no selector norm, density, separability, or smoothing is invented. |
| `exact_low_cross_gcd_complement` | **GREEN.** The range \(\kappa<\delta L\), \(R_{\log}<2\kappa n<R_0\), and \(g=(u,n)<\gamma L\) is retained. |
| `both_opposing_orientations` | **GREEN / open interaction.** Both are combined in (177.H12)--(177.H14).  Their anchors are opposite for \(u_0>1\), but complementary-divisor exchange leaves the upper near-square support, so no cancellation is claimed. |
| `anchor_DFT_and_near_half_alias` | **GREEN.** The exact folding identity is (177.H5); (177.H22)--(177.H25) retain the constant-size primitive near-half aliases. |
| `hybrid_v_n_t_capacity` | **GREEN.** The exact restored count is \(O(Lu_0)\), with the complete \(v,n_0,t\) multiplicity. |
| `primitive_modulus_and_gcd_multiplicity` | **GREEN repair.** The modulus is \(u_0=u/(u,n)\); \(g\) \(v\)-lifts and \(\kappa\) fibre lifts give \(\kappa g=L/u_0\), not one. |
| `k_zero_and_imprimitive_aliases` | **GREEN.** The zero fold has coefficient \(1/u_0\); every imprimitive alias is classified by the exact conductor (177.H20), and its mass is (177.H24). |
| `incomplete_v_interval` | **GREEN obstruction.** Modulo \(q\), the interval repeats \(O(gh)\) times and has literal zero-extended lift-dependent weights; (177.H35) restores the cost. |
| `large_sieve_diagonal_offdiagonal` | **GREEN no-go.** Exact weighted \(TT^*\) is (177.H31); alias Cauchy is (177.H32); the diagonal capacity is (177.H33), and positive collisions return (177.H34). |
| `squarefree_Mobius_progressions` | **GREEN route audit.** Odd square progressions preserve the half-frequency.  Positive opening costs divisor factors only; signed Möbius cancellation remains open. |
| `parity_and_two_adic_branches` | **GREEN.** All conductors are odd; both odd--odd and squarefree even--even branches are retained, and the fixed factor two changes no power. |
| `selected_and_no_pair_rows` | **OPEN literal theorem.** Both remain in the amplitude.  No cancellation between their classes or across selector switches is assumed. |
| `short_cross_gcd_fibres` | **GREEN obstruction.** For \(\kappa=O(1)\), the \(t\)-sum has \(O(1)\) sites, so the required full conductor gain must come from the joint \(v,n_0\), alias, selector, or orientation structure. |
| `stationary_and_dechirped_modes` | **GREEN quarantine.** Positive rowwise stationary-mode recombination restores the fibre length.  The near-half alias is retained, and no generic nonstationarity is assumed. |
| `endpoints_and_zero_extension` | **GREEN.** They only delete atoms in the count-safe packet and remain arbitrary weights in the high-conductor audit.  The zero extension is exactly what blocks complementary-divisor orientation pairing. |
| `false_coefficient_controls` | **GREEN quarantine.** On the same support shadow, choosing artificial \(a_x=E_{u_0}(\phi_x)\) makes (177.H14) fully coherent, while choosing \(a_x=e(-\ell\phi_x/u_0)\) makes a selected near-half alias fully coherent.  These dechirped arrays prove only that coefficient-uniform support/energy large sieves cannot give the missing factor; they are not literal K17a lower bounds. |
| `residual_only_owner_scope` | **GREEN.** The safe packet and no-go concern only the Round-177 low-cross-gcd K17a complement. |
| `no_in_round_pivot` | **GREEN.** No K26, scale-chain, product-collar, fixed-shift, or accepted fixed-proportion sector is substituted for the assigned mechanism. |

No numerical experiment, symbolic experiment, web source, or external
theorem was used.

## 6. Dependencies and exact artifacts used

This report used exactly the assigned brief and the permitted context:

1. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/briefs/hybrid_large_sieve_capacity_audit.md`;
2. `protocol.md`;
3. `state/active_campaign.yml`, at graph
   `e3927f0ace0f3d74e9e9f5116a319159e3508838c7f7bd14b086fa851cad82b8`;
4. `strategy/round177_m2_hard_top_t1_residual_k17a_selector_aware_inverse_residue_strategy.md`;
5. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-selector-aware-inverse-residue-gate/barrier_packet.md`;
6. `proofs/kernels/m9_m2_hard_top_t1_residual_k17a_cross_gcd_alternating_fibre_reduction.md`;
7. `rounds/codex-managed/m9-m2-hard-top-t1-residual-k17a-cross-gcd-alternating-fibre-gate/reports/joint_fibre_capacity_hostile_audit.md`;
8. `strategy/round173_selection/k26_actual_symbol_mechanism_audit.md`;
9. `proofs/kernels/m9_m2_hard_top_t1_residual_whole_chain_scale_coboundary_positive_capacity_obstruction.md`; and
10. `proofs/kernels/m9_m2_hard_top_t1_residual_maximal_fejer_dyadic_positive_transform_obstruction.md`.

No unlisted repository research artifact was read.  No shared state,
strategy, packet, candidate, review, control, synthesis, or proof kernel was
edited.

## 7. Recommended state effect

**Retain, and promote after the required independent seam review,** the
exact alias-folding lemma (177.H5), the conductor-mass estimate (177.H7),
and the complete target-safe low-conductor alias packet (177.H8).  The
physical small-primitive-modulus sector \(u_0\le(\log X)^A\) is a
corollary; (177.H8) is the stronger exact transform-sector statement.

**Record a route-scoped no-go** for a single reciprocal square-root saving,
exact alias \(TT^*\) without new signed information, alias Cauchy followed
by nonnegative diagonal/off-diagonal closure, primitive completion without
lift restoration, positive stationary/Möbius/endpoint recombination, and
separate-orientation moduli.  Their restored capacities are those in
Section 3.7.

**Do not promote** the diagonal or collision capacities, stationary counts,
or dechirped controls to literal lower mass.  Do not infer two-orientation
cancellation from (177.H36): the upper near-square window and zero
extension invalidate the complementary-divisor pairing.

Leave the high-conductor complement \(q>(\log X)^A\), the full K17a
target, the complete residual scalar, every other hard-TOP channel, hard
TOP, both BAL scopes, UNBAL, M9--M2, either M1 route or GAR, endpoint
uniformity, M9, both bridges, the quarter theorem, and every exponent owner
open unless a sibling report proves (177.H38).

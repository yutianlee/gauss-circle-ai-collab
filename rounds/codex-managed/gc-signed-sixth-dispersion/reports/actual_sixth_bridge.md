# Round235 actual sixth-band bridge and odd-packet formalization

## 1. Result: a valid conditional bridge, with unconditional paid sectors

Campaign `gc-signed-sixth-dispersion`; round 235; task `actual_sixth_bridge`; role formalizer; selected-context claimant, independently deriving the formulas below but **not** statement-only isolated. Generated 2026-10-12, Asia/Shanghai. Starting graph SHA256 `dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306`. This report is candidate evidence only.

The proposed sixth-order reduction is valid at its stated conditional scope. The actual band has pointwise squarefree-class variance

\[
 V_F(R):=\sum_{d\ {m squarefree}}g_d(R)^2
 \ll_\varepsilon T^\varepsilon X^{-1/2},\qquad
 \int w(R/T)V_F(R)^3dR\ll_\varepsilon T^{47/125+\varepsilon}.
 \tag{1}
\]

This includes every squarefree class and every harmonic allowed by the actual smooth norm band. Accepted finite relative absorption at order six therefore reduces its sixth moment to a one-sided, signed, distinct-six-class integral, with repeat expenditure (1).

The proposed Hankel leading kernel, sign, constant and variable width are correct. For every required smooth dyadic block, with the kernel and width in Section 2,

\[
 F_N(R)=R^{-1/2}S_N(R^2)+E_N(R),\qquad
 \|E_N\|_{\infty,R\asymp T}\ll_\varepsilon T^\varepsilon N^{-1}.
 \tag{2}
\]

In particular, all Hankel and linearization errors cost at most

\[
 M_6(E_N)\ll_\varepsilon T^{1+\varepsilon}N^{-6}.
 \tag{3}
\]

The actual arithmetic S6 hypothesis in the brief implies the required band bound at exponent 193/500. Its interpolation margin into the complete twelfth moment is positive but only about 0.0002018883. No S6 estimate is proved here. Unconditionally, the constant-mean sector, sufficiently small full divisor progressions in **both** character branches, and the hyperbola square correction are paid. The remaining common-center signed sixth correlation is the first gap.

Effort was analytical/algebraic; no numerical asymptotic experiment was run. File reading and hashing were the only local computational operations. Shared exact Wolfram/local controls remain the conductor's responsibility.

## 2. Exact statements and hypotheses

Use the actual fixed nonnegative radial smooth unit-mass rho, real even Schwartz Psi, and smooth nonnegative radius window w specified by the permitted accepted kernels. Fix eta smooth, zero for t<=1, one for t>=2, and 0<=eta<=1. Put

\[
 \gamma=13/125,\quad
 \beta={50\sqrt{1717}-297\over13762},\quad
 X=T^{52/125},\quad Y=T^{99/125},\quad
 \phi(n)=\eta(n/X)-\eta(n/Y).
\]

For sufficiently large real T, 2X<Y; bounded T is covered by enlarged constants. The exact actual band is

\[
 F(R)=\sum_{n\ge1}\phi(n)r_2(n)n^{-3/4}\Psi(\sqrt{n/T})
       \cos(2\pi R\sqrt n-3\pi/4).
 \tag{4}
\]

It has finite norm support X<n<2Y, including both transition strips. Set

\[
 g_d(R)=\sum_{s\ge1}\phi(ds^2)a_{ds^2}(T)
       \cos(2\pi Rs\sqrt d-3\pi/4),\qquad F=\sum_{d\ {m sf}}g_d.
\]

Define E6 as the sum over ordered pairwise distinct squarefree d1,...,d6 of the product of these six g's, and I6=int w(R/T)E6(R)dR. For every fixed 0<delta<1,

\[
 \int w|F^6-E6|\le\delta M_6(F)+C_\delta T^{47/125+\varepsilon},
 \quad (1-\delta)M_6(F)\le I6+C_\delta T^{47/125+\varepsilon}.
 \tag{5}
\]

Also I6>=-C_delta T^(47/125+epsilon) and |I6|<=(1+delta)M6(F)+C_delta T^(47/125+epsilon). Thus M6(F)<<T^(193/500+epsilon), |I6| at that budget, and a one-sided upper bound for I6 at that budget are equivalent, with every assertion quantified for every epsilon>0. This is an upper-bound equivalence, not a small additive approximation to the physical moment.

Choose a fixed smooth dyadic partition sum_N chi(n/N)=1 on n>0, with chi supported in a compact interval [a^2,b^2] subset (0,infinity). Only O(log T) dyadic N intersect the support of phi; they obey cX<=N<=CY. Define F_N by inserting chi(n/N) in (4), A=sqrt(N),

\[
 b_N(u)=\Psi(u/\sqrt T)\phi(u^2)\chi(u^2/N),\qquad
 q_N(s)=s^{-1}b_N(As),
\]
\[
 K_N(v)=\int_0^\infty q_N(s)\sin(2\pi vs)ds,
 \quad H_N(x)={2\sqrt x\over A},\quad
 S_N(x)=\sum_{m\ge1}r_2(m)K_N\left({x-m\over H_N(x)}\right).
 \tag{6}
\]

All q_N have common compact support [a,b] and uniformly bounded derivatives of each fixed order. Thus K_N is real, odd, uniformly Schwartz. Under the e(-u xi) Fourier convention,

\[
 \widehat K_N(\xi)={1\over2i}
 \begin{cases}q_N(\xi),&\xi>0,\\-q_N(-\xi),&\xi<0,\end{cases}
 \qquad \operatorname{supp}\widehat K_N\subset[-b,-a]\cup[a,b].
 \tag{7}
\]

The proposed arithmetic input is the actual inequality

\[
 \int w(\sqrt x/T)|S_N(x)|^6dx
 \ll_\varepsilon T^{2+1/100+\varepsilon}(T/\sqrt N)^3
 \tag{S6}
\]

uniformly for all required N, real T, all radius endpoints and all transition blocks. No constant-width replacement of H_N(x) is included. In this range H_N(x) is comparable to a scale between T^(151/250) and T^(99/125).

## 3. Proof and derivation

### 3.1. Actual band variance and repeated classes

The elementary divisor bound, compact band support, and |Psi|<=1 give, for arbitrarily small fixed eta>0,

\[
 |g_d(R)|\ll T^\eta d^{-3/4}
       \sum_{s\ge\max(1,\sqrt{X/d})}s^{-3/2}
 \ll T^\eta
 \begin{cases}X^{-1/4}d^{-1/2},&d\le X,\\d^{-3/4},&d>X.
 \end{cases}
 \tag{8}
\]

Strict lower endpoints cause no problem if the summation lower limit is enlarged by a fixed comparison constant. Summing the squares over all positive d, an upper bound for the squarefree sum, gives

\[
 V_F\ll T^{2\eta}
 \left(X^{-1/2}\sum_{d\le X}d^{-1}+\sum_{d>X}d^{-3/2}\right)
 \ll_\varepsilon T^\varepsilon X^{-1/2}.
\]

In particular low d are not removed: their high-harmonic lower cutoff supplies the factor X^(-1/4). Since int w=O(T), cubing proves (1), with 1-(3/2)(52/125)=47/125. The accepted finite absorption proof is a real-family algebraic identity and applies to these new g_d directly; its arithmetic estimate for a different class cutoff is not substituted here. In fact the family in this application is finite. Equations (5) follow. For p=6 its explicit accepted constant can be taken as

\[
 C_\delta=719\max\{1,(719/\delta)^2\}.
\]

This collectively pays all equality patterns; it does not presume a pairing model or exact frequency separation.

### 3.2. Uniform block profiles and exact radial Poisson

The derivatives of b_N(As) are uniformly bounded on the fixed s support. For example derivatives of eta(Ns^2/X) occur only where Ns^2/X is in [1,2], which forces N/X to be bounded above and below there. The same observation applies at Y. Psi derivatives are uniform because N<=CY<T for large T; alternatively its Schwartz seminorms suffice. Consequently for each fixed p,k,

\[
 \left\|\left({d\over du}\right)^k[u^{-p}b_N(u)]\right\|_1
 \ll_{p,k} A^{1-p-k}.
 \tag{9}
\]

The radial function f(z)=|z|^(-3/2)b_N(|z|)cos(2pi R|z|-3pi/4), zero near zero, is smooth compactly supported. Exact two-dimensional Poisson, followed by the angular J0 identity, yields

\[
 F_N(R)=\widehat f(0)+\sum_{m\ge1}r_2(m)\widehat f(\sqrt m),
\]
\[
 \widehat f(v)=2\pi\int_0^\infty
 u^{-1/2}b_N(u)\cos(2\pi Ru-3\pi/4)J_0(2\pi vu)du.
 \tag{10}
\]

There is no primal zero mode; its value is zero by support. The dual zero mode is present and, by two integrations by parts and (9),

\[
 |\widehat f(0)|\ll R^{-2}A^{-3/2}.
 \tag{11}
\]

Use the two-term positive-real order-zero Bessel expansion, as explicitly established/audited in the permitted blind Hankel report:

\[
 J_0(2\pi vu)={\cos(2\pi vu-\pi/4)\over\pi\sqrt{vu}}
 +{\sin(2\pi vu-\pi/4)\over16\pi^2(vu)^{3/2}}
 +O((vu)^{-5/2}).
 \tag{12}
\]

It is used for v>=1 and u~A>=1. Put

\[
 C_N(t)=\int s^{-1}b_N(As)\cos(2\pi ts)ds,
\]
\[
 C_{2,N}(t)=\int s^{-2}b_N(As)\cos(2\pi ts)ds,
 \quad S_{2,N}(t)=\int s^{-2}b_N(As)\sin(2\pi ts)ds.
\]

All four profiles K_N,C_N,C2_N,S2_N are uniformly Schwartz. The exact trigonometric products are

\[
 2\cos(2\pi Ru-3\pi/4)\cos(2\pi vu-\pi/4)
 =\sin(2\pi(R-v)u)-\cos(2\pi(R+v)u),
\]
\[
 2\cos(2\pi Ru-3\pi/4)\sin(2\pi vu-\pi/4)
 =\cos(2\pi(R-v)u)-\sin(2\pi(R+v)u).
\]

Therefore

\[
 \begin{split}
 \widehat f(v)={}&v^{-1/2}
 [K_N(A(R-v))-C_N(A(R+v))]\\
 &+{v^{-3/2}\over16\pi A}
 [C_{2,N}(A(R-v))-S_{2,N}(A(R+v))]+\mathcal R_v,
 \end{split}
 \tag{13}
\]

with |mathcal R_v|<<v^(-5/2)A^(-2). The full remainder is summable:

\[
 \sum_{m\ge1}r_2(m)|\mathcal R_{\sqrt m}|
 \ll A^{-2}\sum_{z\in\mathbb Z^2\setminus\{0\}}|z|^{-5/2}
 \ll A^{-2}.
 \tag{14}
\]

The order |z|^(-3/2) left by a one-term expansion is not absolutely summable in two dimensions. Its replacement by (14) is why the second term in (12) is mandatory here.

### 3.3. Full dual tails and the paid linearization

For fixed sufficiently large L and q=1/2 or 3/2, the elementary shifted-integer-grid estimate gives

\[
 \sum_{m\ge1}r_2(m)m^{-q/2}(1+A|R-\sqrt m|)^{-L}
 \ll_\varepsilon T^\varepsilon R^{-q}(1+R/A).
 \tag{15}
\]

Indeed on R/2<=sqrt(m)<=2R one has |R-sqrt(m)|>=|R^2-m|/(3R), and sum_j(1+lambda|j-x|)^(-L)<<1+lambda^(-1), uniformly for every real x. Outside that central region, the low part costs at most A^(-L)R^(2-q-L+epsilon); the **entire** high part m>4R^2 has the same bound by a convergent series. The sum phase R+sqrt(m) has this same tail bound with no central exception. This proves (15), justifies absolute summation in (13), and retains every dual norm.

The second Bessel contribution thus costs

\[
 \ll_\varepsilon T^\varepsilon A^{-1}R^{-3/2}(1+R/A).
 \tag{16}
\]

The leading sum phase is O_L(A^(-L)R^(3/2-L+epsilon)); because A is at least a fixed positive power of T, this can be O(T^(-B)) for any prescribed B by choosing L.

For the leading difference phase put x=R^2, v=sqrt(m),

\[
 t=A(R-v),\qquad u={A(x-m)\over2R}
       =t-{t^2\over2AR}={x-m\over H_N(x)}.
 \tag{17}
\]

On R/2<=v<=2R, u and t have the same sign and comparable absolute values, and the whole segment between them has this property. Uniform Schwartz bounds and the mean-value theorem imply

\[
 |K_N(t)-K_N(u)|\ll_L {|t|^2\over AR}(1+|t|)^{-L},
\]
\[
 |v^{-1/2}-R^{-1/2}|\ll R^{-3/2}A^{-1}|t|.
\]

Summing against r2(m) by the same shifted-grid estimate shows that replacing v^(-1/2)K_N(t) by R^(-1/2)K_N(u) costs

\[
 \ll_\varepsilon T^\varepsilon R^{-3/2}A^{-1}(1+R/A).
 \tag{18}
\]

The old and new leading expressions outside R/2<=v<=2R each cost O_L(A^(-L)R^(3/2-L+epsilon)). For the new high tail use |u|~Am/R, so its sum is bounded by R^(-1/2)(R/A)^L sum_(m>4R^2)m^(-L+epsilon), exactly the asserted bound. The new low tail uses |u|>>AR and O(R^(2+epsilon)) terms. Thus the linearized S_N still contains all m>=1, with no hard deletion around x.

Combining (11), (14), (16), (18) and the tails gives the more informative version of (2):

\[
 |E_N(R)|\ll_\varepsilon T^\varepsilon\left[
 N^{-1}+T^{-3/2}N^{-1/2}+T^{-1/2}N^{-1}
 +T^{-2}N^{-3/4}\right]+O_B(T^{-B}).
 \tag{19}
\]

Since N<=CY<T and N>=cX>1 for large T, N^(-1) dominates. There is no freezing of H_N(x): (17) uses exactly 2sqrt(x)/sqrt(N), at every real radius. The sixth-moment costs of the four displayed terms are respectively

\[
 T N^{-6},\quad T^{-8}N^{-3},\quad T^{-2}N^{-6},\quad
 T^{-11}N^{-9/2},
\]

up to T^epsilon. This proves (2)--(3), including all transitions and endpoints. Summed over the band, even the largest error budget is T X^(-6)=T^(-187/125), up to epsilon and harmless logarithms.

### 3.4. Actual S6 implication and complete expenditure

The exact Jacobian and leading amplitude give

\[
 \int w(R/T)|R^{-1/2}S_N(R^2)|^6dR
 ={1\over2}\int w(\sqrt x/T)x^{-2}|S_N(x)|^6dx.
 \tag{20}
\]

Thus (S6) implies

\[
 M_6(F_N)\ll_\varepsilon
 T^{1+1/100+\varepsilon}N^{-3/2}+T^{1+\varepsilon}N^{-6}.
\]

The finite norm inequality, or Minkowski and a geometric dyadic sum, proves

\[
 M_6(F)\ll_\varepsilon T^{1+1/100+\varepsilon}X^{-3/2}
 =T^{193/500+\varepsilon},
\]

because 47/125+1/100=193/500. The exact decomposition is B_T=L+F+H with coefficients 1-eta(n/X), phi(n), eta(n/Y), respectively. The high complement contains the full infinite Schwartz tail. Its inherited, independently proved actual Hankel ceiling is ||H||_infinity<<T^epsilon sqrt(T/Y)=T^(gamma+epsilon), and the low complement has the absolute coefficient ceiling ||L||_infinity<<X^(1/4+epsilon)=T^(gamma+epsilon).

The accepted coefficient-uniform distribution mechanism applies to these fixed smooth coefficient vectors. Layer cake, including all levels below one, gives

\[
 M_{12}(L)+M_{12}(H)
 \ll T^\varepsilon[T+T^{10\gamma}+T^{1+20\gamma/13}]
 \ll T^{29/25+\varepsilon}.
 \tag{21}
\]

The full actual B_T ceiling from the qualified accepted pointwise input, together with this **exact** three-piece identity, gives ||F||_infinity<<T^(beta+epsilon), since gamma<beta. This does not invoke a pointwise ceiling for arbitrary coefficient masks.

Consequently

\[
 M_{12}(F)\le\|F\|_\infty^6M_6(F)
 \ll T^{6\beta+193/500+\varepsilon}.
\]

The exact strict margin is

\[
 {29\over25}-6\beta-{193\over500}
 ={3108447-75000\sqrt{1717}\over3440500}>0.
 \tag{22}
\]

For a wholly rational sign check, beta<129/1000 is equivalent to 25000sqrt(1717)<1036149. Both sides are positive, and

\[
 1036149^2-1717\cdot25000^2=479750201>0.
\]

Then 6beta+193/500<774/1000+386/1000=29/25. The margin's approximate size is diagnostic only; the exact square comparison proves positivity. Epsilon allocations must be made after fixing a requested output epsilon, and sufficiently small compared with this fixed margin where needed.

Combining (21) with the physical twelfth-norm inequality pays every mixed contribution and gives the complete conditional exponent 29/25. The accepted complete reconstruction and Jacobian produce the sharp twelfth moment exponent 102/25 in the squared-radius variable: T^(7+29/25)=T^(204/25), whereas the smoothing contribution is T^8 and is smaller. Inclusive-count persistence then yields the **conditional fixed-order** pointwise exponent (102/25)/13=102/325. No unbounded-order moment family, quarter exponent, or M1/M2/GAR closure follows.

### 3.5. Unconditional arithmetic sectors and their exact scope

For any fixed x in the window write H=H_N(x), K=K_N. Fourier support (7) gives the exact identities

\[
 \sum_{k\in\mathbb Z}K((x-dk)/H)
 ={H\over d}\sum_{\ell\in\mathbb Z}e(\ell x/d)\widehat K(H\ell/d),
 \tag{23}
\]
\[
 \begin{split}
 \sum_{k\in\mathbb Z}\chi_4(k)K((x-dk)/H)
 ={H\over2id}\bigg[&\sum_\ell e((\ell+1/4)x/d)\widehat K(H(\ell+1/4)/d)\\
 -&\sum_\ell e((\ell-1/4)x/d)\widehat K(H(\ell-1/4)/d)\bigg].
 \end{split}
 \tag{24}
\]

Here chi4(k)=sin(pi k/2) for integer k, including its standard extension to negative k. Formula (23) vanishes if d<H/b; formula (24) vanishes if d<H/(4b). The zero frequency in (23) also vanishes since Khat(0)=0. These are pointwise identities for the actual variable H, with no center averaging.

For positive k only, the missing nonpositive terms are at most

\[
 C_L(H/x)^L(1+x/d).
 \tag{25}
\]

Summing (25) over d<=cH remains smaller than T^(-B) for every chosen B after increasing L, since x/H~T sqrt(N) is a fixed positive power of T. The same applies to the twisted branch by |chi4|<=1.

The exact hyperbola identity, with the square counted once, is

\[
 r_2(m)=4\sum_{d\mid m,\ d^2\le m}[\chi_4(d)+\chi_4(m/d)]
       -4\mathbf1_{m=s^2}\chi_4(s).
 \tag{26}
\]

For any fixed c<1/(4b), the sub-sector d<=cH has d^2<<x throughout this band, because H/T~N^(-1/2) tends to zero. Extending its constraint k>=d to all positive k changes only m=dk<=d^2<<x. The total of these excluded terms is O_L(H^2(H/x)^L), again rapidly small. Equations (23)--(26) therefore rigorously pay the small-d hyperbola sector in **both** branches, including the moving boundary. A smooth cutoff supported in d<=cH works as well, because each completed progression vanishes separately.

The square correction is bounded by

\[
 \sum_{s\ge1}|K((x-s^2)/H)|\ll_L1+H/\sqrt x\ll1.
 \tag{27}
\]

For s~sqrt(x), use |x-s^2|>>sqrt(x)|s-sqrt(x)| and the shifted-grid bound; the low/high tails are convergent Schwartz tails. It contributes O(T^(-1/2)) after the R^(-1/2) factor in (2), hence only O(T^(-2)) to its sixth moment. This is an unconditional paid sector, not proof of S6 for the remaining hyperbola sums.

Similarly, replacing r2(m) by a constant c0 yields a rapidly small positive-integer packet: the full-integer sum vanishes by (23) at d=1 and H>b, and (25) owns the omitted m<=0 tail. This exact mean control must not be confused with cancellation of actual arithmetic fluctuations.

The surviving fractions in (23) are ell/d and those in (24) are (ell+/-1/4)/d. A signed sixth expansion has a **single** phase exp(2pi i x Omega) with Omega the signed sum of six such fractions. On a common x interval of length comparable to T^2 its natural resolution is T^(-2), not H^(-1), T^(-1), or six independent resolutions. For genuinely smooth amplitudes whose jth derivatives cost O(T^(-2j)), integration by parts yields the usual factor (1+T^2|Omega|)^(-L). Since H'(x)=H/(2x), smooth Fourier-profile amplitudes have precisely this derivative scale. This observation does not smooth the sharp moving hyperbola cutoffs for free: outside the explicitly paid small-d sector, all such cutoff errors remain part of the unproved arithmetic owner.

The unconditional absolute packet bound is only |S_N(x)|<<T^epsilon(1+H). It follows directly from the same shifted-grid/tail argument. Its sixth integral costs at most T^(2+epsilon)H^6, whereas S6 asks for T^(2+1/100+epsilon)H^3. This is an upper-bound-method deficit, not a lower bound or a refutation of S6.

## 4. First doubtful or unproved step

The first missing step is (S6), or equivalently at the physical band level the one-sided signed I6 estimate in (5) at 193/500. The algebraic reduction, Poisson formula, two-term Bessel summation, moving-width linearization and error expenditure above do not supply it.

After the unconditional sectors in Section 3.5 are removed, the exact common-center sixth correlation over d>=cH still needs cancellation between different reciprocal-fraction tuples with both chi4 branches and every moving cutoff retained. A modulus-density approximation or a product of independent averages does not follow from these identities. A near-frequency absolute majorant is a stronger new assertion and has not been proved. Returning to the original F_N through the inverse transform is only an equivalence and supplies no gain.

The accepted qualified Li--Yang pointwise input is used only for the band ceiling and conditional interpolation. The old complete baseline and prior absolute-cumulant obstruction remain intact. This report neither challenges the Round234 absolute certificate nor imports it as a sixth-order lower bound.

## 5. Control tests and outcomes

| Required control | Outcome and exact scope |
|---|---|
| actual_band_and_complements | Pass analytically: exact B=L+F+H, all transitions and the entire high-norm Schwartz tail retained; (21) pays both complements at 29/25. |
| sixth_variance_and_repeats | Pass analytically: (8) retains low-d high harmonics; variance costs 47/125, and accepted finite absorption applies directly to this finite real family. |
| hankel_phase_and_two_term_error | Pass analytically: the two product identities give positive difference sine and coefficient 1; correction is 1/(16pi A). One-term absolute remainder would diverge; (14) converges. At exact m=R^2 the leading K(0)=0 but C2_N(0) in the correction need not vanish. |
| moving_width_and_endpoints | Pass analytically: exact H=2sqrt(x)/sqrt(N) in (17); no width freezing. Shifted-grid bounds are uniform in fractional parts. Derivative support pays both norm transitions. |
| two_character_branches | Pass for identities/paid small sector: (24), (26) retain chi4(d), chi4(k), and the square correction. No full-branch S6 bound is claimed. |
| signed_fraction_resolution | Pass as normalization audit: surviving phases share x~T^2, so the near-relation scale is T^(-2). The desired signed dispersion bound at this scale remains open. |
| constant_mean_and_absolute_control | Constant full-integer packet is exactly zero, positive packet rapidly small. Absolute bound gives H^6 instead of H^3, so it does not reach S6. Replacing K by |K| generally restores a nonzero mean of size H. An even band-limited kernel with a Fourier gap could still have zero mean, but loses K(0)=0; thus oddness and mean-zero must not be conflated. |
| complete_exponent_margin | Exact positive expression (22); rational square difference 479750201>0. Fixed p12 restoration gives only conditional 102/325. |
| wolfram_local_exact | Not performed by this subagent, per brief. Conductor should independently reproduce (22), the square difference, 47/125+1/100, error powers, the two trig identities, and the Fourier shifts in (24). No unobserved control success is asserted. |
| blind_isolation | Selected-context isolation preserved; no sibling report read. This report is not itself the campaign's statement-only blind proof. |
| history_preservation | Only this assigned report was written. No shared state, synthesis, proof draft, legacy path, or predecessor artifact was edited. |

The arbitrary-coefficient control is structural: replacing r2 by unrelated coefficients invalidates the exact two-dimensional radial Poisson identity and the divisor/character progressions. No arithmetic S6 theorem for such a surrogate is inferred. Conversely, the finite relative-absorption identity is coefficient-uniform, and is used only for its algebraic conclusion; it cannot create arithmetic cancellation.

## 6. Dependencies and exact artifacts used

All file hashes are SHA256 of the exact bytes read. The live campaign hash is a snapshot and may legitimately change under conductor status updates after this read.

| File | SHA256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| state/proof_obligations.yml | dd743db27ed8eaac685d23dd2f92da743dd2d1742c2f150ddecf802dbbca5306 |
| state/active_campaign.yml | 8e1e7cdf33fea4338bc8fcc154536ba8df576a3ea359054f6c3a32617788db92 |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/actual_sixth_bridge.md | d99ae8e265175c581f9242a8ba3539f07e46a02c0d9d1357cd61d30d6919e723 |
| rounds/codex-managed/gc-signed-sixth-dispersion/briefs/actual_interface.md | e665ea9cd651c7c6346279d90e89ca7b476bc9f39f757becc9f788abc1a4ecfa |
| proofs/kernels/gc_complete_square_root_large_values_moment_bound.md | 942083c3a124ffb8320f306eb767de376ae45e2b3b12175ffe9c5b70feeb5212 |
| proofs/kernels/gc_complete_fixed_even_moment_distinct_absorption.md | b1097aa498d0430d5bbe81fb0b8927cc4ffdf278ce838b3ef38f555bc75c31d0 |
| strategy/round231_balanced_cancellation/conductor_combined_owner.md | 9f5d9a31c0624e7ee97a21bcdfa2e638154fa313cc45cbab198856222366d76b |
| strategy/round231_balanced_cancellation/reports/blind_hankel_tail.md | 03b30638eb6da7242343731ac03b425e2f09e16749f73685adc343a357cd01d5 |
| rounds/codex-managed/gc-connected-cumulant-test/synthesis.md | fc90f9a04a4d851f7dcaa05f90771ab8762f3987b97bc23a6add445006e55213 |

The relevant graph statuses were directly checked: GC-complete-square-root-large-values-moment-bound, GC-complete-distinct-radical-twelfth-reduction, and GC-complete-fixed-even-moment-distinct-absorption are proved_internal; GC-target is open. The smooth high-norm ledger remains previously reviewed evidence, not a newly graph-promoted result in this report.

No unlisted local context, sibling report, source card or historical file was read. The permitted blind Hankel report supplies the explicitly stated positive-real J0 expansion and its source audit: [DLMF 10.9.1](https://dlmf.nist.gov/10.9.E1), [10.17.3](https://dlmf.nist.gov/10.17.E3), and [10.17(iii)](https://dlmf.nist.gov/10.17#iii), fixed real order zero and positive argument. Those pages were not freshly opened by this subagent; this is inherited primary-source qualification, not a claim of a fresh external source audit. All new profile, summation, linearization and exponent estimates are derived above from the exact displayed specialization.

## 7. Recommended state effect

**Retain** the rigorously derived bridge and paid-sector lemmas as evidence for conductor-selected nonauthor review. A narrow promotion of the actual sixth-band variance/absorption specialization and the fully paid odd-packet representation could be considered only after the required seam controls and mechanically valid State Patch; neither is itself a complete moment gain.

**No change** to the complete moment or pointwise claims, M1/M2/GAR/endpoints, or quarter target. Keep S6 and the signed distinct-six target explicitly open. Stop after this report; no successor round is proposed or launched.

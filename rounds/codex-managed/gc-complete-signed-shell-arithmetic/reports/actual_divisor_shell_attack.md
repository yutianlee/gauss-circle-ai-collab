# Round 206: actual divisor and centered six-shift attack

Campaign: `gc-complete-signed-shell-arithmetic`. Task: `actual_divisor_shell_attack`. Role: discovery; selected context, not blind. Date: 2026-09-26. Starting graph SHA-256: `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`. Candidate evidence only. Effort: 100 percent analytical/algebraic; no numerical experiment or new external theorem.

## 1. Result: complete arithmetic attempt, with a scoped absolute-placement no-go

Opening the actual centered sixth moment gives a complete six-shift correlation problem. Every stratum with at most three distinct shifts is already bounded by the requested variance-scale order. The first unresolved part is the **joint signed sum of the four-, five-, and six-distinct-shift strata**, including their repeated coordinates and local congruence densities.

The exact divisor identity, followed by an exact hyperbola split, reduces each coefficient to \(O(\sqrt X)\) periodic atoms with explicit quotient-character signs and moving thresholds. Applying weighted CRT to every six-atom correlation gives an exact signed local-density main term plus an error bounded by

\[
 O_\epsilon(X^{3+\epsilon}H^6),\qquad H\asymp T/\sqrt N,
 \tag{A1}
\]

where the desired sixth-moment bound is \(X^{1+\epsilon}H^3\), \(X=T^2\). Opening all divisors without the hyperbola split instead gives the still worse \(X^{6+\epsilon}H^6\) endpoint-error ledger. Neither error estimate certifies the desired cancellation. These are upper-bound costs of the specified placement, not lower bounds for the actual error.

There is also a rigorous no-go for taking the termwise absolute value of the centered six-shift expansion. Since \(r_2(n)\in4\mathbb Z_{\ge0}\),

\[
 |r_2(n)-\pi|\ge4-\pi>0.
\]

Consequently that absolute expansion has size at least \(cXH^6\), exceeding \(XH^3\) by \(H^3\). Section3 also compares it with the weaker sufficient sixth-moment threshold (A4'), which permits a scale-dependent loss \(\Lambda\) over \(XH^3\): the absolute cost still exceeds that threshold by at least a factor \(T^{136/125}\), before epsilon losses. This does **not** lower-bound the signed sixth moment or refute the frozen twelfth-moment target.

The full middle-band twelfth moment therefore retains its existing bound

\[
 \int_I\left|\sum_{T^{52/125}<N=2^j<T^{99/125}}S_N(R)\right|^{12}dR
 \ll_\epsilon T^{10\beta+\epsilon},\qquad
 \beta=2\theta_{LY}-\tfrac12.
 \tag{A2}
\]

No complete moment power or pointwise exponent is improved.

## 2. Exact statement and hypotheses

Use exactly the actual mollifier transform and fixed smooth partition in the reviewed Round205 interface. Thus

\[
 L_{N,T}(z)=\int_0^\infty r^{-1}\Psi(r/\sqrt T)v(r^2/N)
                  \sin(2\pi zr)\,dr,
 \quad S_N(R)=\sum_{m\ge1}r_2(m)m^{-1/4}L_{N,T}(R-\sqrt m),
\]

where \(v(t)=\phi(t/2)-\phi(t)\), \(\operatorname{supp}v\subset[1,4]\), and \(\Psi(0)=1\). Let \(T\ge2\) be real, \(I=[T/\sqrt2,\sqrt3T]\), \(X=T^2\), \(J=[X/2,3X]\), and let \(N\) run over **every** dyadic scale strictly between \(T^{52/125}\) and \(T^{99/125}\). Equality at either boundary belongs to the estimated outer band, as in Round205.

Define the real odd Schwartz filter

\[
 F_{N,T}(u)=-\int_1^2t^{-1}\Psi(\sqrt{N/T}\,t)v(t^2)
                   \sin(2\pi tu)\,dt,
 \quad h(x)=2\sqrt x/\sqrt N,
\]

and

\[
 E_N(x)=\sum_{m\ge1}(r_2(m)-\pi)F_{N,T}((m-x)/h(x)).
 \tag{A3}
\]

Its Fourier support is contained in \([-2,-1]\cup[1,2]\). All Schwartz seminorms are uniform in the middle band. Set \(H=2\sqrt{3X}/\sqrt N\); then \(H/\sqrt6\le h(x)\le H\) on \(J\). In particular

\[
 H\asymp T/\sqrt N,\qquad
 X^{151/500}\ll H\ll X^{99/250}.
\]

Constants may depend on fixed filters, fixed window endpoints and epsilon. No uniformity in arbitrary filters, growing moments, or a shrinking window is asserted. The prospective sufficient input is

\[
 \int_J |E_N(x)|^6dx\ll_\epsilon X^{1+\epsilon}H^3
 \quad\hbox{uniformly over the complete middle range}.
 \tag{A4}
\]

This report does not assume (A4). It is stronger than the sixth-moment input actually sufficient through the available suprema. With

\[
 W_0=\min\{N^{1/4},T^\beta,T^{1/2}N^{-1/2}\},\qquad
 \Lambda=T^{4/25}N^{3/2}W_0^{-6},
\]

the weaker bound

\[
 \int_J|E_N(x)|^6dx
 \ll_\epsilon T^{129/25+\epsilon}W_0^{-6}
 \asymp T^\epsilon\Lambda XH^3
 \tag{A4'}
\]

also suffices, uniformly over all middle blocks. In particular, \(\Lambda\ge T^{4/25}\), so a uniform loss \(X^{2/25}\) over the variance sixth scale is allowed. Failure to establish (A4), or failure of a method aimed at it, is not a refutation of the frozen twelfth-moment target.

## 3. Derivation and complete power ledger

### Exact curved-shell, mean and tail costs

For \(x=R^2\), \(m=x+h(x)u\), and \(m\asymp x\), Taylor's theorem gives

\[
 \sqrt N(R-\sqrt m)=-u+O(u^2/(R\sqrt N)),\qquad
 m^{-1/4}=R^{-1/2}\{1+O(|u|/(R\sqrt N))\}.
\]

On \(|m-x|\le x/2\), the two filter arguments and all intermediate arguments are comparable in modulus. The mean-value theorem with uniform Schwartz decay therefore bounds their weighted difference by

\[
 C_A R^{-1/2}(R\sqrt N)^{-1}(|u|+u^2)(1+|u|)^{-A}.
\]

The divisor envelope and \(h\gg1\) show that summing this difference costs \(O_\epsilon(T^{-1/2+\epsilon}N^{-1})\). For \(|m-x|>x/2\), the curved radial argument is bounded below by a fixed multiple of \(R\sqrt N\) until \(m\gg X\), and then by a fixed multiple of \(\sqrt{Nm}\). Arbitrarily high fixed Schwartz decay sums both infinite tails to \(O_K(T^{-K})\). The additive filter tail is treated in the same way; it is not made compact by declaration.

Since \(h>2\) for large \(T\), Poisson summation for the *constant-density* sequence gives exactly

\[
 \sum_{m\in\mathbb Z}F_{N,T}((m-x)/h)=0.
 \tag{A5}
\]

Indeed every sampled Fourier argument \(h\ell\) misses the support, including \(\ell=0\). The omitted nonpositive integers lie a distance \(\gg X/h\) from the center and contribute \(O_K(T^{-K})\). Thus mean subtraction has an explicitly negligible cost, and

\[
 S_N(R)=R^{-1/2}E_N(R^2)
      +O_\epsilon(T^{-1/2+\epsilon}N^{-1})+O_K(T^{-K}).
 \tag{A6}
\]

All assertions hold at real \(R\), including \(R^2\in\mathbb Z\); oddness gives \(L(0)=F(0)=0\). No endpoint is removed.

For later finite divisor manipulations choose a fixed smooth \(0\le\eta\le1\) supported in ([1/4,6]), equal to one on ([1/3,4]), and replace (A3) by

\[
 E_N^\eta(x)=\sum_{m\ge1}(r_2(m)-\pi)\eta(m/X)F_{N,T}((m-x)/h(x)).
\]

Uniformly on \(J\), the difference is \(O_K(X^{-K})\), by the preceding tail bound with a sufficiently high fixed decay order. This localization retains, and explicitly pays, the original infinite tail. The same argument and (A5) show \(\sum_m\eta(m/X)F((m-x)/h)=O_K(X^{-K})\).

### What (A4) would buy, and the currently available analytic bound

Write \(a(m)=r_2(m)-\pi\). Its inclusive partial sum is

\[
 \sum_{1\le m\le y}a(m)=P(y)+\pi\{y\}-1\ll_\epsilon y^{\theta+\epsilon},
 \qquad\theta=\theta_{LY}.
\]

Partial summation against the smooth localized filter has total variation \(O(1)\), uniformly in (x,N). Therefore

\[
 |E_N(x)|\ll_\epsilon X^{\theta+\epsilon},\qquad
 |S_N(R)|\ll_\epsilon T^{\beta+\epsilon}.
 \tag{A7}
\]

This proves the single-block supremum directly from the accepted inclusive pointwise theorem; it does not infer a block supremum by subtracting unrelated blocks.

Since \(dR=dx/(2\sqrt x)\), (A4) and (A6) would yield

\[
 \int_I|S_N|^6dR\ll T^{-4}XH^3
       \ll T^{1+\epsilon}N^{-3/2}.
\]

Combining with (A7) gives

\[
 \int_I|S_N|^{12}dR
 \ll T^{1+6\beta+\epsilon}N^{-3/2}.
 \tag{A8}
\]

Using just (A7), the worst middle scale is the lower boundary. Its exponent is

\[
 1+6\beta-78/125=47/125+6\beta
              <29/25,
\]

because \(\beta<27/208\) implies \(6\beta<81/104<98/125\). Thus a uniform (A4) is sufficient for the whole middle band by Minkowski over \(O(\log T)\) scales, with all cross-block terms covered by the physical norm inequality. This is conditional bookkeeping only.

There is substantial additional slack if the actual original coefficient bound is retained: \(|S_N|\ll_\epsilon N^{1/4+\epsilon}\), by its reviewed equality to \(H_N\) and the original coefficient sum. Combining that bound with the same sixth moment gives \(N^{3/2}\cdot TN^{-3/2}=T\). Thus the variance-scale hypothesis would in fact give

\[
 \int_I|S_N|^{12}dR\ll_\epsilon T^{1+\epsilon}.
 \tag{A8a}
\]

More generally the three legitimate supremum bounds give

\[
 \int_I|S_N|^{12}dR
 \ll_\epsilon W_0^6 T^{-4+\epsilon}\int_J|E_N(x)|^6dx
       +O_\epsilon(T^{-2+\epsilon}).
 \tag{A8b}
\]

The algebraic error here is paid: the sixth power of the error in (A6), integrated and multiplied by \(W_0^6\le N^{3/2}\), is \(O_\epsilon(T^{-2+\epsilon}N^{-9/2})\). Formula (A8b) is the origin of (A4'), whose exponent \(129/25=4+29/25\) retains the Jacobian and amplitude exactly. If \(N=T^\nu\), its allowed loss over \(XH^3\) has exponent

\[
 \log_T\Lambda=
 \frac4{25}+\frac32\nu-
 6\min\{\nu/4,\beta,(1-\nu)/2\}.
 \tag{A8c}
\]

For \(\nu\le4\beta\) it is \(4/25\); for \(4\beta\le\nu\le1-2\beta\) it is \(4/25+3\nu/2-6\beta\); and for \(\nu\ge1-2\beta\) it is \(9\nu/2-71/25\). These are all parts of the present middle range, with no complement omitted. This is the least restrictive sufficient sixth-moment threshold obtained from these suprema and the particular interpolation (A8b); it is not asserted to be necessary for the actual twelfth moment.

For comparison, the actual original block has coefficient energy \(O_\epsilon(N^{-1/2+\epsilon})\). For distinct original indices in ([N,4N]), \(|\sqrt n-\sqrt m|\gg |n-m|/\sqrt N\). Integrating over the real interval \(I\), the sum of absolute off-diagonal kernels in any row is \(O(\sqrt N\log(2N))\), so the elementary mean-square bound is

\[
 \int_I|H_N|^2dR\ll_\epsilon T^{1+\epsilon}N^{-1/2},
\]

as \(\sqrt N\log(2N)\ll T\) throughout this band. The reviewed \(H_N-S_N\) error and (A6) consequently give

\[
 \int_J|E_N|^2dx\ll_\epsilon X^{1+\epsilon}H.
 \tag{A9}
\]

This variance bound does not imply (A4). The valid interpolation, also allowing the elementary original and shell suprema, is only

\[
 \int_J|E_N|^6dx\ll_\epsilon
 X^{1+\epsilon}H
 \min\{H,X^\theta,X^{1/2}H^{-1/2}\}^{4}.
 \tag{A10}
\]

Equivalently, for \(W=W_0\), the sixth shell moment is at most \(T^{1+\epsilon}N^{-1/2}W^4\). The ratio of this available bound to the variance sixth scale \(TN^{-3/2}\) is \(NW^4\). Against the weaker sufficient input (A4'), the ratio is instead

\[
 T^{-4/25}N^{-1/2}W_0^{10}.
\]

It is still a positive power on every middle scale: its exponent is \(2\nu-4/25\) on the first range, \(10\beta-\nu/2-4/25\) on the second, and \(121/25-11\nu/2\) on the third. The first is at least \(84/125\) at the lower boundary; the third approaches \(121/250\) at the upper boundary; the second is larger than \(121/250\). Thus the priced second-moment/supremum interpolation does not establish even (A4'), while remaining only an insufficient upper-bound argument.

The corresponding second-moment interpolation for the twelfth shell moment is \(T^{1+\epsilon}N^{-1/2}W^{10}\). The stronger accepted large-value estimate gives instead

\[
 \int_I|S_N|^{12}dR\ll_\epsilon
 T^{1+\epsilon}+T^\epsilon W^{10}+T^{1+\epsilon}W^{20/13}
 \ll T^{10\beta+\epsilon}.
\]

Here \(\beta(136/13-2)>1\) is the accepted comparison, and all transform errors are smaller. Summing all middle blocks proves the complete retained bound (A2). Its missing saving remains exactly \(10\beta-29/25\), approximately (0.1296635).

### The complete six-shift expansion and target-safe repeated-shift strata

Write \(x=b+u\) with \(b\in\mathbb Z\), \(0\le u<1\). For \(\mathbf k=(k_1,\ldots,k_6)\in\mathbb Z^6\), set

\[
 W_{\mathbf k,u}(b)=\mathbf1_J(b+u)
 \prod_{i=1}^6\eta((b+k_i)/X)
 F_{N,T}((k_i-u)/h(b+u)).
\]

Only positive arguments survive the cutoff. Exact absolute convergence permits the identity

\[
 \int_J|E_N^\eta(x)|^6dx
 =\int_0^1\sum_{\mathbf k\in\mathbb Z^6}\sum_{b\in\mathbb Z}
 W_{\mathbf k,u}(b)\prod_{i=1}^6 a(b+k_i)\,du.
 \tag{A11}
\]

The endpoint indicator in \(W\) retains the partial first and last unit cells. The sixth power is the ordinary power because the filter and coefficients are real.

For a shift pattern with \(q\le3\) distinct values, the divisor envelope bounds the coefficient product by \(X^\epsilon\). Uniform decay gives \(\sum_k(1+|k|/H)^{-A}\ll H\). Summing the \(q\) independent shift values and \(O(X)\) anchors bounds the absolute contribution by \(O_\epsilon(X^{1+\epsilon}H^q)\), hence by \(X^{1+\epsilon}H^3\). There are only finitely many equality patterns. This includes every partition with no singleton, all-equal shifts and every pair-pair-pair arrangement; no Gaussian coefficient or independence claim is used.

The patterns with four or five distinct shifts also contain repetitions, and are **not** discarded by this argument. They stay together with the six-distinct pattern in (A17) below.

### Exact hyperbola opening, local densities, and its endpoint error

Let \(M=\lceil6X\rceil\), \(D=\lfloor\sqrt M\rfloor\), and \(L=\lfloor M/(D+1)\rfloor\). For every positive integer \(n\le M\),

\[
 \frac{r_2(n)}4
 =\sum_{d\le D}\chi_4(d)\mathbf1_{d\mid n}
 +\sum_{\ell\le L}\mathbf1_{n>D\ell}\mathbf1_{\ell\mid n}
                              \chi_4(n/\ell).
 \tag{A12}
\]

The second sum is exactly the complementary divisor range \(d>D\), with \(\ell=n/d\); the strict threshold is correct also when \(n=D\ell\). The quotient-character function is exactly

\[
 \mathbf1_{\ell\mid n}\chi_4(n/\ell)
 =\mathbf1_{n\equiv\ell\ (4\ell)}-
   \mathbf1_{n\equiv3\ell\ (4\ell)}.
 \tag{A13}
\]

Thus even quotient divisors vanish through the actual character, and both odd residue branches remain.

The bounded partial sums of \(\chi_4\) and the elementary identity \(4\sum_{d\ge1}\chi_4(d)/d=\pi\) give

\[
 a(n)=4\sum_{d\le D}\chi_4(d)
       (\mathbf1_{d\mid n}-1/d)
 +4\sum_{\ell\le L}\mathbf1_{n>D\ell}
       (\mathbf1_{n\equiv\ell\ (4\ell)}-
        \mathbf1_{n\equiv3\ell\ (4\ell)})+\delta_D,
 \quad |\delta_D|\ll D^{-1}.
 \tag{A14}
\]

The constant remainder is retained; after complete filtering it is negligible by (A5), but it cannot simply be erased from an individual correlation.

Each of the \(D+L+1=O(\sqrt X)\) atom labels in (A14) is a linear combination of at most two congruence indicators. The small centered atom uses moduli \(d\) and (1), with coefficients \(\chi_4(d)\) and \(-\chi_4(d)/d\); the quotient atom uses two residues modulo \(4\ell\). The constant atom has modulus (1). Factors (4) are retained in the coefficients and affect only a fixed constant.

For a chosen six-atom label tuple, absorb its quotient thresholds \(\mathbf1_{b+k_i>D\ell_i}\) into the weight. For each choice of its at most \(2^6\) residue branches, the CRT congruences are

\[
 b\equiv r_i-k_i\pmod {q_i}\quad(1\le i\le6).
\]

They have density

\[
 \rho(\mathbf q,\mathbf r,\mathbf k)=
 \frac{\mathbf1_{r_i-k_i\equiv r_j-k_j\ (\gcd(q_i,q_j))\ \forall i,j}}
      {\operatorname{lcm}(q_1,\ldots,q_6)}.
 \tag{A15}
\]

When incompatible the correlation is zero exactly. When compatible, weighted summation in the single resulting residue class gives

\[
 \sum_{b\equiv b_0\ (Q)}W(b)
 =Q^{-1}\int_\mathbb R W(y)dy
   +O(\|W\|_\infty+\operatorname{Var}W).
 \tag{A16}
\]

The weight contains at most six hyperbola jumps and two real window endpoint jumps. Its smooth derivative has total integral bounded by \(C_A\prod_i(1+|k_i|/H)^{-A}\): here \(h'(x)=h(x)/(2x)\), cutoff derivatives are \(O(1/X)\), and the differentiated Schwartz factors retain arbitrary decay. Its supremum and every jump have the same product bound. This verifies (A16) uniformly in every modulus, shift, partial unit cell and threshold position.

Equations (A11), (A14)--(A16) are an exact main-term-plus-error expansion. The main term is the sum of **all signed branch coefficients times (A15) times their thresholded weight integrals**. No local density, coincident residue, even modulus, repeated shift or large lcm is deleted. Summing the lawful absolute endpoint-error bounds over \(O(X^3)\) atom tuples, at most \(2^6\) branches, all shifts and \(u\in[0,1]\) gives (A1). If one opens \(r_2\) directly with all \(d\le M\), the \(O(M^6)\) choices give \(X^{6+\epsilon}H^6\). The hyperbola split saves \(X^3\) in this error ledger, but still leaves a factor \(X^2H^3\) beyond (A4).

Centering does not zero these local main terms individually. For example, choose the same odd small-divisor modulus \(d>1\) in all six factors and six distinct shifts congruent modulo \(d\). The complete-residue mean of their centered product is

\[
 d^{-1}(1-d^{-1})^6+(1-d^{-1})d^{-6}>0,
\]

and \(\chi_4(d)^6=1\). This example diagnoses an invalid independence substitution. It does not assert positivity after summing the signed filter weights or the other divisor tuples. Cancellation among the actual local-density terms is still required.

### Rigorous failure of the termwise absolute placement

Here is the uniform nonvanishing and Riemann-sum proof. The fixed smooth function \(v(t^2)/t\) is not identically zero on \([1,2]\): the defining \(\phi\) changes from one to zero, so its dyadic difference cannot vanish everywhere. Its odd Fourier extension is nonzero. Uniqueness of the Fourier transform therefore shows that the limiting sine filter \(F_0\), obtained by replacing \(\Psi\) by \(1\), is nonzero. In particular \(\|F_0\|_1>0\).

Throughout the middle band \(N/T\le T^{-26/125}\to0\). Smoothness of \(\Psi\) on a fixed compact neighborhood of zero gives convergence of the compactly supported amplitudes and all their derivatives. Repeated integration by parts then gives \(F_{N,T}\to F_0\) in every fixed Schwartz seminorm, uniformly over the band. Thus, for all sufficiently large \(T\),

\[
 \|F_{N,T}\|_1\ge c_0>0,\qquad
 \|F_{N,T}\|_1+\|F'_{N,T}\|_1\le C_0.
 \tag{A18}
\]

For each fixed real \(x\in J\), put
\[
 g_x(t)=\eta(t/X)|F_{N,T}((t-x)/h(x))|.
\]
The width \(h(x)\) is kept at its actual value. Its variation as \(x\) changes is not replaced by a fixed width. For this fixed \(x\), variation in the summation variable \(t\) satisfies
\[
 \operatorname{Var}_t(g_x)
 \le \|\eta\|_\infty\|F'_{N,T}\|_1+
       (h(x)/X)\|\eta'\|_\infty\|F_{N,T}\|_1
 \le C.
\]
Absolute value is harmless for bounded variation: its variation is bounded by that of the smooth underlying function.

For any compactly supported BV function \(g\), comparison on each interval \([m,m+1]\) proves
\[
 \left|\sum_{m\in\mathbb Z}g(m)-\int_\mathbb R g(t)\,dt\right|
 \le\operatorname{Var}(g).
\]
Indeed the error on that interval is at most its variation, and the interval variations sum to the total. Applying this with \(g_x\) gives a uniform error \(O(1)\), also at integer or arbitrarily close-to-integer \(x\).

The cutoff equals one a distance at least \(cX\) on both sides of every \(x\in J\). Substitution \(t=x+h(x)u\) and the Schwartz tail therefore give, for every fixed large \(A\),
\[
 \int g_x(t)\,dt
 =h(x)\|F_{N,T}\|_1+
       O_A\{h(x)(X/h(x))^{-A}\}.
\]
Because \(h(x)\le H\ll X^{99/250}\) and \(h(x)\gg X^{151/500}\), the tail error is \(o(h(x))\) and the Riemann-sum error \(O(1)\) is also \(o(h(x))\), uniformly. The cutoff is supported on positive \(t\). We have therefore proved

\[
 \sum_{m\ge1}\eta(m/X)|F_{N,T}((m-x)/h(x))|\ge c h(x)
\]

for every \(x\in J\) and sufficiently large \(T\); the cutoff tails are negligible uniformly. Because \(|a(m)|\ge4-\pi\), taking the termwise absolute value of (A11) gives exactly

\[
 \int_J\left(\sum_{m\ge1}|a(m)|\eta(m/X)
                  |F_{N,T}((m-x)/h(x))|\right)^6dx
 \ge cXH^6.
\]

The at-most-three-distinct-shift contribution to this positive expression is \(O_\epsilon(X^{1+\epsilon}H^3)\), as already proved. Thus the same obstruction remains after deleting that target-safe sector, taking epsilon sufficiently small.

For the weaker sufficient threshold (A4'), the relevant ratio is \(H^3/\Lambda\), not just \(H^3\). Up to fixed window constants,
\[
 \frac{H^3}{\Lambda}
 \asymp T^{71/25}N^{-3}W_0^6
 =\min\left\{
 T^{71/25}N^{-3/2},\
 T^{71/25+6\beta}N^{-3},\
 T^{146/25}N^{-6}\right\}.
 \tag{A19}
\]
Each of these three quantities is at least a fixed multiple of \(T^{136/125}\) throughout the middle range. For the third, this follows from \(N<T^{99/125}\), giving \(146/25-6(99/125)=136/125\). The first has the larger exponent \(413/250\) at the same endpoint. The second has exponent greater than \(58/125+3/4>136/125\), using \(\beta>1/8\). Hence the absolute placement fails even the weaker sufficient sixth threshold by a fixed power. The CRT endpoint-error *upper cost* (A1) exceeds that threshold by the further factor \(X^2\); this last comparison is not a lower bound for its actual signed remainder.

This is a concrete no-go for the specified absolute placement of the actual centered coefficients. The argument does not make the sufficient input (A4') necessary, and it supplies no lower bound for the signed sixth or twelfth moment.

## 4. First doubtful or unproved step

No Gaussian or independence step is used in the proved statements. Up to the explicitly negligible localization error, (A4) is equivalent to the following bound on the joint remaining correlation:

\[
 \boxed{\left|\int_0^1
 \sum_{\substack{\mathbf k\in\mathbb Z^6\\
              \#\{k_1,\ldots,k_6\}\ge4}}
 \sum_{b\in\mathbb Z}W_{\mathbf k,u}(b)
       \prod_{i=1}^6(r_2(b+k_i)-\pi)\,du\right|
 \ll_\epsilon X^{1+\epsilon}H^3.}
 \tag{A17}
\]

The equivalence follows because the complementary equality-pattern contribution is already bounded absolutely by the same order. In particular, this is a complete remaining interface, not an unestimated deletion of repeated shifts.

For the frozen twelfth-moment objective through (A8b), the actually sufficient arithmetic gap is the **weaker** version of (A17) with right side \(T^\epsilon\Lambda XH^3\). All at-most-three-distinct-shift patterns remain safe for that version, since \(\Lambda\ge T^{4/25}\). It is this relaxed bound, rather than (A4) alone, that the priced CRT and absolute-placement attempts also fail to establish. Neither failure proves that the actual twelfth-moment objective is false.

The exact hyperbola/CRT expression makes (A17) an inequality for the *joint signed local-density main term plus the joint weighted endpoint remainder*. Separate target-size estimates for both would suffice but are stronger than necessary. Neither is established here. The calculated \(X^3H^6\) error is only a placement cost; one may not infer that the actual error is that large. Conversely, discarding the error, replacing (A15) by a product of individual means, or taking absolute values over the remaining shifts has no justification; the last option is rigorously obstructed above.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `complete_middle_range` | PASS: every strict middle dyadic \(N\), with the exact outer boundary convention. Uniform constants; no smaller surviving frequency complement. |
| `actual_r2_character` | PASS: exact \(4\sum_{d\mid n}\chi_4(d)\), both quotient residue branches and even-character zeros. No representability indicator. |
| `all_divisors_and_shifts` | PASS: (A12) is exact, including \(d=D\), \(n=D\ell\), \(d=1\), \(\ell=1\). All six equality patterns and all CRT local densities are retained. |
| `curvature_and_mean_error` | PASS: (A6), constant-density identity (A5), and the \(O(D^{-1})\) hyperbola mean remainder are priced. |
| `infinite_tails` | PASS: curved and additive tails are summed before the finite arithmetic opening; their \(O_K(T^{-K})\) costs survive all fixed moments and dyadic recombination. |
| `real_endpoints` | PASS: (T,R,x) are real, partial unit cells remain in \(W\), all threshold jumps enter variation, and integer centers are allowed. |
| `signed_not_positive` | PASS as a method rejection: actual absolute centered expansion has a proved \(XH^6\) lower bound. No corresponding lower bound for the signed moment is claimed. |
| `full_moment_power_ledger` | PASS: conditional sixth scale gives (A8); current complete exponent remains \(10\beta\); CRT error and every normalization are displayed. |
| `source_hypotheses` | PASS within inherited scope: only the accepted repaired real-\(X\) Li--Yang consequence and accepted Round204 distribution are used. No new source theorem is imported. |
| `no_gaussian_inference` | PASS: (A9) is not promoted to (A4); explicit common-modulus local densities show why independent centering is invalid. |
| `full_proof_scope` | PASS: no improvement to the quarter target, pointwise exponent, M1/M2, or any parent obligation. Even success at this milestone would only give (102/325). |

These are analytic controls, not computational evidence. This selected-context report does not substitute for the campaign's isolated bridge rederivation or a conductor seam audit.

## 6. Dependencies and exact artifacts used

Read only the assigned brief and its permitted context:

- `protocol.md`.
- `state/proof_obligations.yml`, especially `GC-target`, `GC-external-Li-Yang-theta-star`, `GC-complete-square-root-large-values-moment-bound`, `GC-physical-twelfth-moment-absolute-majorant-obstruction`, and `GC-weighted-square-root-exact-resonance-mass`.
- `state/active_campaign.yml`, Round206.
- `strategy/round206_complete_signed_shell_arithmetic_attack.md`.
- `rounds/codex-managed/gc-complete-signed-shell-arithmetic/briefs/actual_divisor_shell_attack.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_middle_band_strategy.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/reviews/independent_middle_band_review.md`.
- `proofs/kernels/gc_complete_square_root_large_values_moment_bound.md`.
- `rounds/codex-managed/gc-full-frontier-moment-strategy-review/controls/conductor_arithmetic_source_gate.md`.
- `rounds/codex-managed/gc-complete-signed-convolution-attack/reports/arithmetic_signed_tail_attack.md`.

The former strategy/source and Round203 reports supply context and failure boundaries; their external citations are not newly imported as mathematical inputs. The exact divisor/hyperbola identity, CRT density, weighted residue-class summation, filter mean identity, variation estimates, Riemann-sum control and moment powers are derived in this report. No sibling report, excluded artifact or primary web source was consulted.

## 7. Recommended state effect

**No change** to accepted mathematical state or the proof draft. Retain (A11)--(A17) as candidate arithmetic-attempt evidence and the \(XH^6\) absolute-placement obstruction as a scoped diagnostic lemma, subject to the conductor's review policy. Retain the complete middle-band target as open and the existing exponent \(10\beta\).

Reject the inference that an (XH) variance implies an \(XH^3\) sixth moment, that centered distinct shifts have zero local main term, or that the CRT endpoint errors disappear on thin scales. The no-go is limited to the displayed absolute placement and error summation; it does not rule out a new signed divisor or shifted-correlation estimate.

Only this assigned report was written. No state, draft, matrix, synthesis, source-card or successor file was edited. The task stops here.



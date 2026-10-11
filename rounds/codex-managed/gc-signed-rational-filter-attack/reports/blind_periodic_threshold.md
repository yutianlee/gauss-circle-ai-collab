# Round207: independent periodic cutoff and threshold analysis

## 1. Result

Campaign: `gc-signed-rational-filter-attack`. Task and role: `blind_periodic_threshold`, independent statement-only analyst. Status: blind derivation. Generated: 2026-09-27. Graph hash: intentionally unavailable under the isolation instruction; no graph was read. Effort: 100% analytical, with no mathematical numerical experiments.

All three assertions hold under the ordinary integer-lattice interpretation of a progression and a uniformly bounded periodic atom. The support-buffer qualification in assertion 3 is essential and is satisfied by the packet.

There is a stronger uniform conclusion for assertion 2. Put (T_\ell=D\ell). For every fixed (A>0),

\[
R(x)=-\chi_4(D)\sum_{1\leq\ell\leq L}
 \eta(T_\ell/X)\mathbf 1_{x>T_\ell}
 K\!\left(\frac{x-T_\ell}{h(x)}\right)+E_A(x),
\qquad \sup_{x\in J}|E_A(x)|\ll_A X^{-A}.
\tag{1}
\]

The strict indicator at every transition is retained. In particular, when (D) is even, (R(x)=O_A(X^{-A})) uniformly on (J). When (D) is odd, the separated one-sided profiles in (1) give exactly the asserted upper bounds

\[
\sup_J |R|\ll1,
\qquad \int_J |R(x)|^6\,dx\ll X^{1/2}H.
\tag{2}
\]

The full unweighted progression vanishes also at (q=h/2), not merely below that cutoff. For the character-weighted full lattice the Gauss factor is (-2i\chi_4(k)), and its initial vanishing range is (\ell\leq h/8).

These conclusions concern periodic completion and a boundary error only. They provide no arithmetic sixth-moment theorem and no Gaussian-moment inference.

## 2. Exact statements and hypotheses

Use (e(t)=\exp(2\pi i t)) and

\[
\widehat K(\xi)=\int_{\mathbb R}K(u)e(-u\xi)\,du.
\]

For assertion 1, (q\) is a positive integer and (b\) is an integer. Equivalently, the same formula holds for arbitrary real (q>0,b\), if its left side is explicitly the lattice (m\in b+q\mathbb Z\), without an additional restriction (m\in\mathbb Z\). The weighted formula below uses a positive integer (\ell\), and its full-lattice sum includes every integer multiple of (\ell\), including zero and negative multiples.

For assertions 2 and 3, retain every definition and range in the statement packet. In particular (X\to\infty), (0<\delta<1/4) is fixed, and there are fixed comparison constants (a,b>0) such that

\[
aH\leq h(x)\leq bH\quad (x\in J),
\qquad X^\delta\leq H\leq X^{1/2-\delta}.
\tag{3}
\]

The proofs of the upper bounds need only the upper bound in (3); they are therefore valid for the stated (h(x)=c\sqrt{x}/\sqrt N) without any differentiation of (h\). Define the uniform seminorm bounds

\[
B_p=\sup_K\sup_{u\in\mathbb R}(1+|u|)^p|K(u)|<\infty.
\]

Implicit constants may depend on (A,\delta,b\), the fixed cutoff, and sufficiently many stated uniform Schwartz seminorm bounds. They do not depend on (X,H,N,x\), the particular member (K\), or the progression modulus. The estimates hold for all (X\geq X_0), with (X_0) depending only on the fixed parameters; for the separated-center argument it suffices to require (bX^{-\delta}\leq1).

Here is a precise version of the phrase “sums of (O(\sqrt X)) periodic atoms” in assertion 3. Let (n_X\leq C_0\sqrt X), let (|c_j(x)|\leq C_1), and let the integer-lattice weights satisfy (|a_j(m)|\leq1). Periodic progression indicators and the weights (\mathbf 1_{\ell\mid m}\chi_4(m/\ell)) are included. The (K_j\) belong to the given uniform Schwartz family. Then uniformly on (J),

\[
\sum_{j=1}^{n_X}c_j(x)
\left[
\sum_{m\geq1}\eta(m/X)a_j(m)K_j((x-m)/h(x))
-\sum_{m\in\mathbb Z}a_j(m)K_j((x-m)/h(x))
\right]
=O_A(X^{-A}).
\tag{4}
\]

The proof in fact does not require periodicity. Uniformly bounded outer coefficients alone would not suffice if the atom itself were allowed unbounded lattice weights, unbounded normalization, or arbitrarily dense noninteger lattices. Such objects are outside (4).

## 3. Proof and complete error estimates

### 3.1 Full-lattice identities and the endpoint cutoff

For (f(t)=K((x-t)/h)), a change of variables gives

\[
\widehat f(\xi)=h e(-x\xi)\widehat K(-h\xi).
\]

The periodization \(\sum_{n\in\mathbb Z}f(b+qn)\) converges absolutely with all derivatives, and its Fourier coefficients are \(q^{-1}\widehat f(k/q)\). Its Fourier series therefore gives, after replacing (k\) by (-k),

\[
\boxed{
\sum_{m\equiv b\; (q)}K((x-m)/h)
=\frac hq\sum_{k\in\mathbb Z}
\widehat K(hk/q)e(k(x-b)/q).
}
\tag{5}
\]

This argument is also a direct proof of the Poisson formula needed here. All sums are legitimate for Schwartz (K); under the spectral support hypothesis the right side is finite.

The zero frequency is zero: \(\widehat K(0)=0\), both by the support assumption and by oddness. Since \(\widehat K\) is smooth on the whole real line and vanishes off the two closed support intervals, it vanishes at all four endpoints \(\pm1,\pm2\), with every derivative there. If (q<h/2), every nonzero frequency has \(|hk/q|>2\). If (q=h/2), the only additional candidates are (k=\pm1), which evaluate at \(\pm2\) and are zero. Thus the left side of (5) vanishes for (q\leq h/2).

Splitting the character-weighted lattice into the residues (m\equiv\ell,3\ell\pmod{4\ell}) gives

\[
\begin{aligned}
A_\ell(x,h)
&:=\sum_{\substack{m\in\mathbb Z\\\ell\mid m}}
 \chi_4(m/\ell)K((x-m)/h)\\
&=\frac{h}{4\ell}\sum_{k\in\mathbb Z}
 \widehat K\!\left(\frac{hk}{4\ell}\right)
 e\!\left(\frac{kx}{4\ell}\right)
 \left[e(-k/4)-e(-3k/4)\right].
\end{aligned}
\]

For even (k) the bracket is zero; for (k\equiv1\pmod4) it is (-2i), and for (k\equiv3\pmod4) it is (2i). Consequently

\[
\boxed{
A_\ell(x,h)=-\frac{ih}{2\ell}
\sum_{k\in\mathbb Z}\chi_4(k)
\widehat K\!\left(\frac{hk}{4\ell}\right)
e\!\left(\frac{kx}{4\ell}\right).
}
\tag{6}
\]

Only odd frequencies contribute, and the zero frequency vanishes independently through the character. Formula (6) vanishes for (\ell\leq h/8), with equality handled by the same endpoint argument. The constants and the sign in (6) use exactly the stated (e(-u\xi)) convention.

### 3.2 Exact boundary decomposition

For (X\geq1), the definitions imply the convenient bounds

\[
\sqrt X\leq D\leq\sqrt{7X},
\qquad L\leq\sqrt{7X},\qquad DL\leq7X.
\tag{7}
\]

Write (m=\ell r), (T=D\ell). At a given (\ell), the indicator difference is exactly:

* if (x\leq T), it is (1) for (r>D) and zero otherwise;
* if (x>T), it is (-1) for (1\leq r\leq D) and zero otherwise.

In the second case extract the term (r=D). This proves the exact identity

\[
R(x)=-\chi_4(D)S(x)+E(x),
\quad
S(x)=\sum_{\ell\leq L}\eta(T_\ell/X)
\mathbf 1_{x>T_\ell}K((x-T_\ell)/h(x)),
\tag{8}
\]

where the remaining nonzero terms have (r=D+j), (j\geq1), when (x\leq T), or (r=D-j), (1\leq j\leq D-1), when (x>T). In either case their distance from (x) is exactly

\[
|x-m|=|x-T|+j\ell.
\tag{9}
\]

No transition point was removed: at (x=T) the upper case applies and the extracted term is absent.

To bound (E), first consider \(\ell<X/(4D)\). Here (T<X/4<x), and every remaining (m\leq T) is at distance at least (X/4) from (x\in J). There are at most (DL\leq7X) such terms in total. Their absolute contribution is at most

\[
7X B_p(4bH/X)^p.
\tag{10}
\]

For the complementary indices, \(\ell\geq X/(4D)\geq\sqrt X/(4\sqrt7)\). For any fixed (p>1), (9), \(0\leq\eta\leq1\), and \(|\chi_4|\leq1\) give an upper bound per index

\[
B_p\sum_{j\geq1}\left(\frac{h(x)}{j\ell}\right)^p
\leq B_p\zeta(p)(4\sqrt7\,bH/\sqrt X)^p.
\]

Combining the two parts and (7),

\[
\sup_J|E|
\leq C_{p,b}B_p\left[
 X(H/X)^p+X^{1/2}(H/\sqrt X)^p
\right]
\leq C_{p,b}B_p
\left[X^{1-p(1/2+\delta)}+X^{1/2-p\delta}\right].
\tag{11}
\]

Given (A>0), choose an integer

\[
p>\max\left\{1,\frac{A+1}{1/2+\delta},\frac{A+1/2}{\delta}\right\}.
\tag{12}
\]

This proves (1), uniformly for real (x\in J), including every integer threshold. Remote upper thresholds are covered by (9); no assumption that (T\in J) has been used.

### 3.3 The separated-center bounds

Put

\[
F(x)=\sum_{\ell\leq L}\eta(T_\ell/X)
 \mathbf 1_{x>T_\ell}|K((x-T_\ell)/h(x))|.
\]

The centers have spacing (D\), while (h(x)/D\leq bX^{-\delta}\leq1) for sufficiently large (X). There is at most one center with (0<x-T_\ell\leq D). Successive earlier centers have distance at least (D,2D,\ldots). Hence, uniformly in (x),

\[
F(x)\leq B_0+B_2\zeta(2)(h(x)/D)^2
\leq C_*:=B_0+B_2\zeta(2).
\tag{13}
\]

Also,

\[
\int_J F(x)\,dx
\leq \sum_{\ell\leq L}B_2
\int_{\mathbb R}\left(1+\frac{|x-T_\ell|}{bH}\right)^{-2}dx
\leq2bB_2LH.
\tag{14}
\]

Since \(|S|\leq F\),

\[
\int_J|S|^6\leq C_*^5\int_JF
\leq 2\sqrt7\,bB_2 C_*^5\sqrt X H.
\tag{15}
\]

Equations (8), (11), and \(|u+v|^6\leq32(|u|^6+|v|^6)\) now prove (2). Explicitly, the integrated remainder is at most \((5X/2)C_A^6X^{-6A}\); taking (A=1) already makes this negligible relative to the claimed bound. No cancellation between distinct thresholds, and no spectral property of (K), was needed for this part.

### 3.4 Completion through the fixed support buffer

For (x\in[X/2,3X]\), the multiplier

\[
\mathbf 1_{m\geq1}\eta(m/X)-1
\]

can be nonzero only when \(|m-x|\geq X/6\). Indeed, \(\eta=1\) on \([X/3,4X]\), which contains (J) with a left margin (X/6) and a right margin (X); nonpositive integers are farther away. In fact the factor \(\mathbf1_{m\geq1}\) is redundant for the cutoff sum, since the support of \(\eta(m/X)\) is positive.

For (p>1), (X\geq12), and every real (x), comparison with unit intervals gives

\[
\sum_{\substack{m\in\mathbb Z\\|m-x|\geq X/6}}
|m-x|^{-p}\leq C_p X^{1-p}.
\tag{16}
\]

Thus one atom's completion error is at most \(C_pB_p(bH)^pX^{1-p}\), uniformly in its modulus or bounded lattice weight. Summing the bounded outer coefficients and at most (C_0\sqrt X) atoms gives

\[
|\text{total error}|
\leq C_{p,b,C_0,C_1}B_p X^{3/2}(H/X)^p
\leq C_{p,b,C_0,C_1}B_p X^{3/2-p(1/2+\delta)}.
\tag{17}
\]

Choosing an integer \(p>\max\{1,(A+3/2)/(1/2+\delta)\}\) proves (4). Sufficient uniform Schwartz decay is exactly what makes this (O_A(X^{-A})) for every fixed (A).

## 4. First doubtful or unproved step

There is no remaining unproved step in (1)--(6), (11), (15), or (17), under the explicit integer-lattice and bounded-atom hypotheses in section 2.

There are three interpretation boundaries:

1. If “(m\in\mathbb Z,\ m\equiv b\pmod q)” is retained for noninteger (q,b), it need not describe the lattice (b+q\mathbb Z); the Poisson formula must then be applied to the actual lattice, not to the displayed (q) by assumption.
2. Discarding the term (m=D\ell) when (x>D\ell) is a genuine failed step. For odd (D), that term generally contributes a fixed nonzero one-sided profile. Oddness only annihilates its value at the exact center, not at nearby real (x).
3. The completion estimate cannot be applied at evaluation points without an appropriate plateau buffer, or to atoms whose own weights or normalizations are unbounded. The first failed step would be the distance assertion preceding (16), or the bounded-weight estimate preceding (17), respectively.

No claim concerning the full arithmetic signed sum follows merely from these periodic and transition estimates.

## 5. Required analytical controls and outcomes

**Single jump and nearby real points: passed.** Fix (T=D\ell\in[X,2X]), and a fixed (u>0). The equation (x-T=u h(x)) has a unique solution (x>T) for the stated square-root scale, as is seen by solving the quadratic in \(\sqrt x\). It lies in (J) for large (X). The cutoff is one at (T/X), and every other center is at distance comparable to at least (D). Applying Schwartz decay with arbitrary order to those other centers gives

\[
R(x)=-\chi_4(D)K(u)+O_A(X^{-A}).
\tag{18}
\]

For a fixed (u<0), the corresponding solution lies to the left of (T), the extracted term is absent, and (R(x)=O_A(X^{-A})). Therefore uniform smallness of all (R), or deletion of the (r=D) term, is false when (D) is odd and (K(u)\ne0). Formula (18) is the concrete control, using the original coefficient family.

**Exact integer centers: passed.** If (x=T_\ell\in J), the local extracted term is absent, and (K(0)=0) in any case. Every other extracted center is separated by at least (D), and the error is covered by (11). Hence (R(T_\ell)=O_A(X^{-A})). The estimates are not obtained by discarding these points; they hold there directly. An integer (x) which is not a threshold is covered by the same uniform estimates without a special convention.

**Even (D): passed.** The extracted coefficient is exactly \(\chi_4(D)=0\), so (11) gives the stronger superpolynomial bound for the whole boundary error.

**Progression near the cutoff and the Gauss sign: passed.** Let (q\) be a positive integer and take (q<h<2q), so that \(a=h/q\in(1,2)\). Choose a real odd smooth function \(\psi\), compactly supported in the interiors of the two spectral bands, with \(\psi(a)\ne0\), and let \(\widehat K=i\psi\). Its inverse Fourier transform is a real odd Schwartz function of the permitted type. Only (k=\pm1) can contribute to (5), and its value is

\[
-2(h/q)\psi(a)\sin(2\pi(x-b)/q).
\]

This is nonzero for an appropriate (x), so the vanishing range cannot generally be extended to every (q>h/2). At equality (h=2q), the boundary value is zero. Smoothness also implies vanishing to every order as the sampled frequency approaches the endpoint, for a fixed uniformly controlled family.

For (6), take \(4\ell<h<8\ell\) and \(a=h/(4\ell)\in(1,2)\). Only (k=\pm1) contribute, yielding

\[
(h/\ell)\psi(a)\cos(2\pi x/(4\ell)).
\]

This directly checks the sign and factor in (6), and shows that the initial cutoff \(\ell\leq h/8\) is sharp as an interval of guaranteed vanishing. Individual larger moduli can still vanish, for example when all sampled frequencies hit spectral endpoints or zeros.

**Small \(\ell\) and remote thresholds: passed.** For \(D\ell<X/4\), only indices (m\leq D\ell\) remain in the boundary discrepancy and all are at least (X/4) away from (J), giving (10), even if \(\ell\ll h\). For thresholds outside (J) with larger \(\ell\), identity (9) and the grid estimates remain valid. In particular thresholds separated from (J) by a fixed positive multiple of (X) contribute (O_A(X^{-A})), even after summing all indices. No assumption that every \(\ell\) is large was made.

**Plateau-buffer necessity: passed, with scope stated.** This control concerns a proposed extension outside the packet's interval (J). Take positive integer (X\) divisible by four, let (m_0=X/4), (q=100X), and use the periodic atom \(\mathbf1_{m\equiv m_0\;(q)}\). Smooth support forces \(\eta(1/4)=0\). Choose a nonzero permitted (K\) and a fixed (u_0\) with \(K(u_0)\ne0\), and take an evaluation point satisfying (x-m_0=u_0h(x)), with an admissible scale comparable to (H\). This point is near (X/4\), outside (J). The (m_0\) contribution to completion is exactly \(-K(u_0)\), while every other progression point is at distance comparable to (q\) and has total contribution (O_A(X^{-A})\). Thus completion without a buffer can have order-one error. It does not contradict (4), whose buffer is (X/6\).

**Unsigned/adversarial boundary weights: scope verified.** The upper-bound proof for the boundary discrepancy uses only boundedness of the coefficients. Replacing \(\chi_4(r)\) by arbitrary weights \(a_{\ell,r}\) of absolute value at most one gives an extracted term with coefficient \(a_{\ell,D}\), and the same upper bounds. The even-(D\) improvement is specific to \(\chi_4(D)=0\). This extension concerns this boundary object only; it does not assert an unsigned or adversarial analogue of any complete arithmetic moment estimate.

## 6. Dependencies and exact artifacts used

Exactly two context files were read:

1. `protocol.md`.
2. `rounds/codex-managed/gc-signed-rational-filter-attack/briefs/blind_periodic_threshold_statement.md`.

No graph, campaign manifest, general generated brief, strategy, predecessor, claimant report, sibling report, web source, or external literature was inspected. No computation was used. The only mathematical inputs are the packet's hypotheses, Fourier inversion/periodization for Schwartz functions as derived in section 3.1, elementary discrete tail estimates, and integration of a decaying envelope.

Only this assigned report file was written. No authoritative state or shared artifact was edited.

## 7. Recommended state effect

Recommend **promote**, subject to the conductor's required reviews and graph validation, the precisely qualified periodic identities, cutoff including equality, buffered completion estimate, and threshold-error bounds with the stronger decomposition (1). The even-(D\) improvement can be retained as an exact corollary.

Recommend **no change** to any full arithmetic sixth-moment or Gaussian-moment claim. If a broader route had treated the odd-(D\) single-jump contribution as uniformly negligible, recommend **reject** that step using (18). This report does not apply any State Patch or initiate another round.

# Round 213: isolated centered-certificate rederivation

## 1. Result: sharp certificate scale and scoped obstruction

- Campaign: `gc-complete-centered-arithmetic`; round: 213.
- Task and role: `blind_centered_certificate`; statement-only independent rederivation.
- Generated: 2026-09-28T00:46:59+08:00.
- Graph hash (supplied metadata only; not inspected): `4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71`.

Under exactly the packet's assumptions, put

\[
D=\frac{LK}{U}.
\]

The specified positive certificate obeys, for every fixed epsilon greater than zero,

\[
\boxed{c_*N D^{-1/2}\le P\le C_\varepsilon T^\varepsilon N D^{-1/2}.}
\tag{1}
\]

The lower bound holds for every allowed choice of the constants \(\rho_s\); its constant does not depend on that choice. Since

\[
D\asymp T^{1-6b},\qquad ND^{-1/2}\asymp T^{\alpha-1/2+3b},
\]

this resolves the certificate's power scale. Its proposed \(O_\varepsilon(T^{4b+\varepsilon})\) bound holds under the supplied upper bounds when

\[
4b<\alpha\le \frac12+b,
\]

but is impossible in the standard every-epsilon formulation when

\[
\frac12+b<\alpha<1-2b.
\]

Here the threshold is \(1/2+b=204/325\), inside the stipulated band \((166/325,242/325)\). Thus subtraction of constants cannot make this particular certificate satisfy the proposed bound throughout the band.

This is exclusively a certificate obstruction. A control below satisfies all packet hypotheses while its actual signed sums \(C_s(R)\), and also \(E_s(R)\), are uniformly smaller than every negative power of \(N\). The certificate remains of the size in (1).

The exact correction is

\[
E_s(R)-C_s(R)
=\rho_s\left(\sum_n f_s(R,n)-\int_{\mathbb R}f_s(R,t)\,dt\right)
=\rho_s\sum_{\ell\ne0}\int_{\mathbb R}W_s(t)e(R\psi_s(t)-\ell t)\,dt.
\tag{2}
\]

For every \(A>0\), uniformly in the allowed \(s,R,W_s\),

\[
|E_s(R)-C_s(R)|\le C_A\rho_sN^{-A}.
\tag{3}
\]

The uniform constants depend on finitely many stated mask seminorms. In particular the correction is \(O_A(T^{-A})\) after increasing the number of integrations by parts and using the allowed subpower bound for \(\rho_s\).

## 2. Exact statement and hypotheses

All quantities and hypotheses are those of the isolated packet. In particular:

- \(b=83/650\), \(N=T^\alpha\), and \(4b<\alpha<1-2b\), with \(\alpha\) fixed.
- \(L=\max(2,\lceil\sqrt N T^{-2b}\rceil)\), \(K=\max(2,\lceil NT^{-4b}\rceil)\), \(U=N^{3/2}/T\).
- \(s=(h,k)\in\Omega\) means \(1\le h<L\), \(1\le k<K\), \(h\ne k\), and \(\Lambda_s=hk/U>1\).
- \(W_s\) is real, smooth, compactly supported in \([N,4N]\), with \(\|W_s^{(j)}\|_\infty\le C_jN^{-j}\), and \(\sum_n|W_s(n)|\ge cN\), uniformly.
- \(a_s(n)\ge0\), \(a_s(n)=0\) on \(n\equiv3\pmod4\), and \(a_s(n)\le C_\varepsilon T^\varepsilon\). The packet assumes \(\sum_{s\in\Omega,n}a_s(n)|W_s(n)|\ge cLKN\).
- \(\rho_s\ge0\) is constant with respect to \(t,R\), and \(\rho_s\le C_\varepsilon T^\varepsilon\).
- The radius is \(T/\sqrt2\le R\le\sqrt3T\). The fixed nonnegative smooth function \(w\) has compact support in the normalized radius interval and integral one.

Constants in (1)--(3) may depend on these uniform constants and on \(w\). No sign condition on \(W_s\), no correlation asymptotic, and no arithmetic interpretation of \(a_s\) is imposed or used.

The norm naturally certified by \(P\) uses the probability measure

\[
d\mu_T(R)=T^{-1}w(R/T)\,dR.
\tag{4}
\]

Precisely,

\[
\frac1{LK}\sum_{s\in\Omega}\|C_s\|_{L^2(\mu_T)}\le P,
\qquad
\left\|\frac1{LK}\sum_{s\in\Omega}|C_s|\right\|_{L^2(\mu_T)}\le P.
\tag{5}
\]

The weighted \(L^2\) norm of \((LK)^{-1}\sum_sC_s\), and the corresponding weighted \(L^1\) quantities, are consequently bounded by \(P\). This is not a pointwise-in-radius bound, an unweighted full-interval norm assertion, or a lower bound on an actual signed quantity.

## 3. Proof and derivation

### 3.1 Phase scale and uniformity

Set \(\ell_0=\sqrt NT^{-2b}\). Since \(\ell_0\to\infty\),

\[
L\asymp\ell_0,\quad K\asymp\ell_0^2,\quad
D=LK/U\asymp T^{1-6b}.
\tag{6}
\]

The useful exact double-integral identity is

\[
\psi_s(t)=-\frac14\int_0^h\int_0^k(t+x+y)^{-3/2}\,dy\,dx.
\tag{7}
\]

On \([N,4N]\), one has \(h+k=o(N)\). Differentiation of (7) therefore gives

\[
|\psi_s^{(j)}(t)|\le C_jhkN^{-3/2-j},\qquad
c hkN^{-5/2}\le\psi'_s(t)\le C hkN^{-5/2}.
\tag{8}
\]

In particular, for all \(n,m\in[N,4N]\),

\[
c\frac{\Lambda_s}{N}|n-m|
\le |T(\psi_s(n)-\psi_s(m))|
\le C\frac{\Lambda_s}{N}|n-m|.
\tag{9}
\]

Uniformly for the allowed radii, \(|R\psi_s^{(j)}|\le C_j\Lambda_sN^{-j}\). Also

\[
\frac{\Lambda_s}{N}\le\frac DN\ll T^{1-6b-\alpha}
\le T^{1-10b}=T^{-18/65}=o(1).
\tag{10}
\]

This bound is uniform across the open band, apart from harmless absolute ceiling constants.

### 3.2 Residue-zero mass survives arbitrary constant centering

For a fixed \(s\), write

\[
V(n)=|W_s(n)|,\quad Q=\sum_nV(n),\quad
q=\sum_{n\equiv3\ (4)}V(n),\quad p=Q-q,
\]

\[
M=\sum_na_s(n)V(n),\qquad
H=\sum_n|a_s(n)-\rho_s|V(n).
\]

The absolute value \(V(t)=|W_s(t)|\) need not be smooth, but it is absolutely continuous with

\[
\operatorname{Var}(V)\le\int|W'_s(t)|\,dt\le3C_1.
\]

Comparing adjacent residue sums by translating the integer index by one, their difference is bounded by \(\operatorname{Var}(V)\). Hence

\[
q=Q/4+O(1),\qquad p=3Q/4+O(1).
\tag{11}
\]

As \(Q\ge cN\), one has \(q/p=1/3+O(N^{-1})\) and \(p\ge q>0\) for all sufficiently large \(T\).

The exact zero on the fourth residue gives

\[
H=\rho_sq+\sum_{n\not\equiv3\ (4)}|a_s(n)-\rho_s|V(n)
\ge\rho_sq+|M-\rho_sp|.
\tag{12}
\]

For any \(M\ge0\), \(p\ge q>0\), and \(\rho\ge0\),

\[
\rho q+|M-\rho p|\ge (q/p)M.
\]

This follows by considering \(\rho\le M/p\) and \(\rho\ge M/p\); the minimum occurs at \(\rho=M/p\). Thus

\[
H\ge(1/3-O(N^{-1}))M\ge c_0M.
\tag{13}
\]

The asymptotic constant \(1/3\) is optimal at this mass-comparison interface: take \(a_s(n)=A\) off residue three, zero on residue three, and \(\rho_s=A\). Then \(H=Aq\), \(M=Ap\).

The use of \(|W_s|\) in (11)--(13) is essential. No unsigned-to-signed mass substitution has occurred.

### 3.3 Near-diagonal positivity gives the lower certificate bound

Because \(\widehat w_+(0)=1\), there is \(\delta>0\) such that

\[
|\widehat w_+(y)|\ge1/2\quad (|y|\le\delta).
\]

Partition the integer points in \([N,4N]\) into \(J\le C\Lambda_s\) consecutive blocks, each of real diameter at most \(\delta N/(C\Lambda_s)\), with the constant chosen using (9). This is possible because \(\Lambda_s>1\) and \(N/\Lambda_s\to\infty\) uniformly. For the nonnegative sequence \(B_s\), all pairs inside one block then have kernel modulus at least \(1/2\). Consequently,

\[
G_s\ge\frac12\sum_{j=1}^J\left(\sum_{n\in I_j}B_s(n)\right)^2
\ge\frac{H_s^2}{2J},
\]

and therefore

\[
\sqrt{G_s}\ge c H_s\Lambda_s^{-1/2}.
\tag{14}
\]

Use (13), \(\Lambda_s\le D\), and the supplied absolute-mass assumption:

\[
P\ge\frac{c}{LK}\sum_s\frac{M_s}{\sqrt{\Lambda_s}}
\ge\frac{c}{LK\sqrt D}\sum_sM_s
\ge c_*\frac N{\sqrt D}.
\tag{15}
\]

This argument uses no cancellation or arithmetic correlation estimate.

### 3.4 Matching upper certificate scale

Smooth compact support of \(w\) gives \(|\widehat w_+(y)|\le C_A(1+|y|)^{-A}\). Moreover \(B_s(n)\le C_\varepsilon T^\varepsilon\). By the lower inequality in (9), for every fixed \(n\),

\[
\sum_m|\widehat w_+(T(\psi_s(n)-\psi_s(m)))|
\le C\left(1+\frac N{\Lambda_s}\right)
\le C\frac N{\Lambda_s}.
\]

There are \(O(N)\) integer support points. Thus

\[
G_s\le C_\varepsilon T^{2\varepsilon}\frac{N^2}{\Lambda_s},
\qquad
\sqrt{G_s}\le C_\varepsilon T^\varepsilon N\sqrt{\frac U{hk}}.
\tag{16}
\]

Extending the upper sum to the entire positive rectangle, and using \(\sum_{j<J}j^{-1/2}\le2\sqrt J\), gives

\[
P\le\frac{C_\varepsilon T^\varepsilon N\sqrt U}{LK}
\left(\sum_{h<L}h^{-1/2}\right)
\left(\sum_{k<K}k^{-1/2}\right)
\le C_\varepsilon T^\varepsilon N\sqrt{\frac U{LK}}.
\tag{17}
\]

Together (15) and (17) prove (1). If \(\alpha>1/2+b\), choose any \(0<\varepsilon<\alpha-1/2-b\); (15) contradicts a target upper bound with that epsilon. If \(\alpha\le1/2+b\), (17) supplies the target upper bound directly.

### 3.5 Exact sum-integral correction with radius and support costs

Subtracting the two definitions gives the first equality in (2), with the displayed positive sign. Extend \(f_s\) smoothly by zero off its positive support. Poisson summation gives the second equality in (2).

Here is a bound which avoids unnecessarily paying powers of \(\Lambda_s\). Put \(t=Nx\), \(A_s(x)=W_s(Nx)\), and

\[
\Phi_{s,R,\ell}(x)=R\psi_s(Nx)-\ell Nx.
\]

The amplitude has support in the fixed interval \([1,4]\) and uniformly bounded derivatives. For \(\ell\ne0\), (10) yields

\[
|\Phi'_{s,R,\ell}(x)|\ge\tfrac12|\ell|N,
\qquad
|\Phi^{(j)}_{s,R,\ell}(x)|\le C_j\Lambda_s\le C_j|\ell|N\quad(j\ge2).
\]

Every fixed-order derivative of \(1/\Phi'\) is therefore \(O_j((|\ell|N)^{-1})\). Repeated integration by parts with \((2\pi i\Phi')^{-1}d/dx\) gives, for integer \(J\ge2\),

\[
\left|\int W_s(t)e(R\psi_s(t)-\ell t)\,dt\right|
\le C_J N^{1-J}|\ell|^{-J}.
\tag{18}
\]

There are no endpoint terms because the amplitude is smooth and compactly supported. The support length cost is exactly the initial factor \(N\), and normalized support location remains inside \([1,4]\). The radius cost is absorbed uniformly through \(R/T\in[1/\sqrt2,\sqrt3]\). Summing (18) gives \(O_J(\rho_sN^{1-J})\); taking \(J\) sufficiently large proves (3).

### 3.6 The actual norm bounded by the certificate

Let \(d_s(n)=(a_s(n)-\rho_s)W_s(n)\). Direct expansion, with the probability measure (4), gives the exact identity

\[
\|C_s\|_{L^2(\mu_T)}^2
=\sum_{n,m}d_s(n)\overline{d_s(m)}
\widehat w_+(T(\psi_s(n)-\psi_s(m))).
\tag{19}
\]

The triangle inequality makes the right-hand side at most \(G_s\). Summing its square-root bounds proves the first assertion of (5); Minkowski proves the second. Since \(\mu_T\) is a probability measure, weighted \(L^1\) follows by Cauchy--Schwarz. With the unnormalized measure \(w(R/T)dR\), all stated \(L^2\) bounds instead have the factor \(\sqrt T\).

Equation (3) transfers (5) to \(E_s\) with an error smaller than every fixed negative power of \(T\). It does not turn the certificate's lower bound into a lower bound for the norms in (19).

## 4. First doubtful or unproved step

There is no unproved step in the certificate theorem above relative to the packet assumptions. The first unavailable implication would be to infer a lower bound for an actual signed sum, or for its radius norm, from the lower bound on \(G_s\) or \(P\). Equation (19) only provides an upper bound by \(G_s\), and the residue-periodic control below explicitly invalidates the reverse implication.

The assumed global absolute-mass inequality is not proved here for an arithmetic sequence. Any application to a particular arithmetic coefficient system must independently supply that assumption and the other stated hypotheses. No graph state or prior argument was inspected to supply them.

Similarly, a weighted \(L^2\) certificate does not by itself establish a uniform-in-radius upper bound of the same size. The weight need not control the entire radius interval from below.

## 5. Required control tests and outcomes

### 5.1 Residue-zero test: constant centering cannot remove absolute mass

Equation (12) is an exact analytical control. Even if \(a_s\) is constant on the three available residue classes and \(\rho_s\) equals that value, residue three retains centered absolute mass \(\rho_sq\). Smoothness and the given \(\ell^1\) mask mass force \(q\asymp N\). The sharp mass ratio is \(q/p=1/3+O(N^{-1})\). Outcome: pass.

The necessity of the zero-residue hypothesis can also be seen directly: if it is removed, take \(a_s(n)=\rho_s=1\). The uncentered mass is positive but \(B_s=0\), so (1)'s lower bound fails. The necessity of smooth residue equidistribution is likewise visible if the derivative condition is removed: masks vanishing at residue three can hide the zero-residue defect entirely. Neither failure is allowed by the packet.

### 5.2 Sign-changing-mask test

Choose any nonzero real \(\phi\in C_c^\infty((1,4))\) with \(\int\phi=0\), and set \(W_s(t)=\phi(t/N)\). Then \(\sum_n|W_s(n)|\asymp N\), while \(\sum_nW_s(n)\) is smaller than every negative power of \(N\). Nevertheless the absolute mask has bounded variation, and each residue contains \(\tfrac14\sum_n|W_s(n)|+O(1)\). Thus (11)--(15) remain valid without any sign restriction on the mask. Outcome: pass; replacing absolute mask mass by signed mask mass would fail at this exact seam.

### 5.3 Actual-signed-quantity countermodel

Take any fixed nonzero real \(\phi\in C_c^\infty((1,4))\), allowing the sign-changing choice just described, and set for every \(s\)

\[
W_s(t)=\phi(t/N),\qquad
a_s(n)=\mathbf1_{n\not\equiv3\ (4)},\qquad
\rho_s=3/4.
\tag{20}
\]

All coefficient and mask hypotheses hold. The global mass assumption holds as well: for sufficiently large \(T\), the rectangle \(L/2\le h<L\), \(K/2\le k<K\) has \(\gg LK\) integer points, has \(h\ne k\) because \(K/L\to\infty\), and lies in \(\Omega\) because \(LK/U\to\infty\). For each such pair, \(M_s=\tfrac34\sum_n|W_s(n)|+O(1)\gg N\).

The centered coefficient in (20) has period four and mean zero:

\[
a_s(n)-3/4=-\frac14\sum_{j=1}^3e(j(n-3)/4).
\]

Each corresponding term in \(C_s\) has the form

\[
\sum_nW_s(n)e(R\psi_s(n)+jn/4).
\]

Poisson summation produces frequencies \(\ell-j/4\), each of distance at least \(1/4\) from zero. The same nonstationary integration by parts used in (18) therefore gives

\[
\sup_{s\in\Omega,\ R\in[T/\sqrt2,\sqrt3T]}|C_s(R)|=O_A(N^{-A})
\]

for every \(A\). Equation (3) gives the same conclusion for \(E_s\). Yet (1) still applies to its positive certificate. Outcome: the proposed inference from a large positive certificate to a large actual signed quantity is rigorously falsified.

All controls are analytical. No numerical experiment or source search was used.

## 6. Dependencies and exact artifacts used

The only context files read were:

1. `protocol.md`.
2. `rounds/codex-managed/gc-complete-centered-arithmetic/briefs/blind_centered_certificate_statement.md`.

The proof uses elementary differentiation, total variation, triangle and Cauchy--Schwarz inequalities, Minkowski, and Poisson summation for smooth compactly supported functions. The repeated integration-by-parts estimates needed for uniformity are explicitly provided above. No external theorem about an arithmetic correlation, no web source, no sibling report, and no prior-round artifact was used. The supplied graph hash was recorded without opening or validating the graph.

## 7. Recommended state effect

Recommend retaining or promoting, after the conductor's required seam reviews and graph validation, the narrowly stated certificate theorem (1), exact correction (2)--(3), and norm identification (5). Reject the proposal that constant centering alone makes this specific positive certificate \(O_\varepsilon(T^{4b+\varepsilon})\) throughout the entire stated band; its exact obstructed subband is \(\alpha>1/2+b\).

Do not reject a corresponding estimate for the actual signed arithmetic quantity on this evidence. Control (20) demonstrates why the certificate obstruction cannot supply that conclusion. No authoritative state, proof draft, validation matrix, or synthesis was edited. This report completes the assigned task; no next round is proposed or begun.

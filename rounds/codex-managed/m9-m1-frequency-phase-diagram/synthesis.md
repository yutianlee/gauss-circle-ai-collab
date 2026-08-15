# Round 10 synthesis: the M1 terminal line and certified wedge

Campaign: `m9-m1-frequency-phase-diagram`  
Round type: M1 parameter-region attack  
Graph SHA-256 before patch: `de423711249b9a2d4e136f52923b525a41a1e8d09239a74df92fd9c1a74ae819`

## Conductor decision

Promote the frequency-first divisor estimate, the M1 specialization of the
audited Tao--Trudgian--Yang exponent pair, and the resulting exact phase
diagram relative to the accepted direct menu. Retain M1 as open on the
nonempty residual corridor. The hostile literature task disclosed an
isolation breach and is not used to validate the terminal lemma; that lemma
was independently rederived in the statement-only phase-diagram report.

## Actual M1 block

Suppressing fixed harmless constants and the conjugate frequency, write

\[
B_1(D,L;X)=
\sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
\sum_{d\asymp D}\chi_4(d)w_D(d)e(hX/d),
\qquad H_D\asymp DX^{-1/4}.
\]

The actual frequency coefficient, including a fixed dyadic cutoff, satisfies

\[
\|u_{L,H}\|_\infty+\sum_h|\Delta u_{L,H}(h)|\ll L^{-1}.
\]

All promoted bounds require only the accepted bounded discrete-BV spatial
profiles, so they include the one-sided hard top block.

## Frequency-first divisor bound

For every real \(\theta\), Abel summation and the geometric progression give

\[
\left|\sum_hu_{L,H}(h)e(h\theta)\right|
\ll\min\left(1,\frac1{L\|\theta\|}\right).
\]

Apply this with \(\theta=X/d\). Choose an integer \(m_d\) nearest to
\(X/d\), and put \(n_d=dm_d\). Then

\[
|X-n_d|=d\|X/d\|\ll D,
\]

and each fixed \(n\asymp X\) has at most \(\tau(n)\ll_\varepsilon
X^\varepsilon\) participating divisors. Hence

\[
\boxed{
B_1(D,L;X)\ll_\varepsilon
X^\varepsilon\left(1+\frac DL\right).}
\]

This estimate is pointwise, includes exact-square resonances, and is valid
for both frequency signs. On the terminal line

\[
L\asymp H_D\asymp DX^{-1/4},
\]

it proves \(B_1(D,L;X)\ll_\varepsilon X^{1/4+\varepsilon}\) uniformly for
every \(X^{1/4}\le D\le X^{1/2}\). At the hard top endpoint it also bounds
the terminal shell of the accepted transformed M1 cone at the normalized
\(L^{3/2}X^\varepsilon\) scale. Lower and intermediate shells are not
implied.

## Certified exponent-pair wedge

Resolve the spatial character exactly into the two residue classes
\(d\equiv1,3\pmod4\). On each class it is constant, and after writing
\(d=4n+r\), the phase is a shifted reciprocal model phase with a fixed-BV
sampled profile. The audited exponent pair

\[
(\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right)
\]

therefore gives

\[
B_1(D,L;X)\ll_\varepsilon
X^{[89(1+\ell)+819\delta]/1282+\varepsilon},
\qquad D=X^\delta,\quad L=X^\ell.
\]

The target region is exactly

\[
\boxed{178\ell+1638\delta\le463.}
\]

This is a fixed-profile pointwise theorem, not a character saving for
arbitrary coefficients. The source theorem and pair are recorded in the
project's existing primary-source card; Round 10 independently checked the
M1 residue-class transfer. The source search found no theorem that closes
the remaining triangle. Robert--Sargos, Kowalski--Robert--Wu, and
Bettin--Chandee have different multi-variable or modular-inverse phases and
are retained only as strategic analogies.

## Exact direct phase diagram

Let

\[
\Omega=\left\{(\delta,\ell):
\frac14\le\delta\le\frac12,\quad
0\le\ell\le\delta-\frac14\right\}.
\]

The promoted direct bounds cover:

1. the TTY wedge \(178\ell+1638\delta\le463\);
2. the full terminal line \(\ell=\delta-1/4\);
3. the isolated second-derivative endpoint \((\delta,\ell)=(1/2,0)\).

Naive Abel summation against bounded partial sums of \(\chi_4\) costs the
total phase variation \(hX/D\), not merely the one-step derivative
\(hX/D^2\), and adds no active target region beyond the trivial left edge.
Consequently the exact uncovered region relative to these proved methods is

\[
\boxed{
\mathcal U_1=
\left\{(\delta,\ell)\in\Omega:
0\le\ell<\delta-\frac14,
\ 178\ell+1638\delta>463
\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.}
\]

At \(D=X^{1/2}\), the terminal and bounded-frequency endpoints are solved,
but every fixed middle exponent \(0<\ell<1/4\) remains in \(\mathcal U_1\).

## Status and next kernel

Round 10 proves genuine new M1 regions but not full M1. The next narrow
interface is the frequency-first near-product expansion before absolute
values: retain the truncated character-divisor coefficient

\[
A_D(n)=\sum_{\substack{d\mid n\\d\asymp D}}
\chi_4(d)w_D(d)
\]

through the coherent window \(|n-X|\lesssim D/L\), with the actual kernel's
dependence on \((X-n)/d\). Any improvement in \(\mathcal U_1\) must exploit
cancellation or sparsity in this signed short-interval divisor structure, or
an equivalent two-variable product-phase estimate. M9-M1, M9-M2, M9, and the
Gauss-circle target remain open.

No numerical experiment was used. The round remained entirely analytical.

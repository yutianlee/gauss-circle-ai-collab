# Round 83 conductor dual-normalization review

Campaign: `m9-m1-nonzero-residue-offset-dispersion`

Starting graph SHA-256:
`abbec651f0dc76e3e15408ce7fce76700aee01652d88db261d84f83815bdb112`

## Decision

The all-class inverse-unit reduction and the removal of the literal
dual difference (d=0) are exact.  They prove no power of (B=C/T),
but they replace the raw nonzero residue-offset energy by a strictly
smaller centred (d\ne0) Kloosterman-product correlation.

## Local-unit normalization

Fix one compatible nonaxial component and choose the oriented coordinate
so that (k=\rho\sigma>0).  Put

\[
 g_\kappa=4\kappa,
 \qquad
 M_\kappa={4b\over g_\kappa},
 \qquad
 c=g_\kappa x.
\]

After the already accepted reciprocal correction is absorbed into
(e(\pm A_{\kappa,b}/c)), the three local units have the exact form

\[
 u_{\kappa,b,k}(g_\kappa x)
 =\zeta_{\kappa,b,k}
 e_{M_\kappa}(K_{\kappa,b,k}\bar x),
 \qquad |\zeta_{\kappa,b,k}|=1,
\]

with

\[
 \begin{array}{c|c|c|c}
 \kappa&g_\kappa&M_\kappa&K_{\kappa,b,k}\\ \hline
 1/4&1&4b&k\\
 1/2&2&2b&2[k\bar4]_b\\
 1&4&b&[k\bar4]_b.
 \end{array}                                             \tag{83.N1}
\]

For (c=2x\equiv2\pmod4), the accepted representative satisfies

\[
 bs_0+\rho=2tx,
 \qquad
 \chi_4(s_0)=-\chi_4(b)\chi_4(\rho)(-1)^t.
\]

Consequently

\[
 \chi_4(s_0)e_{2b}(\sigma t)
 =-\chi_4(b)\chi_4(\rho)e_b(k\overline{4x}),
\]

which is the middle row of (83.N1) after lifting from modulus (b) to
(2b).  For (c=4x), the same antecedent gives

\[
 \chi_4(s_0)e_b(\sigma t)
 =-\chi_4(b)\chi_4(\rho)e_b(k\overline{4x}),
\]

which is the last row.  The odd row is the accepted
(e_{4b}(k\bar c)).  Thus no even class is inferred by parity analogy.
In every class,

\[
 u(gx)\overline{u(g(x+a))}
 =e_M\!\left(Ka\,\overline{x(x+a)}\right).              \tag{83.N2}
\]

The reflected endpoint orientation conjugates the same formulas.

## Exact Poisson and offset algebra

Define

\[
 F_b(x)=V_{b,gx,k}^{(\kappa)}
 e\!\left(\epsilon{A_{\kappa,b}\over gx}\right),
 \qquad
 I_b(n)=\int_{\mathbb R}F_b(x)e\!\left(-{nx\over M}\right)dx,
\]

and

\[
 S(n,K;M)=\sum_{x\bmod M}^{*}e_M(nx+K\bar x).
\]

Poisson summation on the exact residue progressions gives

\[
 \sum_{x\bmod M}^{*}e_M(K\bar x)
 \sum_{\ell\in\mathbb Z}F_b(x+M\ell)
 ={1\over M}\sum_{n\in\mathbb Z}S(n,K;M)I_b(n).        \tag{83.N3}
\]

For

\[
 \mathcal C_{M,K}(d,a)
 ={1\over M}\sum_{n\bmod M}
 S(n+d,K;M)\overline{S(n,K;M)}e_M(-an),
\]

finite orthogonality gives

\[
 \mathcal C_{M,K}(d,a)
 =\sum_{\substack{y\bmod M\\(y(y+a),M)=1}}
 e_M\!\left(d(y+a)+K(\overline{y+a}-\bar y)\right),    \tag{83.N4}
\]

and

\[
 \mathcal C_{M,K}(d,0)=c_M(d).                          \tag{83.N5}
\]

The residue offset (a=0) is therefore exactly the same-residue mode
already removed in Round 82.  Removing it once and then separating the
literal integer difference (d=0) yields

\[
 \mathfrak X_C^{(\kappa,k)}
 =\mathfrak Z_C^{(\kappa,k)}+\mathfrak Y_C^{(\kappa,k)}, \tag{83.N6}
\]

where

\[
 \mathfrak Z_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_n
 \bigl(|S(n,K;M)|^2-\varphi(M)\bigr)|I_b(n)|^2          \tag{83.N7}
\]

and

\[
 \mathfrak Y_C^{(\kappa,k)}
 ={1\over M^2}\sum_{b\asymp B}\sum_{d\ne0}\sum_n
 \bigl(S(n+d,K;M)\overline{S(n,K;M)}-c_M(d)\bigr)
 I_b(n+d)\overline{I_b(n)}.                              \tag{83.N8}
\]

Here (M=M_{\kappa,b}) inside the (b)-sum.  In particular,
(d\equiv0\pmod M) with (d\ne0) is retained in (83.N8).

## Target-safe zero-difference bound

The exact sampled Parseval identity is

\[
 \sum_n|I_b(n)|^2
 =M\sum_{h\in\mathbb Z}
 \int F_b(x+hM)\overline{F_b(x)}\,dx.                   \tag{83.N9}
\]

The (h=0) term is (O_\varepsilon(X^\varepsilon C/g)).  On every
nonzero overlap, the reciprocal phase difference is monotone and has
derivative

\[
 \asymp {g|h|Q^2\over C}.
\]

The accepted global symbol BV bound and the first-derivative lemma give

\[
 \int F_b(x+hM)\overline{F_b(x)}\,dx
 \ll_\varepsilon X^\varepsilon{C\over gQ^2|h|}.
\]

Since (Q^2/C\ge J^{1/20}) throughout the frozen band, summing the
overlaps proves

\[
 \sum_n|I_b(n)|^2
 \ll_\varepsilon X^\varepsilon M{C\over g}.             \tag{83.N10}
\]

The theorem-free estimate (|S(n,K;M)|\le M) already gives

\[
 \mathfrak Z_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon B^2C
 =X^\varepsilon{C^3\over T^2}
 \ll X^\varepsilon{J^2\over T}                         \tag{83.N11}
\]

for (C\le J^{3/4}).  The standard Weil--Estermann bound, together
with ((K,M)=O_k(1)), sharpens this to

\[
 \mathfrak Z_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon BC
 =X^\varepsilon{C^2\over T},                            \tag{83.N12}
\]

but the weaker internal estimate (83.N11) is already sufficient for the
promoted reduction.

## Scope

Equations (83.N1)--(83.N11) concern only the transition-flattened smooth
nonaxial principal row in (J^{13/18}<C\le J^{3/4}).  They prove no
(B^{-\delta}) gain, conductor extension, transition or axial estimate,
cone-edge estimate, full `M9-M1`, `M9`, or global exponent.  The first
remaining inequality is the signed bound for (83.N8) with its actual
Fourier weights.

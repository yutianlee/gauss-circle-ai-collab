# Source Card: Banerjee–Khurana twisted-divisor Voronoi formulas

## Bibliography

Debika Banerjee and Khyati Khurana, “Character analogues of Cohen type
identities and related Voronoi summation formulas,” arXiv:2306.12399v2
(2023).

- [Abstract and source](https://arxiv.org/abs/2306.12399)
- [Primary PDF](https://arxiv.org/pdf/2306.12399)
- Local PDF: `sources/papers/banerjee_khurana_2023.pdf`
- SHA-256: `434E3C01D841D2DCC5F7762AC4F1F9FC5ADD290E3644F502210490591CCAF22C`

## Exact coefficient match

Their equation (5.11) states

\[
 \sum_{n\ge1}\frac{\overline\sigma_{z,\chi}(n)}{n^s}
 =\zeta(s-z)L(s,\chi),
 \qquad
 \overline\sigma_{z,\chi}(n)
 =\sum_{d\mid n}d^z\chi(n/d),
\]

for (Re s>\max(1,1+Re z)). Therefore the project's coefficient is
exactly

\[
 \tau_{\chi_4,z}(n)=\overline\sigma_{-z,\chi_4}(n).
\]

Theorems 4.3–4.4 give Voronoi-type formulas for an odd primitive
character, with an analytic test function on a finite interval,
nonintegral endpoints, and (0<\Re\nu<1/2). Their dual kernels are explicit
combinations of (J_\nu,Y_\nu,K_\nu) at (4\pi\sqrt{nt/q}).

## Scope restriction

The source proves exact fixed-parameter identities. It does not state
quantitative bounds uniform for arbitrarily large imaginary order, nor a
maximal estimate for the project's hard top (1/u) Perron mode. It therefore
does not prove GAR or a new M1 exponent region.

Audit status: `completed_primary_source_audit`.


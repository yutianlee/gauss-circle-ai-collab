# Source Card: Gao 2026 smooth-number Gauss count

## Bibliographic data

Peng Gao, *On the Gauss circle problem over smooth numbers*,
arXiv:2604.23918v1 [math.NT], submitted 27 April 2026.

- Abstract record: https://arxiv.org/abs/2604.23918v1
- Primary HTML: https://arxiv.org/html/2604.23918v1

## Exact results audited

For

\[
 \Psi_G(x,y)=\sum_{\substack{n\le x\\P(n)\le y}}r(n),
 \qquad x=y^u,
\]

Theorem 1.1 proves the saddle-point asymptotic

\[
 \Psi_G(x,y)=
 \frac{4x^{\alpha_G}H(\alpha_G,G;y)}
 {\alpha_G\sqrt{2\pi\phi_2(\alpha_G,G;y)}}
 \left(1+O(1/u)\right)
\]

for fixed \(\varepsilon_0>0\),
\((\log\log y)^2\le u\le y^{1/(2+\varepsilon_0)}/\log y\),
and sufficiently large \(y\). Theorem 1.2 gives asymptotics for the
saddle point and main term when \((\log x)^{2+\varepsilon_0}<y<x\).

## Project interface audit

The theorems count only integers friable in the prime-factor sense and
prove an asymptotic for that restricted weighted count. The project's
"smooth M1" is a physical block classification, not a friability
condition. The source contains neither the literal hard/smooth M1
coefficient, the remaining \(P_2\) boundary/sign/gcd masks, an M2 owner,
nor a deterministic upper bound for the unrestricted discrepancy.

## Audit status

Current primary v1 through 31 August 2026. This is a relevant new
Gauss-circle variant but supplies no project theorem or exponent.

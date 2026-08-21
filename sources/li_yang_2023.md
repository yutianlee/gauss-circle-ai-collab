# Source Card: Li--Yang 2023

## Bibliographic data

Xiaochun Li and Xuerui Yang, *An Improvement on Gauss's Circle Problem
and Dirichlet's Divisor Problem*, arXiv:2308.14859v2 [math.NT], revised
14 September 2023, 32 pp.

- Local source: `rounds/web-research-test/Li-Yang-arXiv-2308.14859v2.tex`
- Record: https://arxiv.org/abs/2308.14859
- Primary HTML: https://arxiv.org/html/2308.14859v2
- ArXiv-issued DOI: https://doi.org/10.48550/arXiv.2308.14859

The arXiv record contains only v1 and v2. As checked on 17 August 2026,
the current author page still labels the item a preprint; no journal
version or public erratum was found.

## Exact theorem used

Only the following narrow repaired theorem is imported:

\[
 R(X)=\sum_{m^2+n^2\le X}1-\pi X
 \ll_\varepsilon X^{\theta_{\rm LY}+\varepsilon}
 \qquad(X\ge2\text{ real}),
\]

where

\[
 \theta_{\rm LY}
 =\frac{3292+25\sqrt{1717}}{13762}
 =0.3144831759740614\ldots .
\]

This is exactly the project's inclusive discrepancy
\(P(X)=N(\sqrt X)-\pi X\). The general Li--Yang Proposition 3.1 and
Theorem 4.2 are not imported in their full printed generality.

## Literal corrections required

The v2 source and PDF contain four uniquely repairable defects:

1. Definition 4.1 (4.4) must have \(M<T^{7/16}\), not
   \(M<T^{-7/16}\). Li--Yang (5.11) and Bourgain--Watt v1 (4.3)
   both give the positive exponent.
2. Li--Yang (5.18) must read \(H=MT^x\), because
   \(-3/8<x\le-\theta_{\rm LY}\) and every later substitution uses
   \(H/M=T^x\).
3. The duplicated circle sawtooth term is replaced by the exact two-sign,
   two-range identity in Bourgain--Watt v1 (7.2).
4. The isolated \(\sqrt{-1-14x}\) in (5.27) is
   \(\sqrt{-1-8x}\), as forced by the adjacent equations and direct
   algebra.

Lemma 3.4 also swaps the names of the null and circular plate exponents
in its prose. The subsequent localization conditions are geometrically
correct: \(k\) has width \(\eta^{\beta_1}K\) in the curved direction and
\(l\) has width \(\eta^{\beta_2}L\) in the flat direction.

## Two restricted-range supplements

Guth--Maldague requires
\(\beta_1\in[1/2,1]\), \(\beta_2\in[0,1]\). Li--Yang check only the
first lower bound. Their printed Proposition 3.1 is therefore not proved
for every stated tuple. In the final circle range, however, with
\(H=MT^x\), \(q=q_x\), and \(N=N_A\), the missing condition is

\[
 \frac HR\ge\left(\frac NH\right)^{(q_x-4)/4}.
\]

Its exponent margin \(D(x)\) satisfies

\[
 200\frac{2}{q_x-2}D(x)
 =2\frac{2}{q_x-2}(1-14x)+164x+49\ge0,
\]

and squaring is equivalent to

\[
 50(1-14x)(-1-8x)-(192x+47)^2
 =-(8x+3)(3908x+753)\ge0.
\]

It has strict slack on the actual range
\(x>2\theta_{\rm LY}-1>-3/8\). Case B is easier after the verified
comparison \(N_B>N_A\).

The second branch of \(N_B\) exceeds \(N_A\) only under

\[
 H>M^{-27/23}T^{53/92}(\log T)^{2907/12880},
\]

so the general printed Case-B implication omits a logarithm. In the final
application,

\[
 H^{23}M^{27}\ge T^{202\theta_{\rm LY}-50}>T^{53/4},
\]

which supplies a fixed power margin and therefore the missing logarithm.

## Withdrawn Bourgain--Watt boundary

ArXiv:1709.04340 was withdrawn because its Propositions 2, 3, and
\(1'\), hence Theorems 1--3, lost theorem status. The repaired Li--Yang
chain does not import those first-spacing estimates. It uses the
double-large-sieve/second-spacing formula with the first-spacing norm left
symbolic and the exact Section-7 sawtooth reduction; Li--Yang's restricted
small-cap argument supplies the replacement first-spacing estimate.

## Project map and scope

The repaired theorem gives a source-audited global pointwise exponent
strictly below \(1/3\). It does not prove the Round-95 rational-cluster
estimate, either M9-M1/M9-M2 canonical core, M9, endpoint uniformity for
the internal quarter route, or the \(1/4\) target.

## Audit status

`proved_external_dependency_with_explicit_repairs`

## Audited by

Round-95 source auditor and independent Codex conductor seam review,
2026-08-17.

## Evidence

- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reports/li_yang_strict_source_audit.md`
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/reviews/conductor_round95_li_yang_repair.md`
- `rounds/codex-managed/gc-strict-sub-one-third-cluster-source-fork/controls/li_yang_exact_arithmetic_check.txt`

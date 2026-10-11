# Round211 isolated statement: complete arithmetic hyperbola transfer

Read only this packet and protocol.md. No web, graph, strategy, sibling or
prior report. Write only reports/blind_hyperbola_transfer.md in this campaign.
Seven numbered protocol sections are mandatory. Stop after the report.

Let e(t)=exp(2pi i t), T>=2, 1<=N<=T, and R in a fixed positive compact
multiple of T. Let v be fixed smooth supported in[1,4], and Psi fixed real
Schwartz, smooth at zero. Define the complete finite complex block

    F_N(R)=sum_(n>=1) r2(n)n^(-3/4)Psi(sqrt(n/T))v(n/N)e(Rsqrt(n)),
    r2(n)=4 sum_(d|n) chi4(d).

Here chi4 is the nonprincipal real character modulo4. Real T,N,R and all
integer endpoints must be retained. An exact hyperbola decomposition may
use any integer cutoff1<=D<=4N; its two arms must cover every pair d*m in
the support, with no deleted overlap or assumed short-divisor complement.

You may assume one formal exponential-sum input, solely as a hypothesis.
For some fixed0<=kappa<=1/2 and1/2<=lambda<=1, every partial interval in
an interval of length comparable to K and with positive arguments comparable
to K obeys

    |sum_k e(A sqrt(k/K))|
       << (A^kappa K^(lambda-kappa)+K/A) T^epsilon,

uniformly for K>=1 and A>=K, and for the bounded fixed rescalings and shifts
of its normalized square-root phase needed to restrict k to one residue
class modulo4. Constants depend on the compact comparability bounds and
epsilon, not on A,K,T or interval endpoints. Short intervals with O(1)
integers may instead use the trivial bound. Explain the role of this exact
uniformity; do not silently enlarge the hypothesis to arbitrary weights.

Question: derive or refute a complete upper bound for F_N by using this
input on one inner variable in each exact divisor arm, with every smooth
amplitude, arithmetic coefficient, endpoint and outer summation restored.
Optimize the hyperbola cutoff and price all error and small-length terms.
Make no claim that the formal input holds for an unlisted pair.

For comparison, assume as supplied complementary estimates

    |F_N(R)| << T^epsilon min(N^(1/4),(T/N)^(1/2))

on1<=N<=T, and a complete Poisson--Bessel reconstruction

    |P(R^2)| << T^(1/2+epsilon)
       [1+sum_(dyadic1<=N<=T)|F_N(R)|],

where the singleton and the entire N>T tail have already been paid by1.
These two displayed estimates are hypotheses in this packet, not facts to
establish or promote. Use them to compute the complete pointwise exponent
licensed by your result, and an exact criterion for a formal exponent pair
to improve any specified radius-wave threshold b in(0,1/6). Also determine
what a family of pairs approaching(0,1/2) would suffice to prove and whether
one fixed nonendpoint pair alone gives the quarter theorem.

Required controls: exact coverage of both hyperbola arms; period-four
character restriction versus arbitrary coefficients; cutoff rounding and
real endpoints; derivatives/partial summation and O(1) lengths; distinction
between upper-certificate optimization and a lower bound for F_N; complete
reconstruction and the full-quarter quantifier. No computation is needed.

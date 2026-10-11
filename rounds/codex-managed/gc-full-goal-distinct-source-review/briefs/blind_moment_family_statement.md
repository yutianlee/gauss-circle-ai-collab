# Round217 isolated even-moment cutoff and full-goal certificate

Read only protocol.md and this packet. Do not read graph, manifest,
strategy, general generated brief, prior or current reports, sources or
web. Write only reports/blind_moment_family.md in this campaign; seven
numbered protocol sections. Stop after the report; no successor work.
Metadata graph SHA256:f7c8b74e9acaa3bf5234c3678f20e2aaf8dbb9ba6179f73d839fa2f0537a14d7.

Let q=136/13 and 1/8<beta<13/100, with beta(q-2)>1. For real T>=2,
0<=alpha<=4beta and Q=floor(T^alpha), suppose real functions B,L,Z
on the window [T/2,2T] satisfy B=L+Z, sup|B|<<T^(beta+epsilon),
sup|L|<<Q^(1/4), and for F=B,L,Z and V>=1,

    integral w(R/T)1_(|F|>V)dR
        <<_epsilon T^epsilon[V^-2+T V^-q].

The fixed w>=0 is smooth with support in[1/2,2]. Assume Z=sum_(d>Q)f_d,
|f_d|<=A_d, sum_d A_d finite for each T, and for every fixed integerh>=2,
sum_(d>Q)A_d^h<<_(h,epsilon)Q^(1-3h/4+epsilon).
All functions are measurable; every implicit constant may depend on
the fixed order and alpha. Constants need not be uniform in order.

For each fixed even p>=4 define the ordered distinct-index polynomial
E_p=sum_(d_1,...,d_p pairwise distinct)product_j f_(d_j), and the real
signed integral I_p=integral w(R/T)E_p. Do not assert positivity of E_p.

Derive independently a complete finite identity and its infinite limit,
then the best power certificate obtained by bounding its non-singleton
power sums in supremum, retaining signed powers of the full Z and using
the moment estimates supplied by the above distribution and ceilings.
Include the head's full p-moment, all partitions, low levels, floor,
borderline logarithms and the real signed-integral direction of transfer.

As a hypothetical diagnostic grant I_p<=C_(p,epsilon)T^(1+epsilon)
at each tested p and alpha; this is an additional unproved hypothesis.
Optimize the resulting one-pass complete p-moment certificate over
0<=alpha<=4beta, and compare the restored exponent

    Theta(p)=[p/4+(1+max(1,E(p)))/2]/(p+1)

as p runs through unbounded fixed even integers. A lower bound for this
certificate is not a lower bound for an actual moment. Do not assume
that an insufficient one-pass certificate proves every recursive use
impossible: determine exactly whether a repeated lower-moment argument
can improve the conclusion under the stated hypotheses, which uniform
availability in (p,alpha) that would require, and whether an endpoint
such as alpha=0 has different implications. State each extra premise
explicitly. No arithmetic origin is granted for the functions.

Controls: p=4 and p=12; fewer than p indices; coincident/vanishing
functions; alpha=0; transitions across q; strict epsilon allocation;
fixed p versus p growing with T; no positivity or finite-time independence.

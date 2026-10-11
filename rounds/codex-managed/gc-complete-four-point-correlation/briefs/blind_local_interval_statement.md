# Round212 isolated local discrepancy transfer

Read only this packet and protocol.md. No graph, strategy, prior report,
sibling context or web. Write only this campaign's
reports/blind_local_interval_transfer.md, seven numbered protocol sections.
Stop after the report. This is a conditional analytical problem, not a
request to assume or prove arithmetic randomness.

Let T>=2, R in a fixed compact positive multiple of T, fixed0<b<1/6,
and T^(4b)<N<T^(1-2b). Fix real smooth g_N supported in[N,4N] with
g_N^(j)<<_j N^-j. Let integer L=max(2,ceil(N^(1/2)T^(-2b))) and
K=max(2,ceil(NT^(-4b))). For1<=h<L,1<=k<K define

    W_(h,k)(t)=g_N(t)g_N(t+h)g_N(t+k)g_N(t+h+k),
    phi_(h,k)(t)=R[sqrt(t+h+k)-sqrt(t+k)-sqrt(t+h)+sqrt(t)],
    D_(h,k)=sum_n a_(h,k)(n)W_(h,k)(n)e(phi_(h,k)(n)),
    A4=(LK)^(-1)sum_(h,k)|D_(h,k)|,
    Lambda_(h,k)=Thk/N^(3/2),
    ell_(h,k)=N/(1+Lambda_(h,k)).

The sequences are zero extended to the whole real overlap. The actual
application would have a_(h,k)(n)=r2(n)r2(n+h)r2(n+k)r2(n+h+k), but
the following input is purely hypothetical and must remain labeled so.

Suppose genuine real smooth densities mu_(h,k)(t) on a fixed enlarged
positive compact multiple of N satisfy |mu^(j)|<<_j T^epsilon N^-j.
For fixed0<=nu<=1 and eta>=0 suppose, uniformly in h,k and every real
interval(u,v] in that region of length at most ell_(h,k),

    |sum_(u<n<=v) a_(h,k)(n) - integral_u^v mu_(h,k)(t)dt|
                      << T^epsilon N^eta ell_(h,k)^nu.

No claim of this input is made for r2; constants may depend on fixed nu,
eta,b and the masks, not on the shifting intervals or R. The scale ell
uses T, not a different choice at each R. A weaker alternative is the
same bound on every real prefix within a partition of the overlap into
cells of length at most ell; state the precise partition requirements.

Derive, refute or repair a complete upper bound for A4 under this input.
Retain every cell-boundary term, main density integral, small shift product,
repeated shift h=k, exact integer L,K, bounded T and real endpoints.
Derive the exact criterion on nu,eta,b for this route to supply A4<<T^(4b)
up to epsilon on every required scale. Explain what the hypothetical local
square-root case nu=1/2,eta=0 would certify at b=83/650, and its full-quarter
limits. Do not replace an unweighted global discrepancy by the stronger
local input without proof. Establish each phase derivative actually used.

For consequence only, you may assume the finite physical bridge
|F_N|^4<<T^epsilon[N/L^2+N/K+A4] and a complete reconstruction with
already paid complements so that F_N<<T^b on the band gives
P(X)<<X^(1/4+b/2+epsilon). These are hypotheses, not claims to promote.
No numerical experiment is needed.

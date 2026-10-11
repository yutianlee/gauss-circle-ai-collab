# Isolated round221 fixed-vector Gram statement

Read only protocol.md and this packet. No graph,manifest,strategy,
application,source or sibling file. Disclose prior-agent history.
Write seven numbered protocol sections only at
rounds/codex-managed/gc-actual-vector-gram-correlations/reports/blind_anchored_gram.md.

Let U be any J by n complex matrix, b in C^n, B=b*b, f=Ub,
G=UU*, M=U*U. Here * is conjugate transpose. Let k>=1 be a fixed
integer. Derive and prove the exact chain identity

    a_k=b* M^k b=f* G^(k-1) f,

including its fully indexed expansion in the fixed coefficient vector
and row Gram kernels. Prove the sharp inequality a_1^k<=B^(k-1)a_k,
and its consequence if |f_j|>=v>0 for every row. Treat B=0 and every
singular/rank-deficient case. Give equality conditions where meaningful.

Also derive the exact content of positivity of the bordered matrix
[[B,f*],[f,G]] using the Moore-Penrose inverse. Determine necessary and
sufficient conditions on f,B for the existence of SOME vector c with
Uc=f and ||c||²<=B. Prove the statements using finite spectral/orthogonal
decomposition. Distinguish existence of c from information about the
prescribed fixed b. Determine what is lost if a_k is bounded only by
B||G||^k, or the coefficient-vector endpoints in a chain are replaced
by generic Cauchy bounds.

For the finite exponential example U_(j,n)=sqrt(mu_n)e(t_j lambda_n),
mu_n>=0, real lambda_n, e(x)=exp(2pi i x), and a fixed real coefficient
vector b, explain simultaneous translation of all t_j. Derive how G and
f change, and give an exact finite control with nonnegative b showing
that G and B alone do not determine the size of f. No special arithmetic
frequency assertion is requested. Explain whether adding the b row to
the Gram matrix proves an upper bound on its new off-diagonal entries
without a further estimate. Do not infer an analytic theorem from PSD.

Required output: result; exact hypotheses; proof; first unproved or
unsupported step in a prospective use; exact controls; dependencies and
isolation provenance; recommended state effect. Zero experiments/web.
Stop after this assigned finite report.

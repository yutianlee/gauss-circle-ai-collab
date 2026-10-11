# Statement-only review: fixed-norm cosine packet

Read protocol.md and this statement only. Do not read discovery reports, any other admission brief, graph, history or conductor computations. This task is an independent rederivation, not promotion. Write only strategy/round231_admission/reviews/blind_cosine_packet_rederivation.md with the seven protocol sections. Stop after the report and provide its SHA256.

Let w be fixed nonnegative smooth, compactly supported in [1/2,2], with positive integral. Use the Fourier convention w_hat(xi)=integral w(u) exp(-2 pi i u xi) du. Let a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)), with Psi the real even Schwartz Fourier transform of a fixed smooth radial nonnegative unit-mass mollifier. Set Q=floor(T^(2/5)), d(n)=the squarefree part of n.

Define the nonnegative certificate

 C_cos(T)=sum_(ordered n_1,...,n_12>=1, d(n_j)>Q pairwise distinct)
   |integral w(R/T) product_(j=1)^12 [a_(n_j)(T) cos(2pi R sqrt(n_j)-3pi/4)] dR|.

All 4096 cosine signs are summed before the modulus for each norm tuple. Harmonic tuples and distinct norm tuples are NOT summed before that modulus. Prove or refute C_cos(T)>=c T^(5/2) for all sufficiently large real T. Do not claim this for modulus after summing all harmonics for fixed squarefree labels, or for the signed full integral or moment.

You may use ONLY the following supplied elementary/accepted coefficient inputs in addition to basic analysis and algebra; audit the logical sufficiency of these inputs without opening their source proofs. Choose sufficiently small fixed c>0 and S_T={n in[cT,2cT]:d(n)>Q}; then a_n>=0, M_T=sum_(n in S_T)a_n is comparable to T^(1/4), and max_(n in S_T)a_n <=C_epsilon T^(-3/4+epsilon). For every sufficiently small fixed delta>0, the total product weight of ordered tuples in S_T^12 with pairwise distinct d(n_j) and |sum_(j=1)^6 sqrt(n_j)-sum_(j=7)^12 sqrt(n_j)|<=delta/T is at least c_delta T^(3/2) for all sufficiently large T. No other separation, randomness or cancellation is supplied.

If the claim holds, identify exactly why it does not refute a bound of order T^(29/25+epsilon) for the fully signed sum. State whether a further harmonic or cross-norm grouping remains outside the result. No computational proof; any finite checks are diagnostic only.

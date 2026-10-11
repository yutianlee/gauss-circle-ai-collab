# Round223 isolated oscillatory Fourier transfer packet

Read only protocol.md and this packet. Prove or correct the assertions below
without reading any campaign, graph, source, sibling or application file.
Disclose prior-agent history. No web, experiments or successor. Write only
reports/blind_oscillatory_transfer.md in this campaign, seven numbered
protocol sections, and stop after the final hash.

Use e(t)=exp(2pi i t). Let 0<a<b, nonzero W in C_c^infinity((a,b)), and real
phi smooth on a neighbourhood of [a,b], with |phi''| bounded below by a
positive constant. Fix these profiles. For lambda>=1 set

    F_lambda(x)=W(x)e(lambda phi(x)),
    Fhat_lambda(u)=integral_R F_lambda(x)e(-ux)dx.

1. Derive upper and lower bounds c sqrt(lambda)<=integral|Fhat_lambda(u)|du
<=C sqrt(lambda), with constants and their profile dependence stated.
Give a proof of both the stationary band and nonstationary tail, including
complex/sign-changing W. No claim of uniformity over varying profiles is
supplied. Establish the needed inversion and integrability.
2. For real N>=1 and arbitrary finite complex coefficients c_n indexed by
integers, put S(alpha)=sum_n c_n e(n alpha). Derive the exact identity

    sum_n c_n F_lambda(n/N)
      = integral_0^1 G_(lambda,N)(alpha) S(alpha) d alpha,
    G_(lambda,N)(alpha)=N sum_(m in Z) Fhat_lambda(N(alpha+m)).

Define the absolute periodization

    A_(lambda,N)(alpha)=N sum_m |Fhat_lambda(N(alpha+m))|.

Prove the legal weighted bound by integral A|S| and determine integral A.
Keep G and A distinct. Any conditional majorant for |S| must hold at the
frequencies where it is used; an exceptional subset cannot be omitted.
3. Test whether the sqrt(lambda) LOWER bound automatically transfers to
integral|G|, the sampled sum, or an optimal discrete norm. For the control,
take N=1, W supported in (1/2,3/2) with W(1) nonzero, and phi(x)=sqrt(x).
Determine G exactly, including Fourier signs, and its L1 norm for every
lambda. Explain the precise limitation of an absolute-transfer lower cost.
4. State what changes if a claimed application uses a non-smooth cutoff,
row-dependent profiles or a varying curvature constant. Do not assert an
unsupported extension; distinguish missing hypotheses from impossibility.

No source theorem, arithmetic coefficient sequence, actual signed lower
bound or number-theoretic conclusion is included in the packet. This is an
isolated analytic transfer/control task, not a proof of a downstream bound.

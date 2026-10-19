# Round233 frozen interface: fixed-order distinct-class absorption

Date2026-10-12 Asia/Shanghai. Campaign `gc-fixed-order-moment-absorption`. Starting graph SHA256 `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. User continuation explicitly selected Wolfram. This is a different complete-parent reduction after the mandatory two-attempt upper-tail reassessment; it is not a third local product/cutoff attack and does not reset those two attempts.

Objective: prove or reject an all-fixed-even-order complete reduction by absorbing repeated-class terms, with full actual harmonic tails, head, sharp reconstruction and quantifiers. Do not estimate an unproved signed integral by declaration. A proved reduction is not a complete moment improvement.

Use the exact actual wave of accepted204/216: fixed nonnegative real radial smooth unit-mass mollifier in the unit disk, Psi its Fourier transform along a ray; fixed nonnegative smooth w supported[1/2,2], equal1 on[1/sqrt(2),sqrt(3)], dmu=w(R/T)dR. For real T>=2 set

    a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)),
    f_d(R)=sum_(s>=1)a_(d s^2)cos(2pi R s sqrt(d)-3pi/4), d squarefree,
    B=sum_d f_d, L_Q=sum_(d<=Q)f_d, Z_Q=sum_(d>Q)f_d,
    E_(p,Q)=sum_(ordered pairwise distinct d_1,...,d_p>Q) product f_(d_i),
    I_(p,Q)=int E_(p,Q)dmu, M_p(F)=int |F|^p dmu.

p is any fixed even integer>=2, chosen independently of T. Q>=1 may be real or an integer cutoff; membership is literal d>Q. Candidate regime: Q=1 or Q=floor(T^(1/p)). Inspect and derive the more general Q statement if useful. All constants may depend on fixed p, epsilon and fixed cutoffs; no uniform control as p grows with T is asserted.

Available actual amplitude arguments from216: A_d=sum_s |a_(d s^2)|<<r2(d)d^(-3/4), sum_(d<=Q)A_d<<Q^(1/4), and for fixed h>=2, sum_(d>Q)A_d^h<<_epsilon Q^(1-3h/4+epsilon). For each T the complete family is absolutely summable, including infinite harmonics; verify any extension beyond h12 rather than assume graph acceptance. The elementary finite divisor proof is available in the kernel.

New proposed mechanism TO PROVE: for real summable x_d, Z=sum x_d, V=sum x_d^2, E_p the ordered distinct polynomial, use the exact partition identity to obtain, for any fixed delta>0,

    |Z^p-E_p| <= delta |Z|^p + C_(p,delta) V^(p/2).

This is a relative bound and need not give the stronger additive error recorded in216. If valid, it can absorb repeated classes into M_p(Z) instead of paying them by T^((p-4)beta). Check all signs, p=2, zero V, finite family smaller than p, equal/opposite signs and infinite limits. In particular I_p is real but not assumed nonnegative.

Test whether this gives, at the actual-family level,

    M_p(B) <= C_p [I_(p,Q)+C_p T Q^(-p/4+epsilon)+M_p(L_Q)]

with a correct nonnegative interpretation and constants, plus a reverse bound for |I_(p,Q)|. Formulate equivalence of one-sided I targets and complete M_p targets only after explicitly paying the head/error budgets. The conjectured control above should imply an error floor O(T) for Q=1 and an order-independent polynomial head bound when Q=floor(T^(1/p)), but derive exact exponents rather than assuming them.

Restoration: verify the accepted leading sharp-circle amplitude/Jacobian and persistence argument. A complete normalized bound M_p(B)<<T^(b_p+epsilon) gives sharp moment powers max(1+p/4,(1+p/2+b_p)/2) in X=T^2, and the one-sided persistence denominator p+1. Recheck this formula from accepted sources. Determine whether an unbounded sequence of FIXED even p with b_p=o(p) would suffice for the quarter target; do not claim any such estimates have been proved. The proposed absorption must not silently substitute absolute tuple sums for the signed I or infer useful frequency separation from distinct radicals.

Required exit: precise lemma or failed certificate; first remaining arithmetic gap; actual full-owner and source scope audit; statement-only finite rederivation; nonauthor review; bounded Wolfram exact algebra independently reproduced locally; valid State Patch only after all gates. At least90 percent analytic/algebraic, at most10 percent bounded computation. Three initial tasks around10 minutes and one review/repair cycle. No successor design by agents.

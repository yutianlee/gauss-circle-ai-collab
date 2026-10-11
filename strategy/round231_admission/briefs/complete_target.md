# Round231 admission statement (not an analytic campaign)

Date: 2026-10-11. Predecessor Round230 is closed; analytic Round231 remains pending design. This is bounded selection work, following the repository's strategy/round*_selection precedent. Only the conductor may freeze or launch a campaign. No mathematical promotion is sought in this packet.

For fixed radial nonnegative smooth unit-mass rho and Psi its real even Schwartz Fourier transform, and fixed nonnegative smooth w supported on [1/2,2], equal to one on [1/sqrt(2),sqrt(3)], define
 a_n(T)=r2(n)n^(-3/4)Psi(sqrt(n/T)),
 B_T(R)=sum_(n>=1) a_n(T)cos(2pi R sqrt(n)-3pi/4),
 M12(T)=integral w(R/T)|B_T(R)|^12 dR.
Here r2(n)=4 sum_(d|n)chi4(d). Every harmonic, sign, unequal dyadic block, infinite Schwartz tail, all real T>=2 and all R in the window are part of the quantity. The accepted complete upper exponent is 10 beta, beta=2(3292+25sqrt(1717))/13762-1/2. Strict moment gain requires b12<10beta; strict pointwise gain requires b12<13beta-1/2. Preferred finite milestone b12<=29/25 yields pointwise102/325, not quarter.

Accepted216: Q=floor(T^(2/5)); f_d=sum_s a_(d s^2)cos(2pi R s sqrt(d)-3pi/4), d squarefree. Write L=sum_(d<=Q)f_d, Z=sum_(d>Q)f_d and E12=sum_(ordered pairwise distinct d_j>Q) product f_(d_j). Then M12(L)<=T^(15/13+eps), integral w|Z^12-E12|<=T^(8beta-1/5+eps). The target is equivalent to |I12|<=T^(29/25+eps), I12=integral w E12. Its exact expansion is T/2^12 sum_(distinct d_j>Q;s_j>=1;eps_j=+-1) product a_(d_j s_j^2) e(-3 sum eps_j/8) w_hat(-T sum eps_j s_j sqrt(d_j)). A one-sided upper bound suffices. This reduction is accepted only for order twelve, not an all-order bridge.

Barriers:217 termwise absolute Fourier certificate has a positive T^(5/2) subsum at order12, not a lower bound for signed I12. 218 whole Gaussian dual tuple modulus certificate is asymptotic T^7 despite internal tuple cancellation; cross-tuple signed cancellation remains possible. 219 anchored divisor characters become common label signs and oscillatory partners remain unpaid. 221 phase-insensitive fixed-vector Gram methods cannot improve the 10beta ceiling. 224 angular Hecke/prime amplification has actual-symbol, commutator, overlap and self-return costs;225 exact r2 logarithmic/Vaughan factorization, all prime powers and type I/II, restores81/614>beta. New work must identify which exact obstruction it bypasses.

Admission gates: a concrete arithmetic cancellation mechanism, exact complete quantity, an independently checkable new signed analytic input, a full restored power ledger, and a falsifying arithmetic control. A new identity alone does not justify Round231. If absent, keep231 pending; report narrowly what failed, not a universal impossibility theorem.

Resource budget: three bounded orthogonal selection reports, at most one nonauthor review per candidate, one statement-only algebra rederivation, at most two targeted primary source checks and one Wolfram symbolic diagnostic independently reproduced locally. At least95 percent analytic/algebraic, at most5 percent computation. Stop after assigned report. No successor, shared state, proof draft, matrix, synthesis or other reports may be edited.

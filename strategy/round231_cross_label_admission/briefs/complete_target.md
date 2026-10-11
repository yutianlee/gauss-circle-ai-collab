# Complete signed cross-label interface

Selection only, user says keep going. Round230 is closed, analytic231 unlaunched. Previous two admission packets are immutable. Objective: test a genuinely signed cross-label input by subtracting smooth frequency density before estimating the actual arithmetic discrepancy. A cancellation identity alone is not admission.

e(x)=exp(2pi i x); rho nonnegative radial smooth unit-mass supported unit disk; Psi(s)=rho-hat(s e1) is real even Schwartz, |Psi|<=1, Psi(0)=1, may change sign. w>=0 smooth support[1/2,2], equals1 on[1/sqrt2,sqrt3]. T>=2 real, Q=floor(T^(2/5)). r2(n)=4 sum_(k|n)chi4(k).
a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)); B=sum_n a_n cos(2pi R sqrt(n)-3pi/4); f_d=sum_(s>=1)a_(ds^2)cos(2pi R s sqrt(d)-3pi/4), d squarefree; Z=sum_(d>Q)f_d.
E12=sum_(ordered pairwise distinct sf d_j>Q)product_j f_dj; I12=integral w(R/T)E12(R)dR. J_d=integral w product f_d. All actual harmonics, signs, mixed blocks, real windows and tails required.

Accepted216: M12(B-Z)<<T^(15/13+eps); integral w|Z^12-E12|<<T^(8beta-1/5+eps), beta=(50sqrt(1717)-297)/13762=0.128966351948... . Thus a one-sided I12<=T^(29/25+eps) suffices and is equivalent at this power to complete M12(B). Accepted204 gives M12(B)<<T^(10beta+eps). Strict moment gain b<10beta; strict pointwise gain b<13beta-1/2;29/25 gives physical exponent102/325, not quarter.

Reviewed, NOT graph-promoted, previous screen: C_harm=sum_distinct_d |J_d|>=cT^(5/2) even after all harmonics/signs are pooled in each J_d. Only this absolute certificate is obstructed. Signed I12 may be small. Actual weighted squarefree mass sum_(sf d<=x)r2(d)=kappa x+O_sigma(x^sigma), for every fixed1/2<sigma<1, follows from r2 mu^2=h*r2, h-local1-z^2 at2/inert and1-3z^2+2z^3 at split primes. Do not assume this coarse result gives microscopic cancellation.

Earlier failures: Round210 full modulated bins preserve phases but available energy only variance times sup; Round218 actual lattice transform full absolute dual tuple certificate T^7; Round221 averaging actual fixed-vector Gram over common radius erases endpoint phases, gives phase-insensitive T^3 and an adversarial same-magnitude control atT^(10beta). New input must bypass, not rename, these failures. No graph changes in this screen.

Budget: three bounded orthogonal reports plus one review/repair cycle; at least95% analytical, at most5% exact diagnostics. No asymptotic simulation. Each report has seven protocol sections: result, exact hypotheses, derivation, first gap, control, exact provenance/isolation with hashes, state effect. Only assigned report, then stop; no next round or shared-state edits.

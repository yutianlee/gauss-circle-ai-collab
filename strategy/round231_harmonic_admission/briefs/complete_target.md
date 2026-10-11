# User-requested harmonic pooling admission test

Date 2026-10-11. Phase: bounded prelaunch admission for Round231; analytic231 is not launched. Previous strategy/round231_admission is frozen evidence and must not be edited. The user explicitly asks to pool ALL harmonics at each fixed squarefree-label tuple before taking absolute values. Test this new ordering rather than infer failure from the previous norm-tuple certificate.

Fix actual rho>=0 radial smooth, compactly supported in the unit disk, integral1, Psi(s)=rho_hat(s e1), and w>=0 smooth, support[1/2,2], equal1 on[1/sqrt2,sqrt3]. Psi is real even Schwartz with Psi(0)=1 and may change sign. For realT>=2 set a_n=r2(n)n^(-3/4)Psi(sqrt(n/T)), Q=floor(T^(2/5)), f_d(R)=sum_(s>=1)a_(ds^2)cos(2pi R s sqrt(d)-3pi/4), d squarefree. Define
 J_d(T)=integral w(R/T) product_(j=1)^12 f_(d_j)(R)dR,
 C_harm(T)=sum_(ordered pairwise distinct squarefree d_1,...,d_12>Q)|J_d(T)|,
 I12(T)=sum_(same d tuples)J_d(T).
All signs and the infinite harmonic series are pooled before each |J_d|. Mixed dyadic scales, all real endpoints and smoothing tails remain. Absolute convergence at fixedT follows from Schwartz decay and the coefficient bounds.

Accepted216: M12(B_T)<=T^(29/25+eps) is equivalent to |I12| at that power; head costT^(15/13+eps), repeated-class errorT^(8beta-1/5+eps). Thus C_harm at29/25 would suffice but is stronger than the signed target. Accepted full moment exponent10beta=1.28966351948..., beta=2(3292+25sqrt1717)/13762-1/2. Strict moment improvement requires b12<10beta; strict pointwise improvement b12<13beta-1/2; preferred29/25 gives102/325, not quarter. No all-order bridge is accepted.

Previous admission proved only C_cos>=cT^(5/2) when taking a modulus before different norm/harmonic tuples are pooled; this does NOT imply a lower bound for C_harm. It used positive actual block mass, a balanced near relation, and discarded every second nonparallel bounded sign relation by a two-variable completion bound. Harmonic pooling must be analyzed afresh; common harmonic multiples of a near relation remain near and cannot be discarded by that rank-two argument.

Admission: require an exact new signed input with improved COMPLETE restored power, not a regrouping identity or renamed target. If unsuccessful, state a scoped no-go or unresolved premise and leave231 pending. No graph promotion in this screen. Root owns all decisions, reviews, state and synthesis; agents write only assigned reports. Reports have seven protocol sections: result; exact hypotheses; proof; first gap; controls; dependencies with hashes/isolation; state effect. Stop afterward, no successor.

Budget: three orthogonal bounded reports; one statement-only rederivation of each crucial new seam; at most one repair/review pass; >=95 percent analytical/algebraic, <=5 percent bounded exact diagnostics, no broad source search or asymptotic simulations. All report I/O UTF-8.

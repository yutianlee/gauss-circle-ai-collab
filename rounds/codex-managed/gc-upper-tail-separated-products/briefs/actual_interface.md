# Frozen Round232 interface: pay close products, attack separated correlations

Campaign `gc-upper-tail-separated-products`; date2026-10-12 Asia/Shanghai. Starting graph `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`. This is attempt2 on the unchanged upper-tail premise, authorized by the user's continuation after closed231. At closure a strategy reassessment is mandatory if no complete gain; no automatic Round233.

Use the exact actual full smooth band from Round231: rho is fixed nonnegative real radial smooth unit mass in the unit disk, Psi(s)=rho-hat(s e1), w nonnegative smooth supported[1/2,2] and equal1 on[1/sqrt(2),sqrt(3)], dmu=w(R/T)dR, real T>=2. Eta is a fixed smooth cutoff zero below1 and one above2. Gamma=16/125, X=T^(64/125), Y=T^(93/125), phi(n)=eta(n/X)-eta(n/Y). F(R)=sum phi(n)r2(n)n^-3/4 Psi(sqrt(n/T))cos(2pi R sqrt(n)-3pi/4). E={R:|F(R)|>T^gamma} within the radius window. The accepted distribution gives mu(E)<<T^(-2gamma+epsilon) and the actual ceiling is T^(beta+epsilon), beta=(50sqrt1717-297)/13762. A sufficient OPEN target is Q_E=int_E |F|^2dmu<<T^(-a*+epsilon), a*=10beta-32/25=.009663519481... . This restores complete M12(B)<<T^(32/25+epsilon), with B=L+F+H and all complementary moments at32/25; it is only a moment improvement. Accepted theta=(1+2beta)/4.

Round231 supplies an exact second-Poisson leading representation over O(log^2T) smooth divisor rectangles j, D_j M_j~N_j, X/constant<N_j<constant Y:

    F(R)=sum_(j,p) P_(j,p)(R)+e_T(R), ||e_T||infinity<<T^(-1/2+epsilon),
    P_(j,p)(R)=4 T^(-1/2) sum_(h~H_j,h|p,p/h odd) chi4(p/h)
                   K_(j,h,R)((R^2-p)/W_j),
    W_j=T/sqrt(N_j), H_j=T D_j/sqrt(N_j).

Here p is a nonzero integer (h>0 and odd Fourier index q=p/h may be negative); K are real odd Schwartz kernels, with uniform fixed seminorms and slow R derivatives. The original amplitude without divisor factor4 is a_j(d,m); b_h(d,R)=a_j(d,R^2d/(4h^2))R sqrt(d)/(sqrt2 h^(3/2)); K=(sqrtT/2) int b_h(d,R)sin(pi W_j u d/(2h))dd. The explicit4 above owns the divisor identity once. All q are distinct Fourier indices, not repeated nearest-q labels. Both cosine branches are accounted for by the real part.

The reviewed local packet envelope, for p~T^2, is |P_(j,p)(R)|<<T^(-1/2+epsilon)(1+|R^2-p|/W_j)^(-A). Any use of this envelope for the full all-p second-Poisson representation must explicitly pay exterior/negative p tails and cross terms. They should be rapidly negligible, but verify. The full packet P_p=sum_j P_(j,p) retains all rectangles and cross terms. The common largest width is Wmax~T^(1-2gamma). No mask may inherit the actual F ceiling.

Frozen objective: rigorously remove exact and close integer-product pairs, and attempt the remaining actual signed separated-product contribution on E at power -a*. Use separation L=T^(1/2). Candidate close-pair estimate, to PROVE rather than assume:

    int_E sum_(|p-p'|<=L)|P_p P_p'|dmu
          <<T^(-2gamma+epsilon)(L+1)Wmax/T
          <<T^(-3/250+epsilon).

This is below the desired -a* if correct. Exact coincidences would have stronger budget T^(-4gamma+epsilon). The close quadratic form need not be positive; absolute payment is essential. The remaining one-sided signed target is

    2 sum_(p<p', p'-p>L) int_E P_p(R)P_p'(R)dmu <<T^(-a*+epsilon),

with all discarded tails, stationary errors and cross terms paid. Do not assert this bound. A conditional reduction alone is not a complete gain; attempt an actual quantitative estimate using the product-difference arithmetic.

Known sign classification: h=ga,h'=gb,(a,b)=1, r=aq-bq'. If a,b odd then chi4(q)chi4(q')=chi4(ab)(-1)^(r/2), constant within fixed r. If a,b have different parity, odd solutions advance by(2b,2a) and alternate. Actual localized distinct-frequency covariances can be positive of full size; blanket pairwise decorrelation is false. Round232 must pay same-product/near-product collisions instead of invoking it. Strong first-average cancellation or reflection of an odd kernel cannot control the actual indicator1_E. Any signed shift argument must retain actual weights, boundaries, all scales and the same E.

Budget: three orthogonal initial tasks around10-12 minutes, one bounded review/repair cycle. At least95% analytical/algebraic, at most5% bounded computation. Reports have seven protocol sections, exact context hashes, first gap and complete implication; candidate evidence only. Subagents write only assigned paths, freeze and stop. No next-round design by subagents.

# Isolated finite divisor-allocation statement

Read only this file and protocol.md. Do not read graph, campaign,
strategy, application, sibling or source files. Disclose retained prior
agent history; this is current statement-only isolation, not history-free.
No web or experiments. Write only reports/blind_prime_allocation.md in
this campaign, with seven numbered protocol sections and a final hash.

Let chi be the real character modulo4. For any array A on positive
integer pairs, define c_A(n)=sum_(hq=n)chi(q)A(h,q).
Every coefficient is a finite divisor sum. Let F be any finitely
supported complex function on positive integers, and set
L_A(F)=sum_n c_A(n)F(n). Put c_A(n/p)=0 when p does not divide n.
For an odd prime p, set epsilon_p=chi(p) and lambda_p=1+epsilon_p.

Independently derive and verify:

1. The exact decomposition of c_A(pn) in terms of the three arrays
U_pA(h,q)=A(h,pq), V_pA(h,q)=A(ph,q), W_pA(h,q)=A(ph,pq).
Every p-adic multiplicity and the overlap when p|n must be counted once.
Obtain an exact formula for
E_(p,A)(n)=c_A(pn)+epsilon_p*c_A(n/p)-lambda_p*c_A(n)
using differences of those arrays from A.
2. The finite adjoint identity for
T_p^*F(m)=1_(p|m)F(m/p)+epsilon_p F(pm), including the sign of E.
Sum it over any finite collection of odd primes without inferring
orthogonality. State separately what happens when epsilon_p=-1 and
when one attempts to extend the formulas to p=2.
3. For F_(X,N)(n)=1_(1<=n<=N)n^(-3/4)e(sqrt(Xn)), with real X,N>0,
derive all exact dilation amplitudes, phases, divisibility masks and
floored endpoints in T_p^*F. Keep the array A fixed during that identity.
The operator must not silently change A to a parameter-dependent array.
4. For the constant array A=1, prove the Hecke eigenrelation and its
prime-power recurrence, with the cases p=1 mod4, p=3 mod4 and2 separate.
Give an explicit finite control showing that the scalar identity alone
does not imply an automatic inverse-square-root saving in the number of
split primes against the coefficient triangle. Do not claim a universal
no-go for other norms, other arrays or coefficient-sensitive arguments.

All transformations must be exact at empty supports, n=1, p|n, p^2|n
and the terminal integer cutoff. No application bound or successor is
requested. Stop after the assigned seven-section report.

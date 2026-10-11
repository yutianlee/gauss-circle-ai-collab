# Round 209 isolated statement packet

Role: statement-only independent rederivation. Read only protocol.md and
this file. Do not read active state, general generated brief, other reports,
historical proofs or the web. Write only
rounds/codex-managed/gc-complete-signed-tenth-moment/reports/blind_ten_root_audit.md.
Seven numbered protocol sections required. Stop after report; no successor.

Let r2(n) count signed ordered representations as two squares. You may use
r2(n)<=4 tau(n)<<_epsilon n^epsilon, sum_(n<=y)r2(n)=pi y+O(sqrt(y)+1),
and linear independence over Q of distinct squarefree radicals. Fix a
nonzero nonnegative smooth v supported in [1,4], positive on an interior
interval, and real even Schwartz Psi with Psi(0)=1. For real T>=2 and
1<<N<=T^c, fixed c<1, set
a_n=r2(n)n^(-3/4)Psi(sqrt(n/T))v(n/N),
H_N(R)=sum a_n cos(2pi R sqrt(n)-3pi/4).
Let w>=0 be nonzero smooth compactly supported in (0,infinity),
w_hat(xi)=integral w(u)e(-u xi)du, e(t)=exp(2pi i t).

Independently prove or refute the following assertions, stating the
correct hypotheses and any needed repair. Do not assume they are true.

1. For every fixed k>=2 and every sign pattern, the exact 2k-root weighted
mass with all n in [N,4N] is O_(k,epsilon)(N^(-k/2+epsilon)), for weights
bounded by C tau(n)n^(-3/4). Non-pairing same-squarefree-class relations
must be included; zero exact mass for an impossible sign pattern is fine.
2. For k=5, the all-sign termwise absolute expansion with zero frequencies
removed is at least c N^2-C_epsilon T N^(-5/2+epsilon), for large T,N:
A10=(T/2^10)sum_signs sum_(Delta!=0) product|a_n| |w_hat(-T Delta)|,
Delta=sum sign_j sqrt(n_j). Give a uniform positive lower bound when
N=T^alpha, alpha in a fixed compact subset of (1/2,1). Relate it to the
proposed U=T^(83/65)N^(-1/2) for 166/325<alpha<242/325, without inferring
a signed lower bound. Consider whether the obstruction is an exact-resonance
artifact or instead persists after exact-frequency removal.
3. Explain the limitations: can this refute the actual tenth moment or
prove that cancellation after total-frequency aggregation is impossible?
Include a legitimate control showing why a displaced signed integral
can be much smaller than its termwise absolute expansion.

At most two analytic approaches, no mathematical numerical experiments.
An unproved step must be stated explicitly; absence of an actual estimate
is not a reason to invent one. State recommended evidence/state effect.

# Round207 isolated statement packet

Role: independent statement-only analyst. Read only this packet and
protocol.md. Do not read graph, campaign, general brief, strategy,
predecessors, claimant reports, siblings or external literature. Write
only rounds/codex-managed/gc-signed-rational-filter-attack/reports/blind_periodic_threshold.md.
Stop after the seven-section report. No authoritative state edits.

Let X tend to infinity, J=[X/2,3X], M=ceil(6X), D=floor(sqrt(M)),
L=floor(M/(D+1)). Fix eta smooth supported in [1/4,6], equal to1 on
[1/3,4], with0<=eta<=1. Let K be a real odd Schwartz function whose
Fourier transform, with e(-u*xi) convention, is supported in
[-2,-1] union [1,2]. Allow K to vary within a family with uniform
Schwartz seminorms. Put h(x)=c*sqrt(x)/sqrt(N) for fixed c>0, and
assume uniformly on J that h(x) is comparable to H, with
X^delta<=H<=X^(1/2-delta) for a fixed0<delta<1/4.
Define chi4(r)=0 for even r,1 for r=1 mod4,-1 for r=3 mod4.

Prove or refute each claimed statement with precise constants/ranges:

1. For every real x and h>0,
sum_(m in Z,m=b mod q)K((x-m)/h)
=(h/q)sum_(k in Z)Khat(hk/q)e(k(x-b)/q).
Consequently the full progression vanishes for q<h/2. Treat equality
q=h/2 and zero frequency carefully. Derive the exact analogous formula
for sum_(ell|m)chi4(m/ell)K((x-m)/h), including the mod4 Gauss factor.

2. For
R(x)=sum_(1<=ell<=L) sum_(m>=1,ell|m) eta(m/X)chi4(m/ell)
 *[1_(m>D*ell)-1_(x>D*ell)]K((x-m)/h(x)),
one has sup_J|R(x)|<<1 and integral_J|R(x)|^6 dx<<sqrt(X)*H.
Arbitrarily small O_A(X^-A) additions are allowed if explicitly derived.
No exceptional transition x=D*ell may be discarded. The index m and
threshold D*ell are integers; x is real and h varies as stated.

3. Replacing eta(m/X) and m>=1 by the full integer lattice, in sums of
O(sqrt(X)) periodic atoms with coefficients bounded by a constant,
has O_A(X^-A) total error for x in J after taking sufficient uniform
Schwartz decay. Explain any needed support buffer or qualification.

These are analytical statements only, not an arithmetic sixth-moment
theorem. If an assertion fails, give the first failed step and a concrete
control. Check a single jump, integer centers, q near the cutoff, small
ell, and remote thresholds. A counterexample for another coefficient
family must be labeled with its scope. Do not infer Gaussian moments.

Report sections:1 result;2 exact hypotheses;3 proof;4 first gap;
5 controls and outcomes;6 exact dependencies;7 recommended state effect.

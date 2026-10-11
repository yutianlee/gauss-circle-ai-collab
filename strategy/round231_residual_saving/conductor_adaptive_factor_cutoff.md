# Conductor strengthening: an adaptive divisor cutoff at the preferred moment budget

Round231 residual-saving admission; conductor derivation; 2026-10-11. Graph SHA256 a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b. Candidate evidence, subject to nonauthor review. No graph mutation.

## 1. Result

The actual unbalanced owner can be paid at M12<=T^(29/25+epsilon) with a substantially larger top-scale factor cutoff than the fixed-power preferred-budget decomposition. Use

    D_T(x)=T^(26/125-13/42) x^(29/84).

At x~T this is comparable to T^(853/3500)=T^0.2437142857..., while at the lower norm endpoint X0=T^(52/125) it equals X0^(17/168). This places every pair with a factor below the adaptive cutoff into an owner whose supremum is T^(13/125+epsilon) and whose complete twelfth moment is T^(29/25+epsilon).

The remaining owner is the exact central balanced divisor wave. No sufficient estimate for its signed moment is proved. The accepted complete exponent remains 10beta.

## 2. Exact statement and hypotheses

Use the actual wave, fixed smooth factors, real radii, norm head X0, upper cutoff Z=T^(3/2), and radius-independent ordered patch starts x(n) from briefs/residual_interface.md. On X0<n<=Z define

    u_*(n)=4 sum_(d|n, d<D_T(x(n))) [chi4(d)+chi4(n/d)],
    w_*(n)=4 sum_(dm=n, d>=D_T(x(n)), m>=D_T(x(n))) chi4(d).

Let U_*, W_* denote the corresponding real waves with the exact original n^(-3/4)Psi(sqrt(n/T)) cosine weight. Take large T, with the same bounded-T convention as the reviewed interface. Then

    r2(n)=u_*(n)+w_*(n),
    sup_(T/2<=R<=2T) |U_*(R)| << T^(13/125+epsilon),
    M12(U_*) << T^(29/25+epsilon).

The coefficient vectors depend on T but are fixed as R varies, as required by the accepted coefficient-uniform distribution estimate. They remain divisor bounded. Strict cutoff equality belongs to w_*.

## 3. Proof and complete restoration

Write a=26/125-13/42=-533/5250<0. The function D_T(x)=T^a x^(29/84) is increasing in x. Also D_T(x)/sqrt(x)=T^a x^(-13/84)<1 for T,x>1. Since n>x(n), its squared cutoff is strictly below n, so the two unbalanced hyperbola regions are disjoint. Swapping d and m in one region gives the displayed exact identity.

At x=X0 the T exponent of D is

    a+(52/125)(29/84)=(52/125)(17/168)>0.

Thus every retained cutoff exceeds one asymptotically. Comparability at shortened endpoint patches changes only fixed constants, and bounded parameters are absorbed separately.

For any fixed d on a shell n~N, the condition d<D_T(x(n)) holds on an interval because both x(n) and D_T are nondecreasing. Its intersection with the shell and global cutoffs is still one interval. Hence the reviewed proper-interval fibre bound in reports/actual_residual_attack.md applies before any absolute summation over d. The quotient character is split into the two odd residue classes modulo four exactly as in that proof; no arbitrary sign mask is permitted. The smooth amplitude plus its total variation has size O_L(N^(-3/4)(1+N/T)^(-L)).

Since all contributing d are O(D_T(N)), summing the fibre estimates gives

    sup |U_*,N| << T^epsilon (1+N/T)^(-L)
       [T^(13/84) N^(-29/168) D_T(N)^(1/2)
        + T^(-1) N^(-1/4)].

The first term is exactly T^(13/125), apart from shell comparability constants:

    13/84 + a/2 =13/125,
    -29/168 +(29/84)/2=0.

There is no patch-count loss. Summation over the logarithmically many shells X0<N<=Z, including partial first/last shells, proves the supremum bound. The T^epsilon factors absorb divisor and shell logarithms in the usual fixed-epsilon allocation.

The accepted coefficient-uniform distribution estimate therefore yields

    M12(U_*) << T^epsilon [T+T^(26/25)+T^(29/25)]
              << T^(29/25+epsilon).

This uses the independently proved U_* ceiling, not the actual full-wave ceiling on a mask.

The exact full restoration is

    B_T=H_X0+U_*+W_*+E_Z.

The head moment is T^(29/25+epsilon); the true infinite tail E_Z is arbitrarily small by the fixed Schwartz decay. A finite L12 norm inequality pays all mixed terms. Thus any new exponent b for W_* would restore the full moment at max(29/25,b). In particular any b<10beta suffices for strict complete gain, and b<=29/25 suffices for the preferred milestone.

Relative to the original residual, V=W_*+(U_*-Ssharp). Since the old Ssharp moment is T^(3044/2625+epsilon), the entire correction U_*-Ssharp is already paid at29/25. No arithmetic term has been discarded.

At x~T,

    a+29/84=26/125+1/28=853/3500.

Thus the central factor range there is approximately T^(853/3500)<=d,m<=T^(2647/3500). This is a sharper preferred-budget localization than any single fixed exponent alpha=17/168 across the entire norm range. It does not imply a smaller coefficient energy: the actual same-character semiprime control in the reviewed report still applies since both primes have order sqrt(T), exceeding this cutoff by a fixed power. Its lower bound remains a coefficient-energy statement only.

## 4. First unproved step

A signed physical moment bound M12(W_*)<<T^(b+epsilon) with b<10beta remains unproved. The exact identity gives only the inherited sup W_*<<T^(beta+epsilon), since both the head and the newly proved U_* ceiling are smaller. The generic distribution then recovers only10beta. An adaptive cutoff alone does not estimate signed cross-fibre correlations.

## 5. Controls

PASS algebraically: D is positive, increasing, exceeds one in the asymptotic range, and has D^2<x. Every divisor sees one proper interval. Character placements, cutoff equalities, endpoints, and bounded T are owned exactly. The exponent cancellation is an exact rational identity. The original approximant correction, norm head and infinite tail are paid in the complete norm. No complete gain or coefficient-energy gain is inferred. All work is analytical; a rational-arithmetic diagnostic independently checks the displayed exponents.

## 6. Dependencies

protocol.md; briefs/residual_interface.md; reports/actual_residual_attack.md (frozen SHA256 0d18fa59d915809427e1758ee478ba439303748738e8ec1f86d7e95060dd0bc5); the accepted finite distribution kernel and prior properly shifted interval exponent-pair estimate cited in that report. This extension was derived by the conductor after the fixed-alpha report was frozen and is assigned to its nonauthor source reviewer as part of the same single review cycle. No new external theorem is invoked.

## 7. Recommended state effect

Retain the improved adaptive factor localization as reviewed candidate evidence. It narrows the outstanding actual signed residual while paying the correction at the preferred complete budget. No State Patch, proof-draft change, complete-bound promotion or new numbered round follows.

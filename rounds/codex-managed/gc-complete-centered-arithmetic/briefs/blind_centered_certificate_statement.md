# Round 213 isolated statement packet

Read only this packet and protocol.md. Do not read the graph, manifest,
strategy, generated general brief, prior reports, siblings or web. Write
only reports/blind_centered_certificate.md in this campaign, then stop.
Use seven numbered protocol sections. Role: statement-only rederivation.
Graph hash supplied for metadata only:
4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

Let b=83/650, T tend to infinity, N=T^alpha for fixed
4b<alpha<1-2b. Set L=max(2,ceil(sqrt(N)T^-2b)),
K=max(2,ceil(NT^-4b)), U=N^(3/2)/T, Lambda_s=hk/U for s=(h,k),
and Omega={1<=h<L,1<=k<K,h!=k,Lambda_s>1}.

For each s there is a real C-infinity function W_s compactly supported
inside [N,4N], with |W_s^(j)|<=C_j N^-j. Assume uniformly
sum_n |W_s(n)|>=cN. There are nonnegative coefficients a_s(n),
defined on the support, with a_s(n)=0 whenever n=3 modulo 4, and
a_s(n)<=C_epsilon T^epsilon. Assume the given absolute-mass inequality

    sum_(s in Omega) sum_n a_s(n)|W_s(n)| >= c L K N.

Choose arbitrary nonnegative constants rho_s<=C_epsilon T^epsilon,
independent of the real variable t and radius R. Define

    psi_s(t)=sqrt(t+h+k)-sqrt(t+k)-sqrt(t+h)+sqrt(t),
    f_s(R,t)=W_s(t)e(R psi_s(t)),
    E_s(R)=sum_n a_s(n)f_s(R,n)-rho_s integral f_s(R,t)dt,
    C_s(R)=sum_n (a_s(n)-rho_s) f_s(R,n).

Here R belongs to [T/sqrt(2),sqrt(3)T] and e(x)=exp(2pi i x).
Fix smooth w>=0, supported inside [1/sqrt(2),sqrt(3)], with integral one,
and put hat_w_plus(y)=integral w(t)e(ty)dt. The positive certificate for
C_s is exactly

    B_s(n)=|a_s(n)-rho_s| |W_s(n)|,
    G_s=sum_(n,m) B_s(n)B_s(m)
                   |hat_w_plus(T(psi_s(n)-psi_s(m)))|,
    P=(LK)^(-1)sum_(s in Omega) sqrt(G_s).

Determine rigorously whether subtracting these constants can make this
specific certificate satisfy O(T^(4b+epsilon)) throughout the stated
open band, or derive a sharp enough scoped obstruction. Also determine
the exact sum-integral error E_s-C_s, with uniform radius/support costs,
and the norm which P actually bounds. Do not assume an integer correlation
asymptotic or mistake an upper certificate for the actual signed quantity.
Test the residue-zero and sign-changing-mask seams. If a hypothesis is
insufficient, give its first exact failure or countermodel. No computation
or source search is needed; the given mass inequality is an assumption,
not something this isolated task must prove for an arithmetic sequence.

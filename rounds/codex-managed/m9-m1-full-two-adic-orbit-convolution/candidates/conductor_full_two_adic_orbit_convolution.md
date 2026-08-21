# Conductor candidate: full two-adic actual-row orbit convolution

Campaign: m9-m1-full-two-adic-orbit-convolution.

Starting graph SHA-256:
f4a21236d49d03ff141f637eef932fe95868612e8bb885c97c7f1d042b3c0133.

## Exact local operator

Write

\[
 M=2^\nu N,\qquad N\ \mathrm{odd},\qquad L=2^{\nu-1}.
\]

If the local four-unit mask is nonempty, then \(A=2a\), \(B_2=2c\),
and \(V=2v\) modulo \(2^\nu\), and all odd bases occur exactly once as
\(x=1+2j\), \(j\bmod L\). After the exact CRT rescaling of \(u,K\), put

\[
 w_j=e_{2^\nu}\!\left(u_2(1+2j)+K_2
 \Phi_{2a,2c,2v}(1+2j)\right).
\]

For the literal actual pair rows \(F_j^a\) and \(G_{j-v}^c\), including
entry/exit and zero extension, the local coefficient is

\[
 \mathcal C_{2^\nu}(F,G)
 =\sum_{j\bmod L}w_jF_j^a\overline{G_{j-v}^c}.
\]

With the unnormalised DFT
\(\widehat H_r=\sum_jH_je_L(-rj)\), one has exactly

\[
 \boxed{
 \mathcal C_{2^\nu}(F,G)
 ={1\over L^2}\sum_{k,l\bmod L}
 e_L(lv)\widehat w_{l-k}\widehat F_k^a
 \overline{\widehat G_l^c}.}
 \tag{C101.1}
\]

On unitary Fourier coordinates the kernel is

\[
 \mathsf A_{w,v}(l,k)=L^{-1}\widehat w_{l-k}e_L(lv).
 \tag{C101.2}
\]

It is unitarily equivalent to multiplication by the unimodular sequence
(w_j), followed by a cyclic shift. Therefore

\[
 \mathsf A_{w,v}\mathsf A_{w,v}^*=I_L,\qquad
 \operatorname{rank}\mathsf A_{w,v}=L,\qquad
 \|\mathsf A_{w,v}\|_{2\to2}=1.
 \tag{C101.3}
\]

## Guaranteed twisted period

Let

\[
 P_\nu=
 \begin{cases}
 1,&\nu\le3,\\
 2,&\nu=4,\\
 L/8,&\nu\ge5.
 \end{cases}
 \tag{C101.4}
\]

For the complete reciprocal phase,

\[
 \Phi(1+2(j+P_\nu))\equiv\Phi(1+2j)\pmod{2^\nu}.
 \tag{C101.5}
\]

Consequently

\[
 w_{j+P_\nu}=e_L(u_2P_\nu)w_j,qquad
 \widehat w_r=0\quad\text{unless}\quad
 r\equiv u_2\pmod{L/P_\nu}.
 \tag{C101.6}
\]

This is a guaranteed period, not necessarily the fundamental one.
Nonunit \(K_2\) may shorten it. The affine support in (C101.6) makes
\(\mathsf A_{w,v}\) a permutation of unitary cyclic blocks; it does not
decrease its rank or norm.

To prove (C101.5), use the exact inverse difference

\[
 (z+h)^{-1}-z^{-1}=-h[z(z+h)]^{-1}\pmod{2^\nu}.
\]

For \(\nu\le3\), odd residues are self-inverse modulo \(8\), so the
four-term reciprocal phase is constant. For \(\nu=4\), take \(h=4\);
the inverse difference is \(-4\pmod {16}\), and the four signed copies
cancel. For \(\nu\ge5\), take \(h=2P_\nu=2^{\nu-3}\). Modulo \(8\),
\([z(z+h)]^{-1}\) is constant on odd \(z\): it is \(5\) for \(\nu=5\)
and \(1\) for \(\nu\ge6\). The signed coefficients \(1,-1,-1,1\)
again cancel.

## Normalization and owners

For each of the three accepted class moduli, take its literal
\(\nu=v_2(M)\). The cases \(\nu=0\) and \(\nu=1\) are respectively the
one-point identity and the one-odd-base scalar. CRT gives

\[
 {\mathfrak T_M\over M^2}
 ={\mathfrak T_{2^\nu}\over2^{2\nu}}
 {\mathfrak T_N\over N^2},
 \qquad
 M^{-5}\mathfrak T_M=M^{-4}\sum_x^{\mathrm{mask}}w_x.
 \tag{C101.7}
\]

The four physical rows already supply \(M^{-4}\); (C101.1) contributes
only \(L^{-2}\). The global owner removes the integer \(u=0\) once. A
nonzero \(u\equiv0\pmod{2^\nu}\), a nonzero modulus multiple, a local
zero Fourier index, or a constant local weight is not that owner.

If the full odd labels align and \(a=c\), the aligned return order is

\[
 R_{\rm al}={L\over\gcd(L,v)}.
 \tag{C101.8}
\]

More generally, the full CRT return order is the least common multiple of
the local order and the odd translation order. Only \(R=1\) is
Round-87-owned, and only \(1<R\le\rho_*\) is Round-88-coarse-owned.
Thus the Round-100 deletion of its \(L=4,v=1\) square is correct but does
not extend to every higher two-part aligned term. Exact reversal has its
own return order; on the fully aligned reversal slice it is
\(L/\gcd(L,v-a)\) locally and is not automatically a positive square or
an owner.

## Exact survivor and scope

After the unique global \(u=0\) owner and the successive Round-87,
Round-88 coarse/good-prime, and Round-89 certified-cell owners, the exact
survivor is

\[
 \mathscr S_{2\text{-adic}}(U)
 =\sum_{b\asymp B}\sum_{\lambda\in\mathscr H_{b,U}}
 \mathfrak a_\lambda
 \sum_{y\bmod N_\lambda}^{\mathrm{odd\ mask}}
 w_{N_\lambda,\lambda}(y)
 \mathcal C_{2^{\nu_\lambda},\lambda}(y).
 \tag{C101.9}
\]

Here the conductor sum precedes the absolute value, and
\(\mathfrak a_\lambda\) retains every class, sign, alias, reflection,
Ramanujan term, transition, star, dyadic multiplier, nonunit \(K\),
nonzero modulus multiple, and zero extension. Constant-character,
lower-period, long-return aligned/reversal, and maximal guaranteed-period
terms are subcases of the same scalar, not separately bounded owners.

The exact reduction proves no estimate for (C101.9). In particular it gives
no \(J^{-1/6}\) gain and changes no analytic or exponent status.

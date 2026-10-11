# Round224 actual complete GAR interface

Conductor statement packet. Graph SHA256:
a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.
The complete target and all accepted scopes below are inherited, not
asserted proved here.

For real X>=2, y=floor(sqrt X), D_j=2^(-j)y and
H_j=floor(D_j X^(-1/4)), use the fixed accepted finite denominator
partition and the exact one-sided hard-top and star conventions. Put
\[
A_X(h,q)=\Omega_X^*(hq,h)
 =\sum_j1_{h\le H_j}\Phi(h/(H_j+1))
 [w_j(2\sqrt{Xh/q})]^*,\qquad
C_X^*(n)=\sum_{hq=n}\chi_4(q)A_X(h,q).
\]
This coefficient is real; it is not the unrestricted r2/4. Retain all
active scales, the actual taper and the prime2 through chi4's zero values.
Let F_X(n)=1_{1<=n<=floor(16sqrt X)} n^(-3/4)e(sqrt(Xn)),
with the exact accepted cutoff convention, and
\[
\mathcal L_A(F)=\sum_{n\ge1}c_A(n)F(n),\quad
c_A(n)=\sum_{hq=n}\chi_4(q)A(h,q),\qquad
G_X=\Re\{e(1/8)\mathcal L_{A_X}(F_X)\}.
\]
The objective is |G_X|<<X^epsilon. The accepted reconstruction is
M_(1,active)^stat=-(4/pi)X^(1/4)G_X+O(log^2 X), with inactive bottom
and other owned transform errors already at X^(1/4+epsilon).
The complete original smooth/flat fallback and other routes keep their
own scopes; do not use a blockwise or flat theorem on an unrepresented
companion. GAR implies only total active M1, not blockwise M9-M1.

For a prime p=1 mod4, the finite coefficient algebra gives a candidate
amplification through
c_A(pn)+c_A(n/p)-2c_A(n), with c_A(n/p)=0 if p does not divide n.
For actual A_X this is generally nonzero. Derive it exactly in terms of
A_X(h,pq), A_X(ph,q), A_X(ph,pq), retaining overlap terms for p|n.
The adjoint on a finite radial test is
\[
T_p^*F(m)=1_{p\mid m}F(m/p)+F(pm).
\]
Thus, writing E_(p,A)(n)=c_A(pn)+c_A(n/p)-2c_A(n), the EXACT
joint expression for a finite nonempty split-prime set Pcal is
\[
2|\mathcal P|G_X
 =\Re\left\{e(1/8)\left[
\mathcal L_{A_X}\left(\sum_{p\in\mathcal P}T_p^*F_X\right)
-\sum_{p\in\mathcal P}\sum_n E_{p,A_X}(n)F_X(n)
\right]\right\}.
\]
This identity itself is not a saving. A useful joint bound must be
O(|Pcal| X^epsilon), or improve a stated complete inherited exponent.
Taking main and correction absolute values separately is a stronger
certificate and must be priced as such. Do not delete E, replace A_X
by1, or infer cross-prime orthogonality from the unweighted eigenrelation.

Radial dilations also change amplitude and cutoff. The factors p^(3/4)
and p^(-3/4), phases sqrt((X/p)m) and sqrt((pX)m), divisibility mask and
cutoffs at p*floor(16sqrt X) or floor(16sqrt X)/p must remain exact.
A_X is still the original coefficient at X, not A_(pX) or A_(X/p).
No averaging or high-value membership at the scaled centres is granted.

Accepted120 pays the fixed nonlower radial complement. Accepted121
permits full lower flattening/integerization only with its O(X^(1/4+
epsilon)) physical errors. Accepted122 retains all low-two-adic and
residue branches. Later lower dependencies through159 remain, including
the common-profile self-return and every D>1,L>1,t and cross contribution.
The packet authorizes no deletion or extra state promotion.

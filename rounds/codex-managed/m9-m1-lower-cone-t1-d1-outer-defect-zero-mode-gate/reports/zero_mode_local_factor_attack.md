# Round 156 analytic report: exact local factors and closure of the theta zero row

- Campaign: m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate
- Task: zero_mode_local_factor_attack
- Role: discovery / claimant
- Research round: 156
- Starting graph SHA-256: f9866ea08923ae28f9631e503d2a5eb6be3cd85a09eb05505deec2903d1658b6
- Allocation: 100% analytic and algebraic; 0% numerical
- Status: candidate evidence only
- Terminal label proposed by this report: outer_defect_zero_mode_target

## 1. Result: exact character arithmetic and a target-sized weighted zero row

Put \(q=4N\), and for every odd \(d\mid N\) put \(m=N/d\) and
\(c=4m=q/d\). The two assertions below are proved.

First, if

\[
 r=\prod_{p:\,v_p(m)\ {\rm odd}}p
\tag{156.R1}
\]

is the square-free kernel of \(m\), including \(p=2\), and

\[
 D_\sigma=
 \begin{cases}
  \sigma r,&\sigma r\equiv1\pmod4,\\
  4\sigma r,&\sigma r\not\equiv1\pmod4,
 \end{cases}
 \qquad \sigma\in\{+1,-1\},
\tag{156.R2}
\]

then the two characters in the zero-frequency multiplier are precisely
the primitive quadratic characters
\(\psi_\sigma=\chi_{D_\sigma}\), induced from conductor
\(f_\sigma=|D_\sigma|\) to modulus \(4m\). Thus

\[
 K(0,-j;4m)=\alpha S_+(j;4m)+\beta S_-(j;4m),
 \quad \alpha=\frac{1+i}{2},\quad\beta=\frac{1-i}{2},
\tag{156.R3}
\]

where

\[
 S_\sigma(j;4m)=\sum_{a\bmod4m}^{*}\psi_\sigma(a)e_{4m}(-aj).
\tag{156.R4}
\]

Equations (156.R18)--(156.R31) below give every odd prime-power factor,
the complete two-adic factor, its exact phase and magnitude, the induced
multiplicity, all valuation support, and the principal and repeated-prime
degeneracies. In particular no square-free or odd-\(N\) assumption is
used.

Second, the full normalized \(d\)-sum has a stronger exact recombination.
Define

\[
 \mathscr S_N(j)=\sum_{x\bmod4N}
 {\bf1}_{N\mid x^2-j}\chi_4\!\left(\frac{x^2-j}{N}\right).
\tag{156.R5}
\]

Then

\[
 \boxed{
 \mathscr S_N(j)=
 -\frac{i(1+i)}{2N}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt{4N/d}\,K(0,-j;4N/d).}
\tag{156.R6}
\]

Consequently the literal zero row is exactly

\[
 \boxed{
 \mathcal Z_U(V)=\frac1{4N}
 \sum_{V<|j|\le2V}\widehat B_j(0)\mathscr S_N(j).}
\tag{156.R7}
\]

The arithmetic sequence in (156.R5) has the uniform interval bound

\[
 \sup_{I\subset\mathbb Z,\ |I|\le4N}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 \ll \sqrt N\,\tau(N)\log(2N).
\tag{156.R8}
\]

For each of the two literal signed dyadic intervals, the actual
pre-linearization coefficient satisfies

\[
 \|\widehat B_\bullet(0)\|_{\mathrm{BV}(I)}
 :=\sup_{j\in I}|\widehat B_j(0)|
   +\sum_{j,j+1\in I}|\widehat B_{j+1}(0)-\widehat B_j(0)|
 \ll_\varepsilon K M^{-3/4}X^\varepsilon,
 \qquad K=\sqrt{NM}.
\tag{156.R9}
\]

This is derived with the exact residual phase, zero-extended profile,
asymmetric cell, transitions, strict mask, and hard endpoints; the selected
linearization is not used. Abel summation in (156.R7) now gives

\[
 \boxed{
 |\mathcal Z_U(V)|
 \ll_\varepsilon
 \frac{K M^{-3/4}\sqrt N}{N}X^\varepsilon
 =M^{-1/4}X^\varepsilon
 \ll X^\varepsilon.}
\tag{156.R10}
\]

The bound is uniform for arbitrary \(N\), every
\(M^{3/4}(\log(2X))^A<V\le\sqrt{NM}\), both signs of \(j\), every profile
transition and endpoint, and the external \(B_{1,U}(1)\) seam. It proves
the frozen zero-row target, but nothing about the nonzero theta matrix or
any broader owner.

## 2. Exact statement and hypotheses

Fix \(A>0\), \(N=\lfloor X\rfloor\), \(1\ll M\le X^{1/2}\),

\[
 J_A=M^{3/4}(\log(2X))^A,
 \qquad K=\sqrt{NM},
 \qquad J_A<V\le K,
\tag{156.R11}
\]

and retain the inherited zero-extended profile

\[
 \|w_U\|_\infty+\operatorname {Var}(w_U)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{156.R12}
\]

The ambient \(x\)-support has total length \(O(KX^\varepsilon)\), lies on
\(x\asymp K\), and is shorter than \(N\). The coefficient \(B_j(x)\) is
the literal one from the accepted completion: on its support it contains

\[
 w_U\!\left(\frac{x^2-j}{N}\right)
 e\!\left(\sqrt{x^2-j}-x\right),
 \qquad
 e\!\left(\sqrt{x^2-j}-x\right)
 =e\!\left(-\frac{j}{x+\sqrt{x^2-j}}\right),
\tag{156.R13}
\]

and it retains the literal zero extension, every actual support component
and transition, the asymmetric cell \(-x\le j\le x-1\), the strict mask
\(V<|j|\le2V\), and all hard endpoints. Thus

\[
 \widehat B_j(0)=\sum_{x\bmod q}B_j(x),\qquad q=4N,
\tag{156.R14}
\]

with the unique supported representatives used in the sum. The external
\(B_{1,U}(1)\) is not inserted into \(B_j\) and remains
\(O_\varepsilon(X^\varepsilon)\).

For \(c=4m\), the theta multiplier convention is

\[
 K(0,-j;c)=\sum_{a\bmod c}^{*}
 \epsilon_a\left(\frac ca\right)e_c(-aj),
 \qquad
 \epsilon_a=\begin{cases}1,&a\equiv1\pmod4,\\i,&a\equiv3\pmod4.
 \end{cases}
\tag{156.R15}
\]

All Kronecker symbols are used with their literal composite and two-adic
content. No primitive-character theorem, Pólya--Vinogradov theorem,
Burgess theorem, or numerical experiment is imported: all finite formulas
and the interval estimate used below are derived directly.

## 3. Proof and derivation

### 3.1 The two characters and their primitive conductors

For odd \(a\),

\[
 \epsilon_a=\alpha+\beta\chi_4(a),\qquad
 \left(\frac{4m}{a}\right)=\left(\frac ma\right)
 =\left(\frac ra\right).
\tag{156.R16}
\]

Moreover

\[
 \chi_4(a)\left(\frac ra\right)=\left(\frac{-r}{a}\right).
\tag{156.R17}
\]

The fundamental-discriminant rule (156.R2) therefore gives (156.R3)--
(156.R4). Explicitly, if \(r\) is odd, then

\[
 f_+=\begin{cases}r,&r\equiv1\pmod4,\\4r,&r\equiv3\pmod4,
 \end{cases}
 \qquad
 f_-=\begin{cases}4r,&r\equiv1\pmod4,\\r,&r\equiv3\pmod4;
 \end{cases}
\tag{156.R18}
\]

if \(r\) is even, then \(f_+=f_-=4r\). The only principal case is
\(r=1,\sigma=+\), when \(D_+=1\) and \(f_+=1\). When \(r=1\), the other
piece is exactly the primitive character \(\chi_{-4}=\chi_4\) of conductor
four.

For later local phases, factor a fundamental discriminant into prime
discriminants. At every odd \(p\mid r\), both \(\psi_+\) and \(\psi_-\)
have local component \((\cdot/p)\). Write \(s=v_2(m)\). If \(s\) is even,
then \(r\) is odd and, with \(\eta=\chi_4(r)\), the two-adic component is
principal for \(\sigma=\eta\) and is \(\chi_{-4}=\chi_4\) for
\(\sigma=-\eta\). If \(s\) is odd, write \(r=2r_o\); the two-adic
component of \(\psi_\sigma\) is

\[
 \chi_{8\sigma\chi_4(r_o)}\in\{\chi_8,\chi_{-8}\}.
\tag{156.R19}
\]

This derives, rather than assumes, every primitive conductor and its exact
two-adic exponent \(0,2\), or \(3\).

### 3.2 Exact induced-modulus formula

Let \(\psi\) be any of the primitive characters above, of conductor
\(f\mid Q\), where \(Q=4m\). Put

\[
 L=Q/f,\qquad
 R_f=\prod_{\substack{p\mid Q\\p\nmid f}}p,\qquad
 \tau(\psi)=\sum_{b\bmod f}\psi(b)e_f(b).
\tag{156.R20}
\]

Möbius inversion of the extra unit conditions gives the exact formula

\[
 \boxed{
 \sum_{a\bmod Q}^{*}\psi(a)e_Q(-ja)
 =\tau(\psi)
 \sum_{\substack{e\mid R_f\\L/e\mid j}}
 \mu(e)\psi(e)\frac Le\,
 \overline\psi\!\left(-\frac{je}{L}\right).}
\tag{156.R21}
\]

Indeed, after writing \(a=eb\), the inner modulus is
\(Q/e=f(L/e)\). Summation over its \(L/e\) lifts vanishes unless
\(L/e\mid j\); on that support it is

\[
 \frac Le\,\overline\psi\!\left(-\frac{je}{L}\right)\tau(\psi).
\tag{156.R22}
\]

Thus a prime already in the conductor supplies the exact induced
multiplicity \(p^{\nu-\kappa}\) and forces
\(v_p(j)=\nu-\kappa\), whereas a prime absent from the conductor supplies
a Ramanujan factor and permits only \(v_p(j)=\nu-1\) or
\(v_p(j)\ge\nu\). For these real quadratic characters
\(\tau(\chi_D)=\sqrt D\), with the branch
\(\sqrt D=\sqrt D\) for \(D>0\) and \(i\sqrt{|D|}\) for \(D<0\); the local
tables below also prove this phase convention.

### 3.3 Every prime-power Fourier factor

For a completely phase-exact CRT statement, if \(p^\nu\Vert Q\), put
\(Q_p=Q/p^\nu\) and choose \(u_pQ_p\equiv1\pmod{p^\nu}\). Set
\(n_p=ju_p\). Then

\[
 S_\sigma(j;Q)=\prod_{p^\nu\Vert Q}F_{p,\sigma}(n_p),
 \quad
 F_{p,\sigma}(n)=
 \sum_{a\bmod p^\nu}^{*}\psi_{\sigma,p}(a)e_{p^\nu}(-na).
\tag{156.R23}
\]

The CRT units \(u_p\) in (156.R23) retain every exact phase; they do not
change valuations.

The local induction used in every line below is elementary. If
\(\psi_p\) is primitive modulo \(p^\kappa\), \(1\le\kappa\le\nu\), split
\(a=a_0+p^\kappa t\). Then

\[
 \sum_{a\bmod p^\nu}\psi_p(a)e_{p^\nu}(-na)
 =
 \begin{cases}
  p^{\nu-\kappa}\overline{\psi_p}(-u)\tau(\psi_p),
    &n=p^{\nu-\kappa}u,\quad p\nmid u,\\
  0,&v_p(n)\ne\nu-\kappa.
 \end{cases}
\tag{156.R23a}
\]

If the local character is principal, unit inclusion-exclusion gives
instead the Ramanujan sum \(c_{p^\nu}(n)\). Substituting
\(\tau((\cdot/p))=\epsilon_p\sqrt p\),
\(\tau(\chi_{-4})=2i\), \(\tau(\chi_8)=\sqrt8\), and
\(\tau(\chi_{-8})=i\sqrt8\) into (156.R23a) proves, with the negative
additive phase retained, all of the following values.

For an odd prime \(p^e\Vert m\), the complete table is

\[
 F_{p,\sigma}(n)=
 \begin{cases}
  p^{e-1}\left(\dfrac{-u}{p}\right)\epsilon_p\sqrt p,
    &e\ {\rm odd},\ n=p^{e-1}u,\ p\nmid u,\\[3pt]
  0,&e\ {\rm odd},\ v_p(n)\ne e-1,\\[3pt]
  \varphi(p^e),&e\ {\rm even},\ v_p(n)\ge e,\\
  -p^{e-1},&e\ {\rm even},\ v_p(n)=e-1,\\
  0,&e\ {\rm even},\ v_p(n)\le e-2,
 \end{cases}
\tag{156.R24}
\]

where

\[
 \epsilon_p=\begin{cases}1,&p\equiv1\pmod4,\\i,&p\equiv3\pmod4.
 \end{cases}
\tag{156.R25}
\]

Thus an odd repeated prime with odd exponent has exact support
\(v_p(j)=e-1\) and magnitude \(p^{e-1/2}\). An even exponent is a
principal local degeneration: its two nonzero strata have exact values
\(-p^{e-1}\) and \(\varphi(p^e)\).

At two, put \(\nu=s+2\). If \(s\) is even and
\(\eta=\chi_4(r)\), then for \(\sigma=\eta\)

\[
 F_{2,\eta}(n)=c_{2^\nu}(n)=
 \begin{cases}
  2^{\nu-1},&v_2(n)\ge\nu,\\
  -2^{\nu-1},&v_2(n)=\nu-1,\\
  0,&v_2(n)\le\nu-2,
 \end{cases}
\tag{156.R26}
\]

whereas for \(\sigma=-\eta\)

\[
 F_{2,-\eta}(n)=
 \begin{cases}
  -i\,2^{\nu-1}\chi_4(u),&n=2^{\nu-2}u,\quad u\ {\rm odd},\\
  0,&v_2(n)\ne\nu-2.
 \end{cases}
\tag{156.R27}
\]

Here \(\tau(\chi_{-4})=2i\), and the minus sign in the additive phase is
included in (156.R27).

If \(s\) is odd, write \(r=2r_o\) and
\(\eta_\sigma=\sigma\chi_4(r_o)\). Then

\[
 F_{2,\sigma}(n)=
 \begin{cases}
  2^{\nu-3}\chi_{8\eta_\sigma}(-u)
      \tau(\chi_{8\eta_\sigma}),
      &n=2^{\nu-3}u,\quad u\ {\rm odd},\\
  0,&v_2(n)\ne\nu-3,
 \end{cases}
\tag{156.R28}
\]

with

\[
 \tau(\chi_8)=\sqrt8,\qquad
 \tau(\chi_{-8})=i\sqrt8.
\tag{156.R29}
\]

Thus each individual piece has two-adic magnitude
\(2^{\nu-3/2}\) and exact valuation \(v_2(j)=s-1\).

### 3.4 Combination of the two pieces, support, magnitude, and degeneracy

All odd local factors in \(S_+\) and \(S_-\) are identical, so only the
two-adic factors need be combined with \(\alpha,\beta\). Let
\(n_2=ju_2\), with \(u_2(Q/2^\nu)\equiv1\pmod{2^\nu}\), and let
\(C_+=\alpha,C_-=\beta\).

If \(s\) is even, the two supports are disjoint and the exact combined
two-factor of \(K\) is

\[
 \Omega_2(j)=
 \begin{cases}
  C_{-\eta}\bigl(-i2^{s+1}\chi_4(u)\bigr),
     &n_2=2^su,\ u\ {\rm odd},\\
  C_\eta(-2^{s+1}),&v_2(j)=s+1,\\
  C_\eta(2^{s+1}),&v_2(j)\ge s+2,\\
  0,&v_2(j)<s.
 \end{cases}
\tag{156.R30}
\]

On every surviving stratum, \(|\Omega_2(j)|=2^{s+1/2}\). There is no
cross-character cancellation: the \(\chi_4\)-local piece occupies
\(v_2(j)=s\), and the principal-local piece occupies
\(v_2(j)\ge s+1\).

If \(s\) is odd, put \(\eta=\chi_4(r_o)\) and
\(u=n_2/2^{s-1}\). Direct substitution of (156.R28)--(156.R29) into
\(\alpha F_{2,+}+\beta F_{2,-}\) gives

\[
 \boxed{
 \Omega_2(j)=2^{s-1}\sqrt8\,\chi_8(u)(1+i\eta)
 {\bf1}_{\chi_4(u)=-\eta},
 \qquad v_2(j)=s-1.}
\tag{156.R31}
\]

Since \(Q/2^\nu\) has the same mod-four character as \(r_o\), the last
condition is equivalently

\[
 v_2(j)=s-1,\qquad
 \chi_4\!\left(j/2^{s-1}\right)=-1.
\tag{156.R32}
\]

The exact magnitude on this support is \(2^{s+1}\). Hence the two
character pieces cancel on exactly half of the odd units in the odd-\(s\)
case.

For the odd part set

\[
 A_o(m)=\prod_{\substack{p^e\Vert m\\p\ {\rm odd}}}p^{e-1}.
\tag{156.R33}
\]

Equations (156.R24), (156.R30), and (156.R32) locate every surviving
\(j\). At an odd \(p^e\Vert m\), \(p^{e-1}\mid j\); if \(e\) is odd the
valuation is exactly \(e-1\), while if \(e\) is even both
\(v_p(j)=e-1\) and \(v_p(j)\ge e\) survive. If \(s\) is even, the total
support lies in \(2^sA_o(m)\mid j\), so its dyadic capacity is

\[
 O\!\left(\frac{V}{2^sA_o(m)}+1\right).
\tag{156.R34}
\]

If \(s\) is odd, the two-adic residue (156.R32) and the odd divisibility
give capacity

\[
 O\!\left(\frac{V}{2^{s+1}A_o(m)}+1\right).
\tag{156.R35}
\]

These are support counts only. For odd square-free \(m\), all odd primes
merely require \((j,m)=1\), and the two pieces partition odd and even
\(j\); there is no positive-power sparsity. For even square-free \(m\),
\(j\) is odd and (156.R32) selects one class modulo four. If \(m\) is a
perfect square, \(S_+=c_{4m}(j)\) is the principal Ramanujan sum and
\(S_-\) is the character \(\chi_4\) induced to \(4m\), with exactly the
local strata (156.R24), (156.R26), and (156.R27). Thus every squareful
and principal degeneration has been retained; none of (156.R34)--
(156.R35) is used as signed lower information.

### 3.5 The full \(d\)-sum and its exact local root form

Let

\[
 G_N(t)={\bf1}_{N\mid t}\chi_4(t/N)
 =-\frac{i}{2N}\sum_{\substack{h\bmod4N\\h\ {\rm odd}}}
 \chi_4(h)e_{4N}(ht).
\tag{156.R36}
\]

Summing \(G_N(x^2-j)\) over \(x\bmod q\), partition the odd \(h\)'s
uniquely as

\[
 d=(h,N),\qquad h=da,\qquad
 d\mid N\ {\rm odd},\qquad a\in(\mathbb Z/(4N/d)\mathbb Z)^*.
\tag{156.R37}
\]

There are \(d\) copies of \(x\bmod c\) in \(x\bmod q\), and the exact even
quadratic Gauss sum is

\[
 \sum_{x\bmod c}e_c(ax^2)
 =(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c.
\tag{156.R38}
\]

Because \(\chi_4(a)\epsilon_a^{-1}=\epsilon_a\), equations
(156.R36)--(156.R38) prove (156.R6), including its phase and every factor
\(d,\sqrt c,2N\). Multiplication by the remaining \(1/q\) Fourier factor
proves (156.R7). In particular the entire nested \(d\)-sum is restored
before any estimate; it is not replaced by an absolute divisor sum.

There is also a completely local physical formula:

\[
 \boxed{
 \mathscr S_N(j)=\rho_{4N}(j+N)-\rho_{4N}(j+3N),
 \qquad
 \rho_Q(t)=\#\{x\bmod Q:x^2\equiv t\pmod Q\}.}
\tag{156.R39}
\]

If \(N=2^sn\) with \(n\) odd, CRT gives the full two-adic decomposition

\[
 \mathscr S_N(j)=\rho_n(j)
 \left\{
 \rho_{2^{s+2}}(j+2^sn)
 -\rho_{2^{s+2}}(j+3\cdot2^sn)
 \right\}.
\tag{156.R40}
\]

For completeness, every local root factor in (156.R40) is as follows. If
\(p\) is odd, \(p^e\Vert Q\), and \(v=v_p(t)\), then

\[
 \rho_{p^e}(t)=
 \begin{cases}
  p^{\lfloor e/2\rfloor},&v\ge e,\\
  p^a\bigl(1+(u/p)\bigr),&v=2a<e,\ t=p^{2a}u,\ p\nmid u,\\
  0,&v<e\text{ is odd}.
 \end{cases}
\tag{156.R41}
\]

For \(2^e\), the first and third lines remain
\(2^{\lfloor e/2\rfloor}\) and zero. When \(v=2a<e\), put
\(k=e-2a\); the value is \(2^ag_k(u)\), where

\[
 g_1(u)=1,\qquad
 g_2(u)=2{\bf1}_{u\equiv1\ (4)},\qquad
 g_k(u)=4{\bf1}_{u\equiv1\ (8)}\quad(k\ge3).
\tag{156.R42}
\]

Thus (156.R39)--(156.R42) also retain every squareful and two-adic stratum
of the normalized \(d\)-sum. For odd \(N\), they simplify to

\[
 \mathscr S_N(j)=2\chi_4(N)\eta_4(j)\rho_N(j),
 \qquad
 \eta_4(j)=
 \begin{cases}1,&j\equiv0,3\pmod4,\\-1,&j\equiv1,2\pmod4.
 \end{cases}
\tag{156.R43}
\]

This last display is illustrative only; the proof of the uniform bound
does not assume \(N\) odd.

### 3.6 A direct Pólya-type bound for the recombined arithmetic sequence

Use the Fourier convention

\[
 \widetilde{\mathscr S}_N(h)
 =\sum_{j\bmod q}\mathscr S_N(j)e_q(hj).
\tag{156.R44}
\]

Changing variables \(t=x^2-j\) in (156.R5) gives

\[
 \widetilde{\mathscr S}_N(h)=
 \left(\sum_{r\bmod4}\chi_4(r)e_4(-hr)\right)
 \left(\sum_{x\bmod q}e_q(hx^2)\right).
\tag{156.R45}
\]

The first factor is zero for even \(h\), and is
\(-2i\chi_4(h)\) for odd \(h\). For odd \(h\), put
\(d=(h,N)\), \(c=q/d\), and \(a=h/d\). The second factor is exactly

\[
 d(1+i)\epsilon_a^{-1}\left(\frac ca\right)\sqrt c,
\tag{156.R46}
\]

so

\[
 |\widetilde{\mathscr S}_N(h)|
 =2\sqrt{2qd},\qquad d=(h,N),
\tag{156.R47}
\]

and the zero Fourier coefficient vanishes. Fourier inversion over any
integer interval \(I\) of length at most \(q\), followed by the exact
geometric-progression bound, yields

\[
 \begin{aligned}
 \left|\sum_{j\in I}\mathscr S_N(j)\right|
 &\ll \sqrt q
 \sum_{1\le h\le q/2}\frac{(h,N)^{1/2}}h\\
 &\le \sqrt q\sum_{g\mid N}g^{1/2}
       \sum_{k\le q/(2g)}\frac1{gk}\\
 &\ll \sqrt N\,\tau(N)\log(2N).
 \end{aligned}
\tag{156.R48}
\]

This proves (156.R8). It is a signed finite Fourier estimate for the
fully recombined arithmetic sequence. It is not a termwise DFI bound and
does not call a support count or a theorem right side a lower bound.

### 3.7 Literal \(\widehat B_j(0)\) variation and the restored power ledger

Let \(I_+=\{j:V<j\le2V\}\) and
\(I_-=\{j:-2V\le j<-V\}\), with the literal integer endpoints. For a
fixed supported \(x\), the map

\[
 j\longmapsto (x^2-j)/N
\tag{156.R49}
\]

is monotone. Hence composition with the actual zero-extended profile
costs at most \(\operatorname {Var}(w_U)\), including all profile support
components and transitions. On the same support
\(\sqrt{x^2-j}\asymp K\), and therefore the exact, unlinearized phase has

\[
 \sum_{\substack{j,j+1\in I_\pm\\B_j(x)B_{j+1}(x)\ne0}}
 \left|
 e(\sqrt{x^2-j-1}-x)-e(\sqrt{x^2-j}-x)
 \right|
 \ll \frac{|I_\pm|}{K}\ll1.
\tag{156.R50}
\]

The cell \(-x\le j\le x-1\) contributes at most two jumps for this fixed
\(x\). Zero extension prices the profile endpoints, and extending by zero
across the strict dyadic mask prices at most two further jumps. Thus the
product-variation inequality and (156.R12) give, for every fixed \(x\),

\[
 \sup_{j\in I_\pm}|B_j(x)|
 +\operatorname {Var}_{j\in I_\pm}B_j(x)
 \ll_\varepsilon M^{-3/4}X^\varepsilon.
\tag{156.R51}
\]

The union of actual \(x\)-supports has \(O(KX^\varepsilon)\) integer
points. Summing (156.R51) over those literal representatives proves
(156.R9). This is the required weighted seam; \(\widehat B_j(0)\) has not
been replaced by a constant or by its supremum alone.

Apply discrete Abel summation separately on \(I_+\) and \(I_-\), using
(156.R8)--(156.R9), and then use (156.R7). The complete ledger is

| Stage | Exact or bounded factor |
|---|---:|
| fixed \(d\), local arithmetic | (156.R18)--(156.R35), with every conductor and valuation |
| all odd \(d\mid N\), exterior normalization | exact identity (156.R6) |
| remaining finite-Fourier normalization | \(q^{-1}=(4N)^{-1}\) |
| signed arithmetic partial sum | \(N^{1/2}X^\varepsilon\) |
| literal weighted \(j\)-BV norm | \(K M^{-3/4}X^\varepsilon\) |
| both signs and exact endpoints | constant factor only |
| external \(B_{1,U}(1)\) | \(X^\varepsilon\) |
| final zero row | \(N^{-1}N^{1/2}K M^{-3/4}X^\varepsilon=M^{-1/4}X^\varepsilon\) |

There is no residual \(V\), \(d\), conductor, squareful, or endpoint power.
The older absolute capacity
\(N^{-1/2}M^{-1/4}V+M^{-1/4}\) is therefore improved by a genuine signed
outer-\(j\) estimate after, and only after, the exact \(d\)-recombination.

## 4. First doubtful or unproved step

There is no unproved step inside the zero-row theorem beyond the accepted
literal-profile hypotheses (156.R12)--(156.R14). The first unproved term
after this result is the nonzero matrix

\[
 -\frac{i(1+i)}{2Nq}
 \sum_{V<|j|\le2V}
 \sum_{\substack{d\mid N\\d\ {\rm odd}}}
 \chi_4(d)d\sqrt c
 \sum_{\substack{v\bmod(c/2)\\v\ne0}}
 \widehat B_j(2dv)K(-v^2,-j;c),
 \qquad c=4N/d,
\tag{156.R52}
\]

with the actual nonseparable coefficient, all folds, both signs, and every
endpoint. Equivalently, the selected signed cross-fibre seam recorded in
Round 155 remains unproved. Formula (156.R8) is special to the zero row:
it comes from the exact full \(d\)-recombination (156.R6), and it does not
extend to (156.R52), where the translated chirp depends jointly on
\(a,x,v\). This report supplies no second top-scale gain for that matrix.

## 5. Required control tests and outcomes

| Required control | Outcome |
|---|---|
| literal_zero_mode_row | GREEN. Equations (156.R6)--(156.R7) reproduce the frozen row with the exact \(1/(2Nq)\), \(d\sqrt c\), multiplier, and Fourier-zero normalization. |
| exact_epsilon_two_character_decomposition | GREEN. Equations (156.R16)--(156.R17) prove the identity and (156.R3) retains both complex coefficients. |
| primitive_conductor_and_induced_modulus | GREEN. Equations (156.R18)--(156.R22) give both fundamental discriminants, conductor \(1,r,4r\), the induced lift multiplicity, and the extra-prime Möbius/Ramanujan factor. |
| all_prime_power_two_adic_local_factors | GREEN. Equations (156.R23)--(156.R31) give exact CRT phases, every odd prime power, and two-adic conductor exponents \(0,2,3\). |
| valuation_support_and_squareful_strata | GREEN. Equations (156.R24), (156.R26)--(156.R35), and (156.R41)--(156.R42) give all exact valuations, magnitudes, principal shells, repeated-prime cases, and the cancellation of half the odd units when \(v_2(m)\) is odd. |
| d_sum_and_full_normalization | GREEN. Every odd \(d\mid N\) is recombined exactly in (156.R6); the remaining \(1/q\) is retained in (156.R7). |
| actual_Bhat0_j_variation | GREEN. Equations (156.R49)--(156.R51) derive the literal \(j\)-BV norm from the zero-extended profile, exact residual phase, actual cell, transitions, and endpoints. |
| positive_negative_defect_and_endpoints | GREEN. Abel summation is applied separately to the two literal half-open integer intervals; mask and cell boundary jumps are included in (156.R51). |
| N_M_V_d_conductor_power_ledger | GREEN. The table after (156.R51) restores all variables before obtaining \(M^{-1/4}X^\varepsilon\); no \(V,d,f_\sigma\), or endpoint power is hidden. |
| upper_capacity_vs_signed_sum | GREEN. Local magnitudes and (156.R34)--(156.R35) are labelled capacities only. The asserted gain is the proved signed interval estimate (156.R48), not a lower bound. |
| nonzero_and_downstream_scope | GREEN. Equation (156.R52) and all \(D>1,L>1\), generic \(t=1\), \(t\ge2\), cross, other M1, M2, endpoint, M9, bridge, target, and exponent owners remain open. |

No numerical experiment was performed.

## 6. Dependencies and exact artifacts used

This report used exactly the permitted context:

1. protocol.md;
2. state/proof_obligations.yml, in particular the five Round-156 target
   nodes and the Round-154/155 rejected-inference ledger;
3. state/active_campaign.yml;
4. strategy/round156_d1_outer_defect_zero_mode_strategy.md;
5. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/barrier_packet.md;
6. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-zero-mode-gate/candidates/conductor_round156_zero_mode_seed.md;
7. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reviews/conductor_round155_adjudication.md;
8. rounds/codex-managed/m9-m1-lower-cone-t1-d1-outer-defect-theta-dispersion-gate/reports/outer_defect_spectral_dispersion_attack.md; and
9. rounds/codex-managed/m9-m1-lower-cone-t1-d1-large-defect-root-dispersion-gate/candidates/conductor_round154_root_dispersion_adjudication.md.

The finite quadratic and character Gauss evaluations are derived in the
report's normalization. No web source, sibling Round-156 report,
computation, or nonpermitted artifact was used. No shared proof-state,
strategy, candidate, review, synthesis, validation, control, or sibling
file was edited.

## 7. Recommended state effect

**Promote after independent seam review under
outer_defect_zero_mode_target.** Add a route-scoped proved-internal
zero-mode lemma consisting of (156.R3)--(156.R10), with the local tables
(156.R18)--(156.R35), the exact normalized \(d\)-sum (156.R6), the signed
interval theorem (156.R8), and the literal weighted seam (156.R9).

Update the D=1 outer-defect frontier only by deleting the zero row from its
list of missing inputs. The first missing input should become the
incomplete nonzero matrix (156.R52), or the equivalent selected signed
cross-fibre theorem. Retain the logarithmic collar as the last proved
range for the complete D=1 wave, and make no change to any \(D>1\),
\(L>1\), generic, \(t\ge2\), cross, other M1, M2, endpoint-uniformity,
M9, bridge, Gauss-circle target, or exponent obligation.

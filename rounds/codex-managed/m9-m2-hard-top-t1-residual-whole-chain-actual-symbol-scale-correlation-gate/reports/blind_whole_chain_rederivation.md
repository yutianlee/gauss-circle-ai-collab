# Round 175 blind whole-chain rederivation

- Round: 175
- Campaign: `m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate`
- Role: statement-only blind rederiver
- Evidence status: candidate only
- Supplied graph-hash provenance: `e40c214351d06bf05212e25fffbec0f1a4808be21cb9098ba25823f0d9bbf211`

## 1. Result

### Exact no-go result

The scale variable is **not** an additional cancellation variable in the
quantity stated in (175.B10).  Put, without changing either frequency
restriction,

\[
 V_\epsilon(\theta):=
 \sum_{\substack{k\in\mathbb Z\\k\ {\mathrm{odd}}}}
 \sum_{\substack{\ell\in\mathbb Z\\\ell\ne0}}
 \chi_4(k)U_{k,\ell}^{(\epsilon)}(\theta),
 \qquad
 T_\epsilon(\theta):={i\over2}V_\epsilon(\theta).
\tag{175.R1}
\]

Then the full stopped chain, including its terminal link (strict only when
\(R_{K-1}<M<2R_{K-1}\)), has the exact identity

\[
 \boxed{
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 ={1\over8}\sum_{\epsilon=0}^1\int_0^1
 (F_M-F_{R_0})(\theta)|V_\epsilon(\theta)|^2\,d\theta
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1
 (F_M-F_{R_0})(\theta)|T_\epsilon(\theta)|^2\,d\theta .}
\tag{175.R2}
\]

This is valid before inspecting \(\omega_L\rho_NA_N\), and indeed for any
integrable scalar array in place of \(V_\epsilon\).  In ordinary Fejer
frequency \(r\), the endpoint multiplier is

\[
 \beta_{M,R_0}(r)=
 \begin{cases}
 |r|(R_0^{-1}-M^{-1}),&0<|r|<R_0,\\
 1-|r|/M,&R_0\le |r|<M,\\
 0,&r=0\ \hbox{or}\ |r|\ge M.
 \end{cases}
\tag{175.R3}
\]

Every individual link has nonnegative coefficients in this same Fejer
Fourier mode.  Thus an isolated integer mode has link weights which simply
add to (175.R3).  After complete physical Poisson recombination, these
integer modes are physical gaps, and gaps with
\(R_0\le |r|\le M/2\) retain weight at least \(1/2\).  This is distinct
from a fixed transformed tuple \((k,k',\ell,\ell')\): for such a tuple the
only exact scale statement is telescoping of its link integrals to its
endpoint integral, with no inferred sign or \(1/2\) lower weight.  Any
saving must therefore be proved inside the exact endpoint correlation in
(175.R2), before a modulus over frequency, cell, opening, endpoint, or
scale.  It cannot be credited to cross-link scale cancellation.

The literal coefficient can also be recovered with the exact \(i/2\)
normalization if and only if the omitted \(\ell=0\) frequency is restored
collectively.  Namely, define

\[
 P_\epsilon(\theta):=\sum_N(-1)^{\epsilon N}z_Ne(\theta N),
 \qquad
 C_\epsilon(\theta):={i\over2}
 \sum_{\substack{k\in\mathbb Z\\k\ {\mathrm{odd}}}}
 \chi_4(k)U_{k,0}^{(\epsilon)}(\theta).
\tag{175.R4}
\]

Then, exactly,

\[
 T_\epsilon=P_\epsilon-C_\epsilon.
\tag{175.R5}
\]

Consequently no \(\ell=0\) term has been discarded in (175.R2): the target
contains the complete signed combination
\(|P_\epsilon-C_\epsilon|^2\), summed over all odd character frequencies
and both absolute-parity branches.  The full-frequency comparison has the
sliding-window endpoint identity recorded below, but replacing
\(|P_\epsilon-C_\epsilon|^2\) by \(|P_\epsilon|^2\) without the complete
correction would not be valid.

This report does **not** prove the \(L^3X^\varepsilon\) estimate.  It proves
the narrow no-go that the stopped Fejer chain supplies only the endpoint
difference (175.R2), not a new factor-\(L\) degree of freedom.

## 2. Exact statement and hypotheses

All literal data in the packet are retained.  In particular,

\[
 J=\sqrt X,\quad y=\lfloor J\rfloor,\quad q_X=X/y^2,\quad
 H=\lfloor yX^{-1/4}\rfloor,\quad
 1\ll L\ll H\le J^{1/2}.
\tag{175.R6}
\]

The squarefree half-open shell \(\mathcal I_L^{\rm lit}\) has
\(N\asymp L^2\) and all of its endpoints, floors, stars, and point-value
conventions are literal.  Write \(N=2^{\nu_N}M_N\),
\(\nu_N\in\{0,1\}\), with \(M_N\) odd.  The deterministic rule either
chooses no pair, in which case \(\rho_N(d)=1\), or chooses distinct odd
primes \(p_N,q_N\mid M_N\) satisfying

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\le\kappa L^{-1/2},
\tag{175.R7}
\]

and then

\[
 \rho_N(d)=1-\mathbf1_{p_N\mid d}-\mathbf1_{q_N\mid d}
 +2\mathbf1_{p_N\mid d}\mathbf1_{q_N\mid d}.
\tag{175.R8}
\]

For odd \(d\mid M_N\), with all three functions zero outside their literal
domains,

\[
\begin{aligned}
 A_N(d)&=\mathbf1_{\{\sqrt N\le d\le2\sqrt N\}}^{\rm lit}
 \eta_L(d)\Phi\!\left({d\over H+1}\right)
 W\!\left({\sqrt{q_X}\,d\over2\sqrt N}\right),\\
 \omega_L(N)&=\mathbf1_{\mathcal I_L^{\rm lit}}(N)\mu^2(N)
 \left({L^2\over N}\right)^{3/4},\\
 \lambda_N(d)&=\omega_L(N)\rho_N(d)A_N(d).
\end{aligned}
\tag{175.R9}
\]

The smooth pieces have bounded fixed-rescaling \(C^1\) norms,
\(\eta_L'(d)\ll L^{-1}\), and no hard face is smoothed.  The coefficient,
chirp, and supplied energy are exactly

\[
 c_N^{\rm rem}=\sum_{\substack{d\mid N\\d\ {\mathrm{odd}}}}
 \chi_4(d)\lambda_N(d),
 \qquad z_N=c_N^{\rm rem}e(J\sqrt N),
 \qquad D_L=\sum_N|z_N|^2\ll_\varepsilon L^2X^\varepsilon.
\tag{175.R10}
\]

The literal shell lies in a consecutive integer interval of exact
cardinality \(M\asymp L^2\), and \(z_N\) is zero-extended on the whole
integer line.  With \(R_0=\lceil L\rceil\),

\[
 R_{j+1}=\min(2R_j,M),\qquad R_K=M,
\tag{175.R11}
\]

where \(K\) is minimal, so the possible strict link
\(R_{K-1}<M<2R_{K-1}\) is included.  For integer \(R\),

\[
 F_R(\theta)=\sum_{|r|<R}\left(1-{|r|\over R}\right)e(r\theta),
 \qquad B_{R,S}=F_S-F_R.
\tag{175.R12}
\]

For the specified real
\(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), the packet's
literal interpolation and transforms are

\[
\begin{aligned}
 \mathcal W_\epsilon(x,y)
 &=\sum_{\substack{d,m\ge1\\d\ {\mathrm{odd}}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)\varphi(x-d)\varphi(y-m),\\
 \mathcal B_{\epsilon,\theta}(x,y)
 &=\mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy),\\
 \widetilde{\mathcal B}_{\epsilon,\theta}(\xi,\nu)
 &=\iint_{\mathbb R^2}\mathcal B_{\epsilon,\theta}(x,y)
 e(-\xi x-\nu y)\,dx\,dy,\\
 U_{k,\ell}^{(\epsilon)}(\theta)
 &=\widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\end{aligned}
\tag{175.R13}
\]

For every integer \(R<S\le2R\), including the terminal link and its
possible strict case,

\[
\begin{aligned}
 \mathcal N_{R,S}={1\over8}\Re\sum_{\epsilon=0}^1
 &\sum_{\substack{k,k'\in\mathbb Z\\k,k'\ {\mathrm{odd}}}}
 \sum_{\substack{\ell,\ell'\in\mathbb Z\\\ell,\ell'\ne0}}
 \chi_4(k)\chi_4(k')\\
 &\quad\times\int_0^1B_{R,S}(\theta)
 U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
\end{aligned}
\tag{175.R14}
\]

Thus the \(i/2\) before squaring, the \(1/8\) after parity averaging, both
absolute-parity branches, the one outer real part, all ordinary
frequencies, and the exclusions \(\ell,\ell'\ne0\) are preserved exactly.
The frozen target is the one-sided estimate

\[
 \sum_{j=0}^{K-1}\mathcal N_{R_j,R_{j+1}}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{175.R15}
\]

## 3. Proof and derivation

### 3.1 Factorization before any modulus

The literal support in \((d,m)\) is finite.  Since the bumps are smooth and
compactly supported away from \(xy=0\), each
\(\mathcal B_{\epsilon,\theta}\) is smooth and compactly supported, and its
sampled Fourier series is absolutely convergent for fixed data.  Therefore
the four frequency sums in (175.R14) may be grouped, without taking any
intermediate absolute value, as

\[
 \sum_{k,k'\ {\mathrm{odd}}}\sum_{\ell,\ell'\ne0}
 \chi_4(k)\chi_4(k')U_{k,\ell}^{(\epsilon)}
 \overline{U_{k',\ell'}^{(\epsilon)}}
 =|V_\epsilon(\theta)|^2.
\tag{175.R16}
\]

Both Fejer kernels are real, so \(B_{R,S}\) is real.  The integrand in
(175.R16) is real as well, and the single outer real part in (175.R14)
therefore makes no change.  Since
\(|V_\epsilon|^2=4|T_\epsilon|^2\), the exact link identity is

\[
 \mathcal N_{R,S}
 ={1\over8}\sum_{\epsilon=0}^1\int_0^1B_{R,S}|V_\epsilon|^2
 ={1\over2}\sum_{\epsilon=0}^1\int_0^1B_{R,S}|T_\epsilon|^2.
\tag{175.R17}
\]

No scale-dependent object remains except \(B_{R,S}\).

### 3.2 General scalar scale-Abel identity

For any \(h\in L^1([0,1])\) independent of \(j\), finite telescoping gives

\[
 \sum_{j=0}^{K-1}\int_0^1(F_{R_{j+1}}-F_{R_j})h
 =\int_0^1(F_M-F_{R_0})h.
\tag{175.R18}
\]

This includes the terminal link, whether it is dyadic or strict, because
its upper endpoint is exactly \(R_K=M\); no assumption
\(M=2R_{K-1}\) is used.  Applying (175.R18) to

\[
 h(\theta)={1\over8}\sum_{\epsilon=0}^1|V_\epsilon(\theta)|^2
 ={1\over2}\sum_{\epsilon=0}^1|T_\epsilon(\theta)|^2
\tag{175.R19}
\]

proves (175.R2).

The same fact can be seen diagonal by diagonal.  If
\(f_R(r)=(1-|r|/R)\mathbf1_{|r|<R}\), then for \(R<S\)

\[
 b_{R,S}(r):=f_S(r)-f_R(r)=
 \begin{cases}
 |r|(R^{-1}-S^{-1}),&0<|r|<R,\\
 1-|r|/S,&R\le |r|<S,\\
 0,&r=0\ \hbox{or}\ |r|\ge S.
 \end{cases}
\tag{175.R20}
\]

In particular \(b_{R,S}(r)\ge0\), and

\[
 \sum_{j=0}^{K-1}b_{R_j,R_{j+1}}(r)
 =f_M(r)-f_{R_0}(r)=\beta_{M,R_0}(r).
\tag{175.R21}
\]

If \(a_r:=\int_0^1h(\theta)e(r\theta)\,d\theta\), then, because \(h\) is
real,

\[
 \sum_j\mathcal N_{R_j,R_{j+1}}
 =\sum_{0<|r|<M}\beta_{M,R_0}(r)a_r
 =2\sum_{r=1}^{M-1}\beta_{M,R_0}(r)\Re a_r.
\tag{175.R22}
\]

Thus there is no cancellation between the scale weights of an isolated
Fejer Fourier mode; after complete physical recombination this is an
integer physical gap.  Cancellation in (175.R22), if any, is already
cancellation among the endpoint correlations \(a_r\).  This does not
identify \(r\) with a fixed transformed tuple
\((k,k',\ell,\ell')\).  For a fixed
\(\alpha=(\epsilon,k,k',\ell,\ell')\), define

\[
 \mathcal I_{R,S}(\alpha):={1\over8}\Re\int_0^1B_{R,S}(\theta)
 \chi_4(k)\chi_4(k')U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
\tag{175.R22a}
\]

The only exact fixed-transformed-diagonal identity is

\[
 \sum_{j=0}^{K-1}\mathcal I_{R_j,R_{j+1}}(\alpha)
 ={1\over8}\Re\int_0^1(F_M-F_{R_0})(\theta)
 \chi_4(k)\chi_4(k')U_{k,\ell}^{(\epsilon)}(\theta)
 \overline{U_{k',\ell'}^{(\epsilon)}(\theta)}\,d\theta .
\tag{175.R22b}
\]

No sign, vanishing, or \(\beta\ge1/2\) assertion for this transformed
tuple follows from (175.R22b).

### 3.3 Exact recovery of the literal coefficient and the omitted-frequency seam

Let

\[
 V_\epsilon^{\rm all}(\theta):=
 \sum_{k\ {\mathrm{odd}}}\sum_{\ell\in\mathbb Z}
 \chi_4(k)U_{k,\ell}^{(\epsilon)}(\theta).
\tag{175.R23}
\]

With the packet's Fourier convention, the two Dirac-comb identities are

\[
\begin{aligned}
 \sum_{k\ {\mathrm{odd}}}\chi_4(k)e(-kx/4)
 &=\bigl(e(-x/4)-e(-3x/4)\bigr)\sum_{a\in\mathbb Z}e(-ax)\\
 &=-2i\sum_{d\ {\mathrm{odd}}}\chi_4(d)\delta(x-d),\\
 \sum_{\ell\in\mathbb Z}e(-\ell y)&=\sum_{m\in\mathbb Z}\delta(y-m).
\end{aligned}
\tag{175.R24}
\]

At an integer sample \((d,m)\), the strict support
\(\operatorname{supp}\varphi\subset(-1/2,1/2)\) and \(\varphi(0)=1\)
give exactly

\[
 \mathcal W_\epsilon(d,m)=(-1)^{\epsilon m}\lambda_{dm}(d)
 \quad(d,m\ge1, d\ {\mathrm{odd}}),
\tag{175.R25}
\]

with no neighboring-cell or hard-endpoint interpolation.  Hence

\[
\begin{aligned}
 V_\epsilon^{\rm all}(\theta)
 &=-2i\sum_{\substack{d,m\ge1\\d\ {\mathrm{odd}}}}
 \chi_4(d)(-1)^{\epsilon m}\lambda_{dm}(d)
 e(J\sqrt{dm}+\theta dm)\\
 &=-2i\sum_N(-1)^{\epsilon N}c_N^{\rm rem}
 e(J\sqrt N+\theta N)\\
 &=-2iP_\epsilon(\theta).
\end{aligned}
\tag{175.R26}
\]

The middle equality uses only that \(d\) is odd, so \(m=N/d\) has the same
parity as \(N\).  Multiplication by the literal \(i/2\) gives
\((i/2)V_\epsilon^{\rm all}=P_\epsilon\).  Subtracting the entire
\(\ell=0\) sum gives (175.R5):

\[
 {i\over2}V_\epsilon
 ={i\over2}\left(V_\epsilon^{\rm all}
 -\sum_{k\ {\mathrm{odd}}}\chi_4(k)U_{k,0}^{(\epsilon)}\right)
 =P_\epsilon-C_\epsilon.
\tag{175.R27}
\]

In particular, the difference between the target and the all-frequency
comparison is the single collective expression

\[
 |P_\epsilon-C_\epsilon|^2-|P_\epsilon|^2
 =|C_\epsilon|^2-2\Re(P_\epsilon\overline{C_\epsilon}),
\tag{175.R28}
\]

not two separately disposable \(\ell=0\) sectors.  Formula (175.R28) is to
be summed over both \(\epsilon\), all odd character frequencies, and the
whole endpoint difference before using any claimed target-safe correction.

### 3.4 Sliding-window/martingale form of the complete physical comparison

This subsection is an exact comparison, not an unauthorized replacement of
the residual target.  For a zero-extended finite sequence \(a_n\), put

\[
 Q_R(a):=\int_0^1F_R(\theta)
 \left|\sum_na_ne(n\theta)\right|^2d\theta.
\tag{175.R29}
\]

Since
\(F_R=R^{-1}|\sum_{s=0}^{R-1}e(s\theta)|^2\), Parseval gives the exact,
non-cyclic window identity

\[
 Q_R(a)={1\over R}\sum_{t\in\mathbb Z}
 \left|\sum_{n=t-R+1}^{t}a_n\right|^2
 =\sum_{n,n'}f_R(n-n')a_n\overline{a_{n'}}.
\tag{175.R30}
\]

All windows meeting a support birth or death are included because the
sequence is zero-extended and \(t\) runs over the full integer line.  For
the literal two parity branches,

\[
\begin{aligned}
 \mathscr Q_R(z)
 &:={1\over2}\sum_{\epsilon=0}^1Q_R
 \bigl(((-1)^{\epsilon n}z_n)_n\bigr)\\
 &={1\over2R}\sum_{\epsilon=0}^1\sum_{t\in\mathbb Z}
 \left|\sum_{n=t-R+1}^{t}(-1)^{\epsilon n}z_n\right|^2\\
 &=\sum_{\substack{n,n'\in\mathbb Z\\n\equiv n'\pmod2}}
 f_R(n-n')z_n\overline{z_{n'}}.
\end{aligned}
\tag{175.R31}
\]

Thus the all-frequency stopped chain is simply

\[
 \mathscr Q_M(z)-\mathscr Q_{R_0}(z).
\tag{175.R32}
\]

Even at a genuinely dyadic link this is a correlation, not a positive
Haar gain.  Writing
\(A_R(t)=\sum_{n=t-R+1}^{t}a_n\), one has

\[
 Q_{2R}(a)-Q_R(a)
 ={1\over R}\Re\sum_tA_R(t)\overline{A_R(t-R)}.
\tag{175.R33}
\]

For the possible strict link \(R<S<2R\), with
\(A_S(t)=A_R(t)+A_{S-R}(t-R)\), the exact formula is

\[
\begin{aligned}
 Q_S(a)-Q_R(a)
 &=\left({1\over S}-{1\over R}\right)\sum_t|A_R(t)|^2
 +{1\over S}\sum_t|A_{S-R}(t-R)|^2\\
 &\quad+{2\over S}\Re\sum_tA_R(t)
 \overline{A_{S-R}(t-R)}.
\end{aligned}
\tag{175.R34}
\]

Summing (175.R33) and (175.R34) returns (175.R32); it creates no further
martingale square or orthogonality.

The supplied energy gives only the coefficient-insensitive estimates

\[
 0\le\mathscr Q_R(z)\le R D_L,
 \qquad
 \mathscr Q_{R_0}(z)\ll_\varepsilon L^3X^\varepsilon,
 \qquad
 \mathscr Q_M(z)\ll_\varepsilon L^4X^\varepsilon.
\tag{175.R35}
\]

The first inequality follows directly from (175.R30) by the \(\ell^2\)
norm bound for convolution with an interval of length \(R\).  Therefore
the lower endpoint is already at target scale, while the upper endpoint
retains exactly the stated positive capacity.  The scale chain alone does
not save the missing factor \(L\).

### 3.5 What the selector does and does not do algebraically

For a selected pair, (175.R8) is exactly the mask

\[
 \rho_N(d)=
 \begin{cases}
 1,&d\text{ contains both or neither of }p_N,q_N,\\
 0,&d\text{ contains exactly one of }p_N,q_N.
 \end{cases}
\tag{175.R36}
\]

It is independent of every Fejer scale.  The near-ratio involution
\(d\mapsto dq_N/p_N\) acts only between the two exactly-one states, both of
which have zero residual weight.  The toggle between the two retained
states is multiplication or division by \(p_Nq_N\).  Since distinct odd
primes have \(p_Nq_N\ge15>2\), a divisor and its \(p_Nq_N\)-toggle cannot
both lie in the hard interval \([\sqrt N,2\sqrt N]\).  The complementary
divisor also lies outside that same hard face: for odd squarefree
\(N>1\), \(N/d<\sqrt N\) when \(d\ge\sqrt N\), while for even \(N\),
\(M_N/d=N/(2d)\le\sqrt N/2\).  Thus neither elementary involution yields a
pairwise cancellation inside the literal residual divisor sum.

This does not rule out a deeper correlation involving different \(N\)'s,
the chirp, or a joint transform.  It does show that no selector identity
modifies (175.R20)--(175.R21), and the hypotheses state no cross-\(N\)
compatibility of the independently selected pairs.  Any such saving would
have to be a new endpoint-correlation theorem, not a cross-link scale
identity.

## 4. First doubtful or unproved step

The first unproved step toward (175.R15) is an actual-symbol estimate for
the endpoint functional

\[
 {1\over2}\sum_{\epsilon=0}^1\int_0^1
 (F_M-F_{R_0})(\theta)
 |P_\epsilon(\theta)-C_\epsilon(\theta)|^2\,d\theta,
\tag{175.R37}
\]

or a stronger target-scale bound for its \(F_M\) term.  The energy estimate
in (175.R10) controls the complete physical polynomial only up to
\(MD_L\ll L^4X^\varepsilon\), and the packet supplies no estimate of the
collective \(C_\epsilon\) endpoint correlation from which the missing
factor \(L\) follows.  Conditions (175.R7)--(175.R9) do not by themselves
produce a scale identity or a cross-\(N\) selector pairing.

Accordingly, claiming (175.R15) immediately after telescoping would be the
first invalid step: it merely renames the original whole-chain aggregate
as its Fejer endpoint difference.  The exact identity proves a method
no-go, not the target estimate.

The mechanisms not excluded by this no-go are:

1. cancellation in the exact endpoint correlations (175.R22) using the
   undephased chirp \(e(J\sqrt N)\) and the literal amplitude;
2. a genuinely cross-\(N\) squarefree/selector theorem proved uniformly
   for the deterministic selection rule;
3. a divisor or joint \((x,y,\theta)\)-transform not reducible to the
   elementary involutions in Section 3.5;
4. collective odd-character and two-parity cancellation before any
   modulus; and
5. the complete, paid-once \(\ell=0\) and short-shift recombinations
   allowed by the packet, with their exact cross terms retained.

## 5. Required controls and outcomes

### 5.1 Six broader controls

1. **Arbitrary coefficients with the same support and energy.**  The
   identity (175.R18) is unchanged.  Moreover take coefficients equal to
   one on the even sites of an interval of cardinality \(M\) and zero
   elsewhere.  Their energy is \(\asymp M\), both absolute-parity branches
   coincide, and the terms with even
   \(R_0\le |r|\le M/2\) in (175.R31) give
   \(\mathscr Q_M\gg M^2\), whereas
   \(\mathscr Q_{R_0}\le R_0D\ll MR_0\).  Since
   \(M\asymp L^2\) and \(R_0\asymp L\), the endpoint difference has
   \(\asymp L^4\) capacity.  **Outcome:** the telescope survives and can
   retain the false-control capacity, so it fails the required
   coefficient-sensitive discriminator.

2. **Phase-dechirped one-parity coefficients.**  Neither (175.R18) nor
   (175.R20) uses the chirp or the second parity branch.  The constant-block
   example after dechirping already has an order-\(M^2\) endpoint.
   **Outcome:** the scale argument survives this forbidden shadow and is
   not a factor-\(L\) mechanism.

3. **Constant-character shadow.**  Factorization and Fejer telescoping hold
   with \(\chi_4(k)\) replaced by any fixed frequency weights, including a
   constant character.  The character is used only in the physical
   recombination (175.R24)--(175.R26), not in the scale identity.
   **Outcome:** the proposed scale saving does not fail this shadow and is
   therefore non-discriminating.

4. **Erased-selector shadow \(\rho_N\equiv1\).**  Changing \(\rho_N\)
   changes \(V_\epsilon\) but not a single scale multiplier
   \(b_{R,S}(r)\).  **Outcome:** telescoping survives verbatim and supplies
   no selector-specific saving.

5. **One-site physical array.**  For
   \(a_n=a\mathbf1_{n=n_0}\), (175.R30) gives
   \(Q_R(a)=|a|^2\) for every \(R\), because exactly \(R\) zero-extended
   windows contain the site.  Hence its endpoint difference is exactly
   zero in each parity branch.  **Outcome:** the scale telescope gives an
   even stronger cancellation for this forbidden degenerate model; it is
   therefore a tautology rather than evidence for the literal arithmetic
   coefficient.  With \(\ell=0\) omitted, (175.R18) still holds, though its
   endpoint need not vanish.

6. **A model leaving an isolated fixed transformed dual diagonal.**  For
   one fixed \(\alpha=(\epsilon,k,k',\ell,\ell')\), the exact statement is
   (175.R22b): its link integrals telescope to the corresponding endpoint
   integral.  No sign or quantitative saving follows.  **Outcome:** the
   scale operation survives this forbidden isolated-dual model and merely
   returns its endpoint, so it is not a factor-\(L\) discriminator.
   Separately, in the complete physical polynomial, a two-site same-parity
   array with even gap \(r\in[R_0,M/2]\) isolates the physical shifts
   \(\pm r\), and (175.R3) gives
   \(\beta_{M,R_0}(r)\ge1/2\).  This physical-gap control is not an
   identification of \(r\) with the transformed dual tuple.

Thus the exact scale identity fails all six mandated tests for a genuine
factor-\(L\), actual-coefficient mechanism.  These are method controls, not
lower bounds for the literal coefficient and not counterexamples to
(175.R15).

### 5.2 Normalization, endpoint, and ownership controls

- **Cardinal interval and zero extension:** (175.R30)--(175.R31) use the
  stated interval of exact cardinality \(M\) and sum all boundary-crossing
  windows on the full integer line; no periodic wrap is introduced.
- **Hard point values and cells:** (175.R25) uses the strict bump support
  and \(\varphi(0)=1\), so each integer cell contributes its literal
  \(\lambda_{dm}(d)\); no shell face or point value is smoothed or moved.
- **Arithmetic openings:** no divisor or squarefree condition is opened or
  bounded before (175.R26); \(\omega_L\rho_NA_N\) is preserved as one
  literal coefficient.  Section 3.5 tests only exact involutions.
- **Ordinary frequencies and transitions:** every \(r\), including the
  transition \(|r|=R_0\), is retained.  At that transition the lower Fejer
  coefficient is exactly zero and
  \(\beta(R_0)=1-R_0/M\); at \(|r|=M\), the coefficient is exactly zero.
- **Terminal link:** (175.R18), (175.R21), and (175.R34) retain the exact
  upper endpoint \(S=M\), including
  \(R_{K-1}<M<2R_{K-1}\) when that strict case occurs; no dyadic completion
  or duplicated endpoint is used.
- **Parity and constants:** both \(\epsilon=0,1\) branches are added after
  squaring.  The exact \(-2i\) comb, \(i/2\) recovery, \(1/8\) prefactor,
  and resulting \(1/2\) physical normalization are all visible in
  (175.R17) and (175.R24)--(175.R27).
- **Omitted \(\ell=0\) ownership:** the target is always
  \(|P_\epsilon-C_\epsilon|^2\).  Formula (175.R28) records the only
  complete restoration; neither a lone zero-frequency square nor a cross
  term is silently dropped or paid linkwise.
- **Rank-one peaks:** the two parity energies are nonnegative and are added,
  not subtracted.  The even-site block makes the two branches identical and
  simultaneously rank one at the relevant centered peak, yet still has
  order-\(M^2\) endpoint capacity.  Rank one therefore supplies no scale
  orthogonality.

No numerical experiment was used; all controls are exact algebraic tests.

## 6. Dependencies and exact artifacts used

Only the following two permitted artifacts were read:

1. `protocol.md`;
2. `rounds/codex-managed/m9-m2-hard-top-t1-residual-whole-chain-actual-symbol-scale-correlation-gate/blind_statement.md`.

No active campaign file, proof graph, proof draft, failure ledger, strategy,
prior report, kernel, conductor note, sibling artifact, web source, or
external theorem was read or used.  The derivation uses only finite Fourier
factorization, the Dirac-comb/Poisson identity for a smooth compactly
supported function, finite Fejer telescoping, and Parseval for a finite
trigonometric polynomial.

## 7. Recommended state effect

**Promote, after an independent seam check, only the exact no-go lemma
(175.R1)--(175.R3) and its complete-frequency seam
(175.R23)--(175.R32):** the whole stopped scale chain is exactly the two
Fejer endpoints.  For an isolated fixed transformed dual tuple, the only
exact scale statement is the endpoint telescope (175.R22b), from which no
factor-\(L\) saving follows.  Reject “cross-link scale correlation” as an
independent factor-\(L\) mechanism.

Retain (175.B10) as open.  No implication is claimed for full \(t=1\),
complete hard TOP, BAL, UNBAL, M9--M2, M9, a bridge, the quarter theorem, or
an exponent.  A future attempt must attack the exact actual-symbol endpoint
correlations or one of the surviving mechanisms in Section 4, with the
collective \(\ell=0\) and paid-once short-shift seams kept owner-complete.




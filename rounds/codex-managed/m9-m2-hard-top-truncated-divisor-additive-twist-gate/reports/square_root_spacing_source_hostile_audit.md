# Round 161 source and hostile audit: square-root spacing at a fixed centre

## 1. Result: a route-scoped source/capacity no-go

Let

\[
 \mathcal T_L^{\rm ns}
 =\sum_{\substack{D>1\\D\ {\rm squarefree}}}\sum_{t\geq 1}
 B_D(t)e(tJ\sqrt D)
\]

be the literal Round-161 nonsquare hard-TOP scalar. The classical
large-sieve, Bombieri--Iwaniec double-large-sieve, Robert--Sargos
square-root-spacing/monomial, and Miller additive-twist results audited
below do **not** prove

\[
 |\mathcal T_L^{\rm ns}|\ll_\varepsilon L^{3/2}X^\varepsilon
 \qquad (J=\sqrt X,\quad 1\ll L\ll H\asymp J^{1/2})
\tag{161.S1}
\]

for the literal coefficient. There are two independent, exact failures.

1.  A common-test or double-large-sieve theorem applies to a rank-one
    array (a_D b_t), whereas the physical array is the varying matrix
    (B_D(t)). After a general decomposition
    (B=\sum_r a_r\otimes b_r), the cited theorem charges a weighted
    collision/projective norm. On the mandatory (t=1), (D\asymp L^2)
    stratum, the test space is one-dimensional. Its dual large-sieve
    operator norm is exactly (R^{1/2}) for (R) rows, independently of
    square-root spacing, and the circular collision norm reduces to the
    row (\ell^1)-norm. Thus this source route supplies no cancellation at
    all on the singleton stratum. It can only be repaired by a new theorem
    using the arithmetic signs of the literal (B_D(1)) across (D).
2.  Even granting, counterfactually, a cost-one separation of every joint
    hard profile, the direct Robert--Sargos three-dimensional monomial
    theorem restores

    \[
      J^{1/4}L^{3/2}+L^{7/4}
      =X^{1/8}L^{3/2}+L^{7/4}.
    \]

    In the strict hard-TOP range (L\ll J^{1/2}), its first term is worse
    than the trivial (L^2) estimate. Taking the better of the source
    bound and the trivial estimate therefore still gives only (L^2).

This is a no-go only for the audited coefficient-uniform
spacing/double-large-sieve/direct-monomial/additive-twist mechanisms. It is
not a lower bound for the physical scalar, and it does not rule out a new
coefficient-sensitive estimate in the (D)-variable.

There is one useful positive localization: the accepted fixed-channel
bound already makes all (D\leq L) channels target-safe in aggregate.
Consequently the unpaid capacity lies in the large-(D), short-channel
region, whose endpoint is precisely the (t=1) obstruction above.

## 2. Exact statement and hypotheses

### 2.1 Literal matrix before any source theorem

The frozen parameters are

\[
 J=\sqrt X,\qquad y=\lfloor J\rfloor,\qquad
 q_X=X/y^2,\qquad H=\lfloor yX^{-1/4}\rfloor,
 \qquad 1\ll L\ll H.
\tag{161.S2}
\]

The square sector has been removed only through its accepted norm owner.
For (D>1) squarefree,

\[
 B_D(t)=L^{3/2}(Dt^2)^{-3/4}C_L(Dt^2)
          1_{Dt^2\asymp L^2}.
\tag{161.S3}
\]

Its full incidence expansion is

\[
\begin{aligned}
B_D(t)=
\sum_{d_1d_2=D}
\sum_{\substack{guv=t\\(d_1u,d_2v)=1\\
 g,d_1,u\ {\rm odd}\\d_2v^2\leq d_1u^2\leq4d_2v^2}}
 &\chi_4(gd_1)\eta_L(gd_1u^2)
 \Phi\!\left(\frac{gd_1u^2}{H+1}\right)\\
 &\times\left(\frac{L^2}{Dt^2}\right)^{3/4}
 W\!\left(\sqrt{\frac{q_Xd_1u^2}{4d_2v^2}}\right),
\end{aligned}
\tag{161.S4}
\]

where (d_1,d_2) are squarefree, and the exact product shell, half-open
block, floors, hard cone entries and exits, profile endpoint values, and
literal zero extension remain in force. Formula (161.S4) follows from the
bijective coordinates

\[
 h=gd_1u^2,\qquad m=gd_2v^2,\qquad d_1d_2=D,
 \qquad t=guv.
\tag{161.S5}
\]

The only accepted norm inputs are

\[
 \sum_{D,t}|B_D(t)|^2\ll L^2\log(2L),
 \qquad
 \sum_t|B_D(t)|\ll_\varepsilon
       (1+L/\sqrt D)L^\varepsilon.
\tag{161.S6}
\]

For a dyadic radical layer (D\asymp\Delta), (161.S3) gives

\[
 R_\Delta\ll\Delta,\qquad
 t\asymp T_\Delta:=1+\frac{L}{\sqrt\Delta},
 \qquad \Delta\ll L^2.
\tag{161.S7}
\]

Thus the matrix moves continuously from long rows at small (D) to one-
or few-entry rows at (Delta\asymp L^2).

### 2.2 Primary-source theorem cards

**Montgomery--Vaughan, Theorem 1, equations (1.1), (1.3), (1.4).** In
H. L. Montgomery and R. C. Vaughan, *The large sieve*, Mathematika 20
(1973), 119--134, let

\[
 S(x)=\sum_{M<n\leq M+N}a_ne(nx),\qquad
 \delta=\min_{r\ne s}\|x_r-x_s\|_{\mathbb R/\mathbb Z},
\]

where (M) is an integer, (N>0) is an integer, (a_n) are arbitrary
complex numbers, and the real (x_r) are distinct modulo one. Then

\[
 \sum_r|S(x_r)|^2<(N+\delta^{-1})
       \sum_{M<n\leq M+N}|a_n|^2.
\tag{161.S8}
\]

Primary PDF:
[Montgomery--Vaughan, *The large sieve*](https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf).
The averaging variables on the left are the frequencies (x_r); there is
one common coefficient vector ((a_n)), and the norm is its (\ell^2)-norm.

**Bombieri--Iwaniec, Lemma 2.4.** In E. Bombieri and H. Iwaniec, *On the
order of \(\zeta(1/2+it)\)*, Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4) 13
(1986), 449--472, let (\mathcal X,\mathcal Y\subset\mathbb R^K), let
(a(x),b(\eta)) be arbitrary complex numbers, and let (X_k,Y_k>0).
They define

\[
 \mathcal B(b;X)=
 \sum_{\substack{\eta,\eta'\in\mathcal Y\\
 |\eta_k-\eta'_k|\leq(2X_k)^{-1}\ (1\leq k\leq K)}}
 |b(\eta)b(\eta')|,
\]

\[
 \mathcal B(a;Y)=
 \sum_{\substack{x,x'\in\mathcal X\\
 |x_k-x'_k|\leq(2Y_k)^{-1}\ (1\leq k\leq K)}}
 |a(x)a(x')|,
\]

and

\[
 \mathcal B(a,b;\mathcal X,\mathcal Y)=
 \sum_{\substack{x\in\mathcal X,\ |x_k|\leq X_k\\
                  \eta\in\mathcal Y,\ |\eta_k|\leq Y_k}}
 a(x)b(\eta)e(x\mathbin{\cdot}\eta).
\]

Their conclusion is

\[
 |\mathcal B(a,b;\mathcal X,\mathcal Y)|^2
 \leq (2\pi^2)^K\prod_{k=1}^K(1+X_kY_k)
       \mathcal B(b;X)\mathcal B(a;Y).
\tag{161.S9}
\]

Primary PDF:
[Bombieri--Iwaniec, *On the order of \(\zeta(1/2+it)\)*](https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf).
This is a bilinear theorem with separable coefficients (a(x)b(\eta));
its norms are absolute weighted near-collision sums, not merely two
(\ell^2)-norms.

**Robert--Sargos, Lemma 8, Theorems 1 and 2.** In O. Robert and P. Sargos,
*Three-dimensional exponential sums with monomials*, J. reine angew.
Math. 591 (2006), 1--20, Lemma 8 treats

\[
 S_1=\sum_{k\leq K}\sum_{\ell\leq L}
 a(k)b(\ell)e(\Xi u(k)v(\ell)),
\]

with (|a(k)|,|b(\ell)|\leq1), bounded real (u(k),v(\ell)), and
(\Xi\gg1). If (B_1,B_2) count pairs with respectively
(|u(k_1)-u(k_2)|\leq\Xi^{-1}) and
(|v(\ell_1)-v(\ell_2)|\leq\Xi^{-1}), then

\[
 |S_1|\ll \Xi^{1/2}B_1^{1/2}B_2^{1/2}.
\tag{161.S10}
\]

Theorem 2 fixes a real (\alpha\ne0,1), an integer (M\geq2), and
(\delta>0). If (N(M;\delta)) counts (M<m_i\leq2M) satisfying

\[
 |m_1^\alpha+m_2^\alpha-m_3^\alpha-m_4^\alpha|
 \leq\delta M^\alpha,
\]

then

\[
 N(M;\delta)\ll_\varepsilon
 M^{2+\varepsilon}+\delta M^{4+\varepsilon}.
\tag{161.S11}
\]

Theorem 1 considers

\[
 S_0=\sum_{H_0<h\leq2H_0}\sum_{N_0<n\leq2N_0}
     \sum_{M_0<m\leq2M_0}
 a(h,n)b(m)e\!\left(
 \Xi\frac{h^\beta n^\gamma m^\alpha}
 {H_0^\beta N_0^\gamma M_0^\alpha}\right),
\]

where (H_0,N_0,M_0) are positive integers, (Xi>1),
(|a(h,n)|,|b(m)|\leq1), and the fixed real exponents obey
(\alpha(\alpha-1)\beta\gamma\ne0). It proves

\[
 S_0\ll_\varepsilon(H_0N_0M_0)^{1+\varepsilon}
 \left\{
 \left(\frac{\Xi}{H_0N_0M_0^2}\right)^{1/4}
 +(H_0N_0)^{-1/4}+M_0^{-1/2}+\Xi^{-1/2}
 \right\}.
\tag{161.S12}
\]

Primary PDF:
[Robert--Sargos, *Three-dimensional exponential sums with monomials*](https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf).
Theorem 2 averages/counts four independent integer variables in a real
Euclidean inequality. It is not a theorem about one fixed centre modulo
one. Lemma 8 and Theorem 1 both require coefficient separation.

**Miller, Theorem 1.1.** In Stephen D. Miller, *Cancellation in additively
twisted sums on GL(n)*, Amer. J. Math. 128 (2006), 699--729, if
(a_{q,n}) are the Fourier coefficients of one fixed cusp form on
(GL(3,\mathbb Z)\backslash GL(3,\mathbb R)), then for every
(\varepsilon>0)

\[
 \sum_{n=1}^{T}a_{q,n}e(n\alpha)
 =O_\varepsilon(T^{3/4+\varepsilon})
 \quad\hbox{uniformly for }\alpha\in\mathbb R,
\tag{161.S13}
\]

with the implied constant depending on (q,\varepsilon), and the cusp
form. Primary PDF:
[Miller, *Cancellation in additively twisted sums on GL(n)*](https://arxiv.org/pdf/math/0404521).
The averaged variable is (n\leq T), and the coefficient hypothesis is
automorphic, not an arbitrary divisor-like finite vector.

## 3. Proof or derivation

### 3.1 The literal layer geometry and the harmless long-channel range

From (161.S6), without invoking any external theorem,

\[
\begin{aligned}
 \sum_{\substack{D\leq L\\D\ {\rm sf}}}
 \left|\sum_tB_D(t)e(tJ\sqrt D)\right|
 &\leq \sum_{D\leq L}\sum_t|B_D(t)|\\
 &\ll_\varepsilon
 \left(L+L\sum_{D\leq L}D^{-1/2}\right)L^\varepsilon
 \ll_\varepsilon L^{3/2+\varepsilon}.
\end{aligned}
\tag{161.S14}
\]

Thus small (D), including the longest channels, is already target-safe.
The (+1) in the fixed-channel capacity accumulates only when there are
many large radicals. In (161.S7), (R_\Delta/T_\Delta) becomes large as
(\Delta) approaches (L^2), so the hard source test must survive many
rows with few columns.

### 3.2 What the large sieve literally sees

Put

\[
 \alpha_D=J\sqrt D\pmod1.
\]

Montgomery--Vaughan maps (n=t), (x_r=\alpha_D), and
(N\asymp T_\Delta), but only for a single vector (c_t). It estimates

\[
 \sum_D\left|\sum_t c_t e(t\alpha_D)\right|^2,
\tag{161.S15}
\]

not

\[
 \sum_D\sum_tB_D(t)e(t\alpha_D).
\tag{161.S16}
\]

No choice (c_t=B_D(t)) is legal because (c_t) would then depend on the
frequency being averaged. Duality does not remove this mismatch; it moves
the same operator constant to the adjoint.

For a rank-one matrix (a_D b_t), Bombieri--Iwaniec does give the relevant
bilinear scalar. Take (K=1), lift the (alpha_D)'s to a bounded arc,
(x=\alpha_D), (eta=t), (X_1\asymp1), and
(Y_1\asymp T_\Delta). A bounded arc partition is required to retain
wraparound. With

\[
 \mathcal C_T(a):=
 \sum_{\substack{D,E\\
 \|\alpha_D-\alpha_E\|_{\mathbb R/\mathbb Z}\leq c/T}}
 |a_Da_E|,
\tag{161.S17}
\]

(161.S9) yields, up to an absolute constant and adjacent-column terms,

\[
 \left|\sum_{D,t}a_Db_te(t\alpha_D)\right|
 \ll T^{1/2}\mathcal C_T(a)^{1/2}\|b\|_2.
\tag{161.S18}
\]

The Robert--Sargos Lemma-8 map
(u(D)=\alpha_D), (v(t)=t/T), (Xi=T) gives the same collision
scale and the same rank-one restriction. Reducing (alpha_D) modulo one
without the arc/wrap ledger is not legal.

For the physical matrix, define the collision-adapted factorization cost

\[
 \mathfrak P_T(B;\alpha)=
 \inf_{B=\sum_r a_r\otimes b_r}
 \sum_r\mathcal C_T(a_r)^{1/2}\|b_r\|_2.
\tag{161.S19}
\]

Then the actual conclusion obtainable from Lemma 2.4 is only

\[
 |\mathcal T_{L,\Delta}^{\rm ns}|
 \ll T_\Delta^{1/2}\mathfrak P_{T_\Delta}(B;\alpha).
\tag{161.S20}
\]

No bound for (161.S19) is contained in (161.S6).

Even under the fictitious best case that every collision form in
(161.S19) is diagonal, (161.S19) becomes the Hilbert projective norm

\[
 \pi_2(B):=\inf_{B=\sum_r a_r\otimes b_r}
       \sum_r\|a_r\|_2\|b_r\|_2,
\tag{161.S21}
\]

which is the nuclear norm of the matrix. The accepted energy controls only
the Frobenius norm,

\[
 \|B\|_F\ll L\sqrt{\log(2L)}.
\]

Since the zero-extended matrix has (O(L)) columns, the generic consequence
is merely

\[
 \pi_2(B)\leq \sqrt{\operatorname{rank}B}\,\|B\|_F
 \ll L^{3/2}\sqrt{\log(2L)}.
\tag{161.S22}
\]

At the global (T\asymp L) scale, (161.S20)--(161.S22) give
(L^{2}\sqrt{\log(2L)}), not (161.S1). A successful ideal-diagonal
version of this route would need a genuinely new literal estimate of size

\[
 \pi_2(B)\ll L^{1+o(1)}
\tag{161.S23}
\]

or a comparably strong collision-adapted substitute. Termwise expansion of
(161.S4), followed by the triangle inequality, gives back the original
positive (L^{2+o(1)}) product-cone capacity; it does not prove
(161.S23).

### 3.3 The decisive (t=1), large-(D) capacity obstruction

When (t=1), (161.S5) forces

\[
 g=u=v=1.
\]

Consequently (D=d_1d_2\asymp L^2), and

\[
\begin{aligned}
B_D(1)=
\sum_{\substack{d_1d_2=D\\(d_1,d_2)=1\\d_1\ {\rm odd}\\
d_2\leq d_1\leq4d_2}}
 &\chi_4(d_1)\eta_L(d_1)
 \Phi\!\left(\frac{d_1}{H+1}\right)
 \left(\frac{L^2}{D}\right)^{3/4}\\
 &\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right),
\end{aligned}
\tag{161.S24}
\]

with all literal endpoints and zero extension retained. For a close product
(D=pq) of distinct odd primes with (p<q\leq4p), the admissible
upper-near-square orientation is (d_1=q,d_2=p); such a row has one
product-fibre incidence. Therefore no unproved cancellation inside its
divisor fibre may be inserted.

Now take any (R) distinct active (t=1) rows. The adjoint of the
Montgomery--Vaughan operator at sequence length (N=1) is

\[
 (a_D)_{D\in\mathcal D}\longmapsto
 \sum_{D\in\mathcal D}a_De(\alpha_D).
\tag{161.S25}
\]

Its (\ell^2(\mathcal D)\to\mathbb C) operator norm is **exactly**
(R^{1/2}), since its row vector has (R) entries of modulus one. No
spacing fact can reduce this norm for arbitrary coefficients. Equivalently,
for (R) points on the circle, (delta\leq1/R), so the dual of
(161.S8) has (1+\delta^{-1}\geq R), exactly the Cauchy capacity.
Repeated frequencies only make the common-test theorem less applicable.

The double-large-sieve ledger says the same thing under its natural
singleton specialization. Represent the circular frequencies in
([-1/2,1/2)), and take (K=1), (X_1=1/2), and (Y_1=T=1). Partitioning
the representative interval into its two half intervals gives

\[
 \frac12\left(\sum_D|a_D|\right)^2
 \le \mathcal C_1(a)
 \le \left(\sum_D|a_D|\right)^2.
\tag{161.S26}
\]

For a one-column matrix, the infimum in (161.S19) is therefore, up to an
absolute constant, exactly

\[
 \mathfrak P_1(B;\alpha)\asymp\sum_D|B_D(1)|.
\tag{161.S27}
\]

Thus this source-legal specialization of (161.S20) becomes absolute
summation on the mandatory singleton layer. This is not a claim that
optimizing every Bombieri--Iwaniec box parameter has the same displayed
norm; the independent exact one-column operator norm above already
carries the coefficient-uniform obstruction. If one uses only the
accepted global energy and the ambient
(R\asymp L^2) large-radical capacity, Cauchy permits

\[
 \sum_D|B_D(1)|
 \leq R^{1/2}\left(\sum_D|B_D(1)|^2\right)^{1/2}
 \ll L^2\sqrt{\log(2L)},
\tag{161.S28}
\]

which still misses (161.S1) by (L^{1/2-o(1)}). Equation (161.S28) is a
capacity statement, not an assertion that the physical (t=1) mass has
that size. Its force is that the cited coefficient-uniform spacing sources
cannot lower it. Cross-(D) cancellation in (161.S24) would require a new
theorem about that literal signed sequence.

More generally, partitioning the circle into (O(T)) arcs of length
(O(1/T)) shows that (R) unweighted frequency points have at least

\[
 \gg R^2/T
\tag{161.S29}
\]

ordered near-collision pairs. Hence whenever (R\gg T), even an optimally
distributed frequency family cannot have diagonal collision capacity at
the test resolution. The endpoint (T=1) is the complete collapse.

### 3.4 Exact and near resonance at an arbitrary fixed centre

If (J\sqrt{D_i}\in\mathbb Z) for two squarefree (D_1,D_2>1), then
(\sqrt{D_1/D_2}\in\mathbb Q), forcing (D_1=D_2). Thus at most one
whole channel is exactly resonant, and (161.S6) makes it target-safe.

There is no corresponding uniform near-separation statement. A
self-contained simultaneous-approximation control is enough. For fixed
distinct squarefree (D_1,\ldots,D_R>1), place the (Q^R+1) points

\[
 k(\sqrt{D_1},\ldots,\sqrt{D_R})\pmod1,
 \qquad 0\leq k\leq Q^R,
\]

in (Q^R) equal boxes. Two lie in one box, so for some
(1\leq q\leq Q^R),

\[
 \max_i\|q\sqrt{D_i}\|_{\mathbb R/\mathbb Z}\leq Q^{-1}
 \leq q^{-1/R}.
\tag{161.S30}
\]

As (Q\to\infty), the resulting denominators are unbounded; otherwise a
fixed nonzero (q) would make an irrational (q\sqrt{D_i}) integral in
the limit. Choose one such (q), put

\[
 J=q,\qquad X=q^2,\qquad y=q,\qquad q_X=1,\qquad
 H=\lfloor q^{1/2}\rfloor,
\]

and choose an admissible polynomial scale (L\asymp q^\lambda) with

\[
 0<\lambda<\min(1/2,1/R).
\]

Then (1\ll L\ll H) and all selected, nonexact frequencies lie within
(o(1/L)) of zero. This does not make their physical contribution large
(indeed fixed small-(D) collections are covered by (161.S14)); it
rigorously refutes any claimed uniform modulo-one separation deduced only
from uniqueness of exact resonance.

For a general dyadic layer, the collision condition is

\[
 \|J(\sqrt D-\sqrt E)\|_{\mathbb R/\mathbb Z}\leq T^{-1},
\tag{161.S31}
\]

equivalently, for some integer (k),

\[
 |\sqrt D-\sqrt E-k/J|\leq (JT)^{-1}.
\tag{161.S32}
\]

Robert--Sargos Theorem 2 with (\alpha=1/2) counts instead the real
four-root relation

\[
 |\sqrt{m_1}+\sqrt{m_2}-\sqrt{m_3}-\sqrt{m_4}|
 \leq\delta\sqrt M.
\]

It neither counts (161.S31) nor supplies the coefficient-weighted form
(161.S17). Passing from (161.S32) to real inequalities requires a union
over (|k|\ll J\sqrt\Delta), a factor absent from Theorem 2. The source
four-root estimate is useful after appropriate moments or centre averages;
no such average is part of the fixed-centre owner here.

### 3.5 Restored Robert--Sargos powers

Give the direct monomial theorem every benefit not yet proved: ignore the
factorization cost of the cone, (W(h/m)), the product shell, coprimality,
parity, floors, and hard endpoints, and suppose they separate with total
cost one. On (h,m\asymp L), map Theorem 1 by

\[
 H_0\asymp L,\qquad M_0\asymp L,\qquad N_0=1,
 \qquad \alpha=\beta=\tfrac12,\qquad\gamma=1,
 \qquad \Xi\asymp JL.
\tag{161.S33}
\]

The single (n)-value is a harmless fixed constant, and (161.S33)
normalizes the phase to (e(J\sqrt{hm})). Substitution in (161.S12) gives

\[
\begin{aligned}
 |S_0|\ll_\varepsilon L^{2+\varepsilon}
 \bigg\{&\left(\frac{JL}{L^3}\right)^{1/4}
 +L^{-1/4}+L^{-1/2}+(JL)^{-1/2}\bigg\}\\
 \ll_\varepsilon{}&
 J^{1/4}L^{3/2+\varepsilon}
 +L^{7/4+\varepsilon}
 +L^{3/2+\varepsilon}
 +J^{-1/2}L^{3/2+\varepsilon}.
\end{aligned}
\tag{161.S34}
\]

Since (H\asymp J^{1/2}=X^{1/4}) and (L\ll H),

\[
 J^{1/4}L^{3/2}\gg L^2.
\tag{161.S35}
\]

The source estimate is therefore worse than the trivial (L^2) capacity
in the strict hard-TOP range. At the boundary (L\asymp J^{1/2}), it is
still (L^2). Moreover (J^{1/4}=X^{1/8}) is a fixed power and cannot be
absorbed into the (X^\varepsilon) in a theorem asserted for every
(\varepsilon>0). Hence (161.S12) supplies neither (161.S1) nor a strict
polynomial subrange inside (L\ll H), even before restoring the literal
joint-coefficient cost.

### 3.6 Additive twists and fixed-centre recovery do not repair the gap

Miller's Theorem 1.1 is uniform in the additive centre, but its coefficients
must be Fourier coefficients of one fixed (GL(3)) cusp form. For each
(D), (161.S4) is a different finite, truncated, near-square incidence
vector, depending also on (X) through (H,q_X), the floors, and the
profiles. No identification

\[
 B_D(t)=a_{q,t}
\]

with a fixed cusp form is present. Treating (D) as the summation variable
does not help: the phase is (e(J\sqrt D)), not an additive character in
(D). Even a hypothetical rowwise (T_D^{3/4}) estimate would give no
gain at (T_D=1) and would still have to be summed over the many large-
(D) rows. Completing (161.S4) to a full divisor or automorphic sequence
is specifically unavailable: the accepted Round-137 controls leave an
uncontrolled complement and return the localized radial principal family.

Finally, a centre-mean theorem cannot simply be converted to this owner.
As (J) varies, (y,H,q_X), and hence (B_D(t)), vary as well. Even if one
artificially froze the coefficient at a centre (J_0), differentiating the
phase costs

\[
 \frac{d}{dJ}e(tJ\sqrt D)=2\pi i,t\sqrt D\,e(tJ\sqrt D),
 \qquad t\sqrt D\asymp L.
\tag{161.S36}
\]

Thus a Sobolev recovery introduces an (L)-scale derivative price, larger
than the missing (L^{1/2}), before the coefficient derivative and hard
floor jumps are addressed.

## 4. First doubtful or unproved step

The first unproved step in every common-test/double-large-sieve proposal is
the assertion that the literal matrix (161.S4) admits a decomposition for
which the collision-adapted norm (161.S19) is (L^{1+o(1)})-scale after
the layer factors are included. Frobenius energy does not imply this,
termwise incidence separation returns positive capacity, and on the
(t=1) layer (161.S27) proves that the cited spacing theorem itself reduces
to (\ell^1).

The first source-hypothesis failure in a direct monomial proposal is the
unproved separation (a(h,n)b(m)) across the hard cone and the joint
(W(h/m)) profile. Even if that seam is granted for free, the restored
power computation (161.S34)--(161.S35) fails. The first source-hypothesis
failure in an additive-twist proposal is earlier still: (161.S4) is not the
coefficient sequence of a fixed cusp form.

A viable continuation must therefore prove a new coefficient-sensitive
fixed-centre estimate for the signed large-(D) sequence, beginning with
(161.S24), or prove a literal projective/collision norm saving not supplied
by the audited sources. Merely citing square-root spacing, uniqueness of
exact resonance, or a theorem uniform in the additive centre is not such a
step.

## 5. Control tests and outcomes

| Required control | Outcome |
|---|---|
| `literal_product_fibre_and_square_owner` | **Pass.** The report starts from the exact nonsquare scalar. The square sector is removed only by the accepted norm owner; no pointwise or signed square cancellation is borrowed. |
| `unique_radical_linearization` | **Pass.** Equations (161.S3)--(161.S5) retain the bijection (n=Dt^2), (h=gd_1u^2), (m=gd_2v^2), (t=guv). |
| `actual_coefficient_incidence` | **Pass.** The character, oddness, coprimality, cone, profiles, shell, and zero extension are explicit in (161.S4). |
| `fixed_center_exact_resonance` | **Pass.** At most one squarefree radical is wholly resonant, and it is target-safe by (161.S6). |
| `near_resonance_mod_one_collisions` | **Source no-match.** The necessary kernel is (161.S31), including wraparound. Circle packing gives (161.S29), and (161.S30) rules out a uniform separation premise. Robert--Sargos Theorem 2 counts a different real four-root relation. |
| `small_D_long_channels` | **Pass, target-safe stratum.** Equation (161.S14) is already (L^{3/2+\varepsilon}). Near resonance there is harmless for the owner total, but it invalidates a global spacing assertion. |
| `t1_large_D_singleton_layer` | **Decisive no-go for the audited route.** Formula (161.S24) is literal; close semiprime rows can be singleton fibres. The one-column operator norm is exactly (R^{1/2}), and the double-large-sieve projective cost is (\ell^1), (161.S25)--(161.S28). |
| `coefficient_varying_large_sieve_applicability` | **Fail.** Montgomery--Vaughan has one common vector; (B_D(t)) changes with (D). A decomposition is legal only after paying (161.S19). |
| `projective_tensor_bessel_price` | **Fail with present inputs.** Even fictitious diagonal collisions plus the generic nuclear/Frobenius inequality give (L^2\sqrt{\log L}); the singleton collision norm is worse and exactly positive. |
| `hard_profiles_parity_endpoints` | **Pass as retention; no free reduction.** The hard cone inequalities, odd (g,d_1,u), (\chi_4), (eta_L,Phi,W), (q_X), floors, half-open entries/exits, endpoint values, and zero extension remain in (161.S4), (161.S24). None of the sources supplies their unpriced separation. |
| `source_theorem_literal_match` | **Fail.** Exact theorem cards and averaging variables are in Section 2. MV needs one vector; BI/RS Lemma 8 and RS Theorem 1 need separability; RS Theorem 2 has the wrong collision relation; Miller needs fixed cuspidal Fourier coefficients. |
| `missing_L_half_power` | **Unpaid.** The (t=1) source capacity is (L^{2+o(1)}). The direct RS theorem restores (X^{1/8}L^{3/2}+L^{7/4}), and its best combination with triviality is (L^2) for (L\ll H). |
| `self_return_and_full_divisor_exclusions` | **Pass.** No divisibility completion, B-process self-return, complementary-divisor switch, or full-divisor/automorphic completion is used. The inherited uncontrolled complement is not silently discarded. |
| `hard_top_owner_and_downstream_scope` | **Pass.** The conclusion concerns only this nonsquare polynomial-intermediate hard-TOP block. It gives no owner-complete target, no strict polynomial range, no downstream asymptotic, and no exponent improvement. |

No numerical or symbolic experiment was used.

## 6. Dependencies and exact artifacts used

The internal dependencies were exactly the context permitted by the task:

- `protocol.md`;
- `state/proof_obligations.yml` (the active hard-TOP obligations and the
  accepted Round-137 energy/fixed-radical owners);
- `state/active_campaign.yml`;
- `strategy/round161_m2_hard_top_radical_frequency_strategy.md`;
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/barrier_packet.md`;
- `rounds/codex-managed/m9-m2-hard-top-truncated-divisor-additive-twist-gate/candidates/conductor_round161_radical_frequency_seed.md`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/synthesis.md`;
- `rounds/codex-managed/m9-m2-hard-top-product-fibre-divisor-scalar-gate/reviews/conductor_round137_product_fibre_adjudication.md`.

No sibling Round-161 report was read. The external primary artifacts were:

1. H. L. Montgomery and R. C. Vaughan, *The large sieve*, Theorem 1,
   equations (1.1), (1.3), (1.4):
   <https://personal.science.psu.edu/rcv4/personal/Publications/large_sieve.pdf>.
2. E. Bombieri and H. Iwaniec, *On the order of \(\zeta(1/2+it)\)*,
   Lemma 2.4:
   <https://www.numdam.org/item/ASNSP_1986_4_13_3_449_0.pdf>.
3. O. Robert and P. Sargos, *Three-dimensional exponential sums with
   monomials*, Theorem 1, Theorem 2, and Lemma 8:
   <https://perso.univ-st-etienne.fr/rool6510/robert-2006-crelle.pdf>.
4. Stephen D. Miller, *Cancellation in additively twisted sums on GL(n)*,
   Theorem 1.1:
   <https://arxiv.org/pdf/math/0404521>.

## 7. Recommended state effect

**Recommend promotion after conductor seam review of the following narrowly
scoped obstruction under `hard_top_radical_frequency_coupling_no_go`:**

> A coefficient-uniform common-test or double-large-sieve reduction cannot
> close the literal radical-frequency scalar from the accepted energy and
> fixed-radical bounds. On the mandatory (t=1), (D\asymp L^2) stratum,
> the frequency test has one column, its exact dual (\ell^2\)-operator norm
> is (R^{1/2}), and the circular Bombieri--Iwaniec collision/projective norm
> is the row (\ell^1)-norm. The direct Robert--Sargos monomial theorem,
> even after a fictitious cost-one separation of the literal coefficient,
> restores (X^{1/8}L^{3/2}+L^{7/4}) and yields no strict range inside
> (L\ll H\asymp X^{1/4}). Miller's additive-twist theorem has no legal
> coefficient match.

Retain the overall hard-TOP target as open. Do not infer a physical lower
bound, do not reject all possible (D)-variable cancellation, and do not
propagate a target, strict range, downstream owner, or improved exponent
from this report.

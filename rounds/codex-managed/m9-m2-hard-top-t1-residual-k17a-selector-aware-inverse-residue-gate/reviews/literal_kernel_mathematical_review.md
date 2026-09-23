# Round-177 literal-kernel mathematical review

## 1. Verdict

\[
 \boxed{\textbf{GREEN AFTER ONE EDITORIAL SUMMATION REPAIR}}
\]

The formalized candidate and durable kernel are mathematically correct at
their stated subordinate scope. The primitive folding, reduced-conductor
normalization, near-half classification, literal atom count, low-conductor
global bound, two-orientation identity, parity branches, selector and
endpoint retention, and exact Fourier complement all check.

The first defect is only notational: equation (177.K26) leaves
$\tau(u)^2$ in a line where the sum over supported $u$ has already been
replaced by its cardinality. The intended uniform divisor-bound argument
is valid, but the bound variable should be restored explicitly before
promotion. The exact replacement is given in Section 5 below. No theorem,
range, exponent, or owner-scope change is needed.

## 2. Primitive folding and reduced-conductor normalization

Write

\[
 g=(u,n),\qquad u=gu_0,\qquad n=gn_0,\qquad (n_0,u_0)=1.
\]

The accepted cross-gcd coordinates have $u$ odd, hence $g$ and $u_0$ are
odd. Since $(u,v)=1$, the inverse of $v$ modulo $u$ reduces to its inverse
modulo $u_0$. For either sign, the least residue of
$\pm\bar vgn_0$ modulo $gu_0$ is exactly $g$ times the least residue of
$\pm\bar vn_0$ modulo $u_0$. Therefore

\[
 [\pm\bar v n]_u=g[\pm\bar v n_0]_{u_0}
\]

and, because $g$ is odd,

\[
 E_u(\pm\bar v n)=E_{u_0}(\pm\bar v n_0).
\]

There is no missing parity sign in (177.K5).

Using the normalized inversion convention

\[
 E_m(a)=\sum_{k\bmod m}c_m(k)e(ka/m),
\]

one has

\[
\begin{aligned}
 E_u(ga)
 &=\sum_{k\bmod u}c_u(k)e(ka/u_0)\\
 &=\sum_{\ell\bmod u_0}
 \left(\sum_{j=0}^{g-1}c_u(\ell+ju_0)\right)e(\ell a/u_0).
\end{aligned}
\]

Comparison with the unique Fourier expansion of $E_{u_0}(a)$ proves

\[
 \sum_{j=0}^{g-1}c_u(\ell+ju_0)=c_{u_0}(\ell).
\]

Thus (177.K6) has the correct normalization: neither a factor $g$ nor
$g^{-1}$ remains. The signs in the two orientations are unchanged, since
the folding is applied separately to the phases
$e(\pm k\bar vn/u)$ before the two orientations are placed in the common
block (177.K15).

Now let $h=(\ell,u_0)$ and $q=u_0/h$. For $q>1$, write
$\ell=ha$ with $(a,q)=1$. Direct substitution gives

\[
 c_{u_0}(ha)
 ={2\over u_0\{1+e(-a/q)\}}
 ={q\over u_0}c_q(a),
\]

and the reciprocal phase is exactly

\[
 e\!\left(\pm{a\bar vn_0\over q}\right).
\]

Hence $q$, rather than $u$ or $u_0$, is the final additive conductor.
Summing over aliases of exact conductor $q$ gives

\[
\begin{aligned}
 \sum_{\substack{\ell\bmod u_0\\u_0/(\ell,u_0)=q}}
 |c_{u_0}(\ell)|
 &={q\over u_0}
 \sum_{\substack{a\bmod q\\(a,q)=1}}|c_q(a)|\\
 &\ll {q\over u_0}\log(2q).
\end{aligned}
\]

This verifies (177.K8)--(177.K9), including $q=1$, where the unique alias
is $\ell=0$ and $c_{u_0}(0)=1/u_0$.

## 3. Near-half aliases, zero alias, and exact complement

For odd $u_0>1$, the two near-half residues

\[
 \ell={u_0-1\over2},\qquad \ell={u_0+1\over2}
\]

are coprime to $u_0$. Their reduced conductor is therefore $q=u_0$.
Moreover,

\[
 |c_{u_0}(\ell)|
 ={1\over u_0|\cos(\pi\ell/u_0)|}
 ={1\over u_0\sin(\pi/(2u_0))}
 \asymp1.
\]

The kernel correctly retains these aliases in the high-conductor
complement whenever $u_0>Q_B$. At the other extreme, the zero alias has
$q=1$ and weight $1/u_0$, and every intermediate imprimitive alias is
assigned uniquely to

\[
 q={u_0\over(\ell,u_0)}.
\]

Consequently the conditions $q\leq Q_B$ and $q>Q_B$ are disjoint and
exhaust every alias of every primitive gcd stratum. Equation (177.K16)
therefore splits exactly into the proved packet (177.K12) and the
remaining packet (177.K14). The complement is a Fourier-sector
complement, not a claim that the underlying physical incidences split by
$q$ before the DFT; the kernel states this distinction correctly.

If $u_0\leq Q_B$, then every $q\mid u_0$ is in the safe packet. Because
the proof of (177.K12) is a positive capacity bound that remains valid
after deleting other strata, it separately proves the complete physical
sector $u/(u,n)\leq Q_B$. This justifies (177.K13); it is not inferred
merely from cancellation in a larger low-$q$ sum.

## 4. Literal atom count, parity, selector, and endpoints

Fix $(\kappa,u,u_0)$ and put $U=L/\kappa$. Literal support gives
$u,v\asymp U$, $n\ll U$, and at most $O(1+\kappa)$ fibre sites for each
$(v,n)$ and each orientation. Since

\[
 n={u\over u_0}n_0,
\]

one has

\[
 n_0\ll {Uu_0\over u}\ll u_0.
\]

Thus the determinant, inverse-residue, and fibre counts are respectively

\[
 O(u_0),\qquad O(U),\qquad O(1+\kappa),
\]

and

\[
 u_0U(1+\kappa)
 =u_0(L+U)
 \ll u_0L
\]

because $\kappa\geq1$. Both orientations contribute only a fixed factor.
This proves (177.K10). Multiplying by the exact-conductor coefficient
mass proves

\[
 O(u_0L)\,{q\over u_0}\log(2q)
 =O(Lq\log(2q)),
\]

so (177.K11) has every power restored.

The count is valid for both parity branches. In the odd-product branch,
$v$ is odd. In the squarefree even-even branch, $v$ is twice odd and the
accepted constraints force the required parity of $n$ and $w$; since
$u$ is odd, $g,u_0,h,q$ remain odd and $v$ is still invertible modulo
each of them. These conditions only delete candidates from the count.

The proof never opens the squarefree masks and never smooths the
selector. The exact selected neither/both rows and the no-pair rows stay
inside $\Lambda^\pm$. Likewise, the Fejer weight, original-gcd cutoff,
strict displacement inequalities, profiles, floors, stars, hard values,
endpoint conjugations, and zero extension remain inside the inherited
amplitudes. Their absolute values are bounded, so they only delete or
downweight atoms in the strict-sector proof. There is no hidden endpoint
completion term.

The two orientations are combined in (177.K15) before the modulus is
taken. The signs of their reciprocal phases and the endpoint
conjugations agree with the accepted Round-176 identity. In the energy
audit, they also occupy the same residue buckets, so potential
cross-orientation cancellation is not discarded.

## 5. Divisor and global summation

At fixed $(\kappa,u)$, the kernel uses

\[
 \sum_{u_0\mid u}\sum_{\substack{q\mid u_0\\q\leq Q_B}}
 Lq\log(2q)
 \ll LQ_B\log(2Q_B)\tau(u)^2.
\]

This is correct: the number of ordered divisor pairs $q\mid u_0\mid u$
is at most $\tau(u)^2$, and each $q$ in the packet is at most $Q_B$.
There are $O(U)=O(L/\kappa)$ supported values of $u$.

The first and only defect is the free occurrence of $\tau(u)^2$ in
(177.K26) after that $u$-sum has been compressed. Replace (177.K26) by

\[
\begin{aligned}
 \left|\mathfrak C^{\rm rem}_{q\leq Q_B}\right|
 &\ll
 LQ_B\log(2Q_B)
 \sum_{\substack{\kappa<\delta L\\\kappa\ {\rm odd}}}
 \sum_{u\asymp L/\kappa}\tau(u)^2\\
 &\ll_\eta
 LQ_B\log(2Q_B)X^\eta
 \sum_{\kappa<\delta L}{L\over\kappa}\\
 &\ll_\eta
 L^2Q_B\log(2Q_B)\log(2L)X^\eta
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\end{aligned}
\tag{R177.1}
\]

Here $u\ll L\leq X^{1/4}$, so the standard pointwise divisor bound gives
$\tau(u)^2\ll_\eta X^\eta$; choose $\eta$ below the final
$\varepsilon$ and absorb $Q_B$ and the logarithms. This is exactly the
argument intended by the prose following (177.K25). It repairs notation
only and confirms (177.K12) with no changed hypothesis.

As an independent check avoiding the divisor notation, write
$u_0=hq$ and $u=gu_0=ghq$. For fixed $(\kappa,q)$,

\[
 \#\{(g,h):gh\asymp U/q\}
 \ll {U\over q}\log(2U)
\]

up to fixed support constants. Multiplication by
$Lq\log(2q)$ gives
$O(LU\log(2q)\log(2U))$. Summing
$q\leq Q_B$ and then $\kappa$ again gives

\[
 O\!\left(
 L^2Q_B\log(2Q_B)\{\log(2L)\}^2\right)
 \ll_{B,\varepsilon}L^2X^\varepsilon.
\]

The two independent ledgers agree.

## 6. Energy, orientation pairing, and first open estimate

With both orientations indexed by $z$,

\[
 H_\ell=\sum_zA_ze(\ell b_z/u_0),\qquad
 B_b=\sum_{z:b_z=b}A_z,
\]

ordinary Fourier orthogonality gives

\[
 \sum_{\ell\bmod u_0}|H_\ell|^2
 =u_0\sum_{b\bmod u_0}|B_b|^2.
\]

This verifies (177.K29). Its expansion contains the complete
self-diagonal and every same-bucket off-diagonal, including pairs between
the two orientations. The rank-one weighted identity (177.K30) is also
exact:

\[
 \sum_{\ell,\ell'}c_{u_0}(\ell)\overline{c_{u_0}(\ell')}
 H_\ell\overline{H_{\ell'}}
 =\left|\sum_bE_{u_0}(b)B_b\right|^2.
\]

Thus weighted alias $TT^*$ reconstructs the physical block, while alias
Cauchy followed by Parseval returns residue-bucket energy. The
$u_0\sqrt L$ diagonal scale and the $L\sqrt q$ one-square-root ledger are
correctly described only as capacities of positive closures, not as
literal lower bounds.

For nonzero $a\bmod u_0$,

\[
 E_{u_0}(-a)=-E_{u_0}(a),
\]

but this does not pair the literal orientations. The coordinate
interchange sends the selected divisor at each endpoint to its
complementary factor. In the odd--odd branch that factor is below the
literal upper near-square divisor window; equality would force a
square product and is excluded on nontrivial squarefree support. In the
even branch the complementary factor is even and is not an allowed
character-bearing divisor. The no-pairing conclusion following
(177.K33) is therefore correct.

The first genuinely unproved mathematical step remains (177.K34), or the
stronger aliaswise estimate (177.K35), on $q>Q_B$. The literal selector
has no supplied variation, Fourier norm, factorization, or residue-bucket
correlation, and the accepted stationary audit supplies no second coupled
square-root. Nothing in the candidate or kernel claims otherwise.

## 7. Promotion and scope

After replacing (177.K26) by (R177.1), promote the durable kernel at
exactly the proposed scope:

- the primitive anchor identity and alias folding (177.K5)--(177.K6);
- the exact reduced-conductor normalization and mass
  (177.K7)--(177.K9);
- the literal $O(u_0L)$ capacity and
  $O(Lq\log(2q))$ weighted ledger;
- the low-reduced-conductor Fourier sector (177.K12), including its
  physical corollary (177.K13);
- the exact high-conductor complement (177.K14); and
- the route-scoped positive-energy and orientation-pairing limitations,
  with no literal lower-bound interpretation.

Keep (177.K34)--(177.K35), the high-conductor packet, complete K17a, the
complete residual scalar, full displayed $t=1$, all other hard-TOP
channels, hard TOP, BAL, UNBAL, M9--M2, M9--M1/GAR, endpoint uniformity,
M9, both bridges, the quarter theorem, and every exponent open.

The formalized candidate agrees with the durable kernel on every
mathematical and owner-scope claim. The appropriate terminal label remains
strict_k17a_low_cross_gcd_selector_aware_sector.

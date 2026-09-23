# Formalized Round 184 hard-M1 t=1 comparable-factor exchange sector

- Campaign: `m9-m1-hard-top-t1-comparable-factor-exchange-gate`
- Task: `conductor_formalization`
- Role: conductor-owned formal proof-kernel candidate
- Generated: `2026-08-27T21:43:07.5300757+08:00`
- Starting graph SHA-256:
  `a8e0e5d84c0c5047e0c96f11128dd215ae035bdd4355bd68ad28dc87afe6cfbd`
- Evidence status: candidate evidence only; pending independent seam
  reviews, final kernel review, and State Patch validation
- Numerical work: none

## 1. Exact literal setup

Fix real \(X\geq2\), put

\[
 y=\lfloor\sqrt X\rfloor,\qquad q_X=X/y^2,\qquad
 H=\lfloor yX^{-1/4}\rfloor,
\tag{184.C0}
\]

and fix a literal middle or lower residual hard-M1 shell \(L\), a sign
\(\sigma\in\{+1,-1\}\), and \(\kappa>0\).  Extend the complete actual
normalized symbol \(a_{L,X}^{\mathrm{lit},\sigma}(u,v)\) by zero off
every original shell, height, strict-cone, profile, floor, star,
half-weight, hard-sample, crossing, and endpoint predicate.  The complete
\(t=1\) scalar is

\[
 \mathcal T_{L,X,\sigma}
 =\sum_{\substack{(u,v)=1,\ v\ {\rm odd},\ 4u<v<16u\\
                   uv\ {\rm squarefree}}}
 \chi_4(v)a_{L,X}^{\mathrm{lit},\sigma}(u,v)
 e(\sigma\sqrt{Xuv}).
\tag{184.C1}
\]

This is exactly the \(G=\rho=t=1\) divisor-incidence face of the
Round-183 small-G complement.  The map from an incidence to \((u,v)\)
has multiplicity one.  Literal support gives \(u,v\asymp L\) and
\(uv\asymp L^2\), so boundedness and the divisor bound give only the
coefficient-insensitive envelope

\[
 |\mathcal T_{L,X,\sigma}|
 \ll_\varepsilon L^2X^\varepsilon.
\tag{184.C2}
\]

This is an upper capacity, not literal lower mass.

## 2. Canonical selector and exact exchange

For each squarefree \(N\) choose at most one unordered pair of distinct
odd prime divisors \(\{p_N,q_N\}\) satisfying

\[
 \chi_4(p_Nq_N)=-1,
 \qquad |\log(q_N/p_N)|\leq\kappa L^{-1/2}.
\tag{184.C3}
\]

The selection is any fixed canonical rule depending only on
\((N,L,\kappa)\); for example, order the eligible unordered pairs
lexicographically and choose the first.  It never depends on the
allocation \(N=uv\).  If no pair exists, select nothing.

For a selected product let \(\mathscr A_N^\oplus\) be the complete
ambient set of coprime allocations \(uv=N\), with \(v\) odd, in which
exactly one selected prime divides \(v\).  On this set define

\[
 \tau_N(u,v)=
 \begin{cases}
  (up_N/q_N,\ vq_N/p_N),&q_N\mid u,\ p_N\mid v,\\
  (uq_N/p_N,\ vp_N/q_N),&p_N\mid u,\ q_N\mid v.
 \end{cases}
\tag{184.C4}
\]

Squarefreeness and coprimality make the displayed quotients integral.
The selected bits are interchanged, so \(\tau_N^2=1\), no fixed point is
possible, and every orbit has exactly two allocations.  The map preserves
\(N\), the product phase, squarefreeness, coprimality, parity, and the
selector.  Moreover

\[
 \chi_4(v')=\chi_4(v)\frac{\chi_4(q_N)}{\chi_4(p_N)}
 =\chi_4(v)\chi_4(p_Nq_N)=-\chi_4(v).
\tag{184.C5}
\]

The physical support need not be invariant.  Zero-extend the literal
coefficient on the complete ambient XOR set.  Reindexing by \(\tau_N\)
then gives the exact identity

\[
 \mathcal T^{\rm cp}_{L,X,\sigma}
 =\frac12\sum_N\sum_{(u,v)\in\mathscr A_N^\oplus}
 \chi_4(v)e(\sigma\sqrt{XN})
 \{a_{L,X}^{\mathrm{lit},\sigma}(u,v)
   -a_{L,X}^{\mathrm{lit},\sigma}(\tau_N(u,v))\}.
\tag{184.C6}
\]

No support-preservation or eligible-pair density assertion is used.

## 3. Literal M1 exchange-direction variation

The accepted hard-M1 transform and Round-183 coefficient audit give the
following exact structural ledger for the normalized stationary symbol.
Its moving smooth factors are

\[
 \eta_L(u),\qquad
 \Phi\!\left(\frac{u}{H+1}\right),\qquad
 W\!\left(\sqrt{\frac{4q_Xu}{v}}\right),\qquad
 \left(\frac{L^2}{uv}\right)^{3/4},
\tag{184.C7}
\]

up to fixed shell normalizers and sign constants of
\(O_\varepsilon(X^\varepsilon)\).  Here \(\eta_L\) is the accepted
zero-extended scale-normalized discrete-BV profile, \(\Phi\) is uniformly
\(C^1\), and \(W\) is the fixed transformed hard profile on each smooth
cell.  The remaining literal fields are fixed at fixed \((L,X,\sigma)\)
or are the fixed finite collection of one-variable and ratio masks and
endpoint traces already present in the exact transform.  This includes
the strict \(4,16\) cone edges, \(u\leq H\), shell entries and exits,
profile support and plateau edges, floor, star, half-weight, hard-sample,
real-\(X\) crossing, and zero-extension values.

Write \(\theta_N=\log(q_N/p_N)\).  In either orientation,

\[
 (u',v')=(e^{\pm\theta_N}u,e^{\mp\theta_N}v),
 \qquad |\theta_N|\leq\kappa L^{-1/2},
\tag{184.C8}
\]

so on the fixed enlarged support box

\[
 |u'-u|+|v'-v|\ll_\kappa L^{1/2}+1.
\tag{184.C9}
\]

All coefficient-difference estimates below are restricted to the
\(\tau_N\)-closed active exchange set

\[
 \mathscr B_{L,X,\sigma,\kappa}
 :=\{(N,u,v):(u,v)\in\mathscr A_N^\oplus,\
 a(u,v)\ne0\ {\rm or}\ a(\tau_N(u,v))\ne0\}.
\tag{184.C9a}
\]

If a triple lies outside this set, both terms in (184.C6) vanish.  If it
lies inside, both orbit legs belong to a fixed
\(\kappa\)-dependent \(O(L)\)-by-\(O(L)\) enlargement of the literal
support box.  Thus restricting the estimates to
\(\mathscr B_{L,X,\sigma,\kappa}\) changes neither the exact XOR scalar
nor the complete ambient identity.

The product-only factor in (184.C7) is invariant.  On a common smooth
cell, the \(C^1\) bounds give

\[
 \left|\Phi\!\left(\frac{u'}{H+1}\right)
       -\Phi\!\left(\frac{u}{H+1}\right)\right|
 \ll_\kappa L^{-1/2},
\tag{184.C10}
\]

because nonempty shells have \(L\leq H\), while the argument of \(W\)
is multiplied by \(e^{\pm\theta_N}\), and hence its common-cell change
is also \(O_\kappa(L^{-1/2})\).  Summed over the \(O(L^2)\) ambient
ordered pairs, these smooth differences cost
\(O_{\kappa,\varepsilon}(L^{3/2}X^\varepsilon)\).

No pointwise derivative is imposed on \(\eta_L\).  Let
\(w\ll_\kappa L^{1/2}+1\).  Telescoping gives

\[
 |\eta_L(u')-\eta_L(u)|
 \leq\sum_{\min(u,u')\leq m<\max(u,u')}
 |\eta_L(m+1)-\eta_L(m)|.
\tag{184.C11}
\]

For a fixed increment \(m\), at most \(O(wL)\) pairs in the enlarged
box can cross it.  Therefore the accepted normalized BV bound gives the
weighted aggregate estimate

\[
 \sum_{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}}
 |\eta_L(u')-\eta_L(u)|
 \ll_\kappa wL
 \sum_m|\eta_L(m+1)-\eta_L(m)|
 \ll_\kappa L^{3/2}.
\tag{184.C12}
\]

Finally, a fixed ratio face \(v=\lambda u+O(1)\) can be crossed only in

\[
 |v-\lambda u|\ll_\kappa L^{1/2}+1,
\tag{184.C13}
\]

and a vertical or horizontal face has the analogous collar.  Each collar
has \(O_\kappa(L^{3/2}+L)\) integer pairs.  The exact transform has only
a fixed finite number of such faces.  Exact tie, floor, star, and
half-weight traces have \(O(L)\) sites per face.  Thus the unweighted
exceptional-site count is \(O_\kappa(L^{3/2})\), and the bounded literal
symbol gives the coefficient-weighted collar cost

\[
 \sum_{\substack{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}\\
                   (u,v),\tau_N(u,v)\ {\rm in\ different\ cells}}}
 \bigl(|a(u,v)|+|a(\tau_N(u,v))|\bigr)
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{184.C14}
\]

Equations (184.C10)--(184.C14), the discrete product rule, and arithmetic
restriction by deletion prove

\[
 \sum_{(N,u,v)\in\mathscr B_{L,X,\sigma,\kappa}}
 |a(u,v)-a(\tau_N(u,v))|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.
\tag{184.C15}
\]

Outside \(\mathscr B_{L,X,\sigma,\kappa}\) the full ambient difference
is zero.  Inserting (184.C15) into the exact signed identity (184.C6), and
taking triangle only after the character-reversing pairing, proves

\[
 \boxed{
 |\mathcal T^{\rm cp}_{L,X,\sigma}|
 \ll_{\kappa,\varepsilon}L^{3/2}X^\varepsilon.}
\tag{184.C16}
\]

The estimate is shellwise, uniform for real \(X\geq2\), and valid for
both signs and every literal endpoint convention.

## 4. Exact residual

If a pair is selected, put

\[
 \rho_N(v)=1-\mathbf1_{p_N\mid v}-\mathbf1_{q_N\mid v}
              +2\mathbf1_{p_Nq_N\mid v};
\tag{184.C17}
\]

if no pair is selected, put \(\rho_N(v)=1\).  This is one on the
neither/both patterns and zero on XOR.  Hence

\[
 \mathcal T_{L,X,\sigma}
 =\mathcal T^{\rm cp}_{L,X,\sigma}
  +\mathcal T^{\rm rem}_{L,X,\sigma},
\tag{184.C18}
\]

where

\[
 \mathcal T^{\rm rem}_{L,X,\sigma}
 =\sum_Nc_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN}),
\qquad
 c_{N,\sigma}^{\rm rem}
 =\mu^2(N)\sum_{v\mid N,\ v\ {\rm odd}}
 \chi_4(v)\rho_N(v)a_{L,X}^{\mathrm{lit},\sigma}(N/v,v).
\tag{184.C19}
\]

This residual consists exactly of every no-pair product and the
selected-pair neither/both allocations.  There is no third class.

Before physical profiling, its constant-amplitude sign mass is

\[
 \sum_{v\mid M_N}\chi_4(v)\rho_N(v)
 =\begin{cases}
   \prod_{r\mid M_N}(1+\chi_4(r)),&\text{no pair},\\
   (1+\chi_4(p_Nq_N))
   \prod_{r\mid M_N/(p_Nq_N)}(1+\chi_4(r))=0,&\text{selected pair},
  \end{cases}
\tag{184.C20}
\]

where \(M_N\) is the odd part of \(N\).  The second equality is ambient
balance only; it does not estimate the one-sided literal cone.

## 5. Exact residual connectors and mechanism limit

Ordering the retained residual odd divisors of a fixed \(N\), exact Abel
summation gives

\[
 \left|\sum_j\chi_4(v_j)a_j\right|
 \leq\frac12\operatorname{osc}(C_N)
       \sum_j|a_{j+1}-a_j|,
\tag{184.C21}
\]

where \(C_N\) is the sequence of character partial sums and the amplitude
is zero-extended at both ends.  Bounded profile variation and the divisor
bound alone yield only \(L^2X^\varepsilon\) after a positive product sum;
the required weighted average of \(\operatorname{osc}(C_N)\) is open.

Extend \(c_{N,\sigma}^{\rm rem}\) by zero outside a containing interval
of \(M_L\asymp L^2\) product sites, set
\(z_N=c_{N,\sigma}^{\rm rem}e(\sigma\sqrt{XN})\), and define

\[
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={1\over R}\sum_{s\in\mathbb Z}
 \left|\sum_{j=0}^{R-1}z_{s+j}\right|^2.
\tag{184.C22}
\]

Exact expansion gives

\[
\begin{aligned}
 \mathfrak E_{R,\sigma}^{\rm rem}
 ={}&\sum_N|c_{N,\sigma}^{\rm rem}|^2\\
 &+2\Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right),
\end{aligned}
\tag{184.C23}
\]

with no endpoint error, and

\[
 |\mathcal T^{\rm rem}_{L,X,\sigma}|^2
 \leq\frac{M_L+R-1}{R}\mathfrak E_{R,\sigma}^{\rm rem}.
\tag{184.C24}
\]

The diagonal is \(O_\varepsilon(L^2X^\varepsilon)\).  At
\(R=\lceil L\rceil\), the sufficient actual-direction statement is

\[
 \Re\sum_{1\leq r<R}\left(1-\frac rR\right)
 \sum_Nc_{N+r,\sigma}^{\rm rem}\overline{c_{N,\sigma}^{\rm rem}}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N+r}+\sqrt N}\right)
 \ll_\varepsilon L^2X^\varepsilon.
\tag{184.C25}
\]

There is one outer real part.  Equation (184.C25) is unproved.  A modulus
per shift gives \(\mathfrak E_R\ll L^3X^\varepsilon\) and hence only the
\(L^2X^\varepsilon\) scalar capacity.

A one-prime toggle multiplies \(v/u\in(4,16)\) by \(p^{\pm2}\) and has
disjoint physical supports.  Normalized averaging of full involutions is
an exact rewriting.  All-\(1\pmod4\) products have no eligible pair and
no character reversal.  A supported semiprime's two factor legs differ
by a ratio greater than four, so its only two primes cannot meet
(184.C3) once \(\kappa L^{-1/2}<\log4\).  These controls prove that the
local exchange mechanism alone does not cover the residual; they do not
disprove the literal complete \(t=1\) estimate.

## 6. Scope and state recommendation

The only positive candidate theorem is (184.C16), a strict, possibly
empty, incidence sector.  Equations (184.C17)--(184.C25) give its exact
residual and the first missing signed relation.  A State Patch may create
one subordinate `proved_internal` sector node only after all seam reviews
and final validation are GREEN.

Keep the complete \(t=1\) face, all \(t\geq2\) small-G incidences, the
large-G near-resonant complement, the complete hard small-\(t\) owner,
both direct M1 parents, every M2 owner, endpoint uniformity, M9, both
bridges, the Gauss-circle target, and all exponent claims unchanged.

## 7. Exact dependencies and evidence

Direct accepted dependencies:

- `M9-M1-hard-top-squarefree-radical-sector-reduction`;
- `M9-M1-hard-top-small-t-nonresonant-primitive-ray-sector`;
- `M9-M1-top-endpoint-transform`;
- `M9-M1-frequency-phase-diagram-R10`;
- `H4-Phi-regularity`;
- `M9-M2-dyadic-weight-nondegeneracy`; and
- `Divisor-bound-elementary`.

Round evidence reconciled:

- `reports/literal_t1_exchange_residual_attack.md`;
- `reports/m2_transfer_transport_capacity_audit.md`;
- `reports/blind_complete_t1_exchange_rederivation.md`; and
- `reviews/conductor_round184_report_reconciliation.md`.

The explicit M1 factorization is reproduced from the already accepted
hard-M1 transform evidence, not inferred from the M2 kernel.  The M2
exchange and residual kernels are method controls only.  No external
theorem or numerical experiment is used.

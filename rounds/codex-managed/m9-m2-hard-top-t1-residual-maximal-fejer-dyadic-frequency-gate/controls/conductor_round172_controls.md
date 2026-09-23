# Conductor controls for Round 172

- Campaign: `m9-m2-hard-top-t1-residual-maximal-fejer-dyadic-frequency-gate`
- Round: 172
- Starting graph:
  `c98f95b6b3500d0f48365af338e543f9a0f251b22062f3898df5f448d6b54853`
- Allocation: 100% analytic/algebraic; 0% numerical
- Proposed terminal: `maximal_fejer_dyadic_character_poisson_no_go`

## Exact finite algebra reproduced by the conductor

Let

\[
 C_r=\sum_N z_{N+r}\overline{z_N},\qquad
 A_r=\Re C_r,\qquad D_L=C_0,
\]

with the literal residual sequence extended by zero on an \(M\)-site
containing interval.  Direct Fourier expansion gives

\[
 \mathfrak E_R^{(2)}
 =D_L+2\!\sum_{\substack{0<r<R\\2\mid r}}
 \left(1-\frac rR\right)A_r.
\tag{172.C1}
\]

Both absolute site parities are retained.  Along
\(R_{j+1}=\min(2R_j,M)\), with repetitions removed,

\[
 T_{26}=\frac12\sum_j
 \left(\mathfrak E_{R_{j+1}}^{(2)}-
       \mathfrak E_{R_j}^{(2)}\right)-B_{\rm short},
\]

\[
 B_{\rm short}=\sum_{\substack{0<r<R_0\\2\mid r}}
 r\left(\frac1{R_0}-\frac1M\right)A_r,
 \qquad |B_{\rm short}|\le R_0D_L
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.C2}
\]

For every integer \(R<S\le2R\), direct subtraction gives

\[
 b_{R,S}(r)=
 \begin{cases}
 r(S-R)/(RS),&0<r<R,\\
 1-r/S,&R\le r<S,\\
 0,&r\ge S,
 \end{cases}
 \qquad b_{R,S}(0)=0.
\tag{172.C3}
\]

At \(S=2R\), this is the triangular tent and the parallelogram identity
gives the exact absolute-site-parity Haar formula.  A strict terminal
\(R<S<2R\) link uses (172.C3), not a rounded Haar formula.  For
\(S=\min(2R_0,M)\), positivity or direct summation of (172.C3) gives

\[
 |\mathfrak E_S^{(2)}-\mathfrak E_{R_0}^{(2)}|
 \le (S-R_0)D_L\ll_\varepsilon L^3X^\varepsilon.
\tag{172.C4}
\]

This is a local first-link bound.  Its complement is not target-safe, so
it is not an owner-complete sector.

## Exact common-frequency transform

Choose a real cardinal bump
\(\varphi\in C_c^\infty((-1/2,1/2))\), \(\varphi(0)=1\), and put

\[
 \mathcal W_\epsilon(x,y)=
 \sum_{\substack{d,m\ge1\\d\ {\rm odd}}}
 (-1)^{\epsilon m}\lambda_{dm}(d)
 \varphi(x-d)\varphi(y-m),
\]

\[
 \mathcal B_{\epsilon,\theta}(x,y)=
 \mathcal W_\epsilon(x,y)e(J\sqrt{xy}+\theta xy).
\]

The cells are disjoint at the lattice points, so every selector, arithmetic
hole, parity branch, endpoint value, and zero-extension value is retained
with multiplicity one.  With
\(\widetilde{\mathcal B}(\xi,\nu)=\iint\mathcal B(x,y)
e(-\xi x-\nu y)\,dx\,dy\), character Poisson in \(d\) and ordinary
Poisson in \(m\) give exactly

\[
 Z_\epsilon(\theta)=\frac i2
 \sum_{\substack{k\in\mathbb Z\\k\ {\rm odd}}}\chi_4(k)
 \sum_{\ell\in\mathbb Z}
 \widetilde{\mathcal B}_{\epsilon,\theta}(k/4,\ell).
\tag{172.C5}
\]

The factor \(i/2\) follows from

\[
 \chi_4(n)=\frac{e(n/4)-e(-n/4)}{2i}.
\]

After squaring and applying the two-peak parity average, the exact
bandpass coefficient is \(1/8\), with one real part outside the complete
\(k,k',\ell,\ell'\) aggregate.  No transformed mode, cell, or arithmetic
opening has yet been replaced by a modulus.

## Zero mode, diagonals, and boundary control

After summing all signed odd character frequencies first, the ordinary
zero component is

\[
 Z_{\epsilon,0}(\theta)=
 \sum_d\chi_4(d)\int_{\mathbb R}
 \mathcal B_{\epsilon,\theta}(d,y)\,dy.
\tag{172.C6}
\]

On every positive cell,

\[
 \partial_y(J\sqrt{dy}+\theta dy)
 =\frac J2\sqrt{d/y}+\theta d\asymp J
 \qquad(0\le\theta\le1),
\]

because \(d,y\asymp L\) and \(L^2\le J\).  Cellwise integration by parts,
followed by the \(O(L^2X^\eta)\) literal-incidence count, yields

\[
 \sup_{\epsilon,\theta}|Z_{\epsilon,0}(\theta)|
 \ll_\eta L^2J^{-1}X^\eta.
\tag{172.C7}
\]

Hence all terms with \(\ell=0\) or \(\ell'=0\), after that complete
\(k,k'\) recombination, are

\[
 \ll (R+S)
 \left(D_L^{1/2}\frac{L^2}{J}+\frac{L^4}{J^2}\right)X^{O(\eta)}
 \ll_\varepsilon L^3X^\varepsilon.
\tag{172.C8}
\]

This is not a termwise estimate in \(k\), and it is not the distinct
Round-169 scalar zero mode.

For \(B_{R,S}=F_S-F_R\), the continuous product-difference kernel is

\[
 \mathscr B_{R,S}(t)=\int_0^1B_{R,S}(\theta)e(t\theta)\,d\theta
 =\sum_h b_{R,S}(h)\int_0^1e((t+h)\theta)\,d\theta.
\tag{172.C9}
\]

It equals \(b_{R,S}(n)\) at an integer argument \(n\), but for noninteger
\(t\)

\[
 \mathscr B_{R,S}(t)=
 \frac{(e(t)-1)(S-R)}{2\pi it}
 -\frac1{2\pi it}\int_0^1B'_{R,S}(\theta)e(t\theta)\,d\theta.
\tag{172.C10}
\]

Thus the zero physical diagonal does not delete a fixed dual diagonal:
the two cardinal variables in the squared transform remain independent.
Physical diagonal cancellation emerges only after dual diagonal,
off-diagonal, endpoint-cell, frequency-endpoint, and zero-extension pieces
recombine.

## Restored power and false controls

Fejer positivity gives

\[
 |\mathfrak E_S^{(2)}-\mathfrak E_R^{(2)}|
 \le (R+S)D_L.
\tag{172.C11}
\]

At a maximal link this has capacity \(L^4X^\varepsilon\), one factor
\(L\) above the target.  The capacity is sharp for the coefficient-uniform
interface.  Let \(M=4P\), take \(z_N=1\) on the \(2P\) even sites of an
\(M\)-site interval, and use the legitimate link \(2P\to4P\).  Then
\(D_L=2P\), \(A_{2s}=2P-s\), and direct summation of the tent gives

\[
 \mathfrak E_{4P}^{(2)}-\mathfrak E_{2P}^{(2)}=P^2
 =\frac18MD_L.
\tag{172.C12}
\]

A positive translate makes every square root lawful; choosing the
diagnostic coefficient \(c_N=e(-J\sqrt N)\) dechirps the phase.  Along an
admissible power-of-two subfamily the link occurs in the stopped chain and
\(M\asymp L^2\), so (172.C12) falsifies any uniform \(L^3X^\varepsilon\)
claim derived only from support, \(D_L\), Parseval, Haar positivity, or a
positive dual/cell norm.  It is not the literal residual coefficient and
is not a physical lower bound.  A one-site sequence has every increment
exactly zero, so an isolated positive transformed diagonal is also
inadmissible.

At either Fejer peak, after the exact parity gauge is moved into the
amplitude, the smooth product phase is

\[
 \Phi_\phi(u,v)=J\sqrt{uv}+\phi uv-\xi u-\eta v,
 \qquad
 \det\operatorname{Hess}\Phi_\phi
 =-\phi^2-\frac{J\phi}{2\sqrt{uv}}.
\tag{172.C13}
\]

It is rank one at both centred peaks.  Positive simultaneous dualization
therefore returns to the accepted product-collar capacity; it supplies no
generic factor-\(L\) mechanism.

## Control matrix

| control | conductor outcome |
|---|---|
| even parity projection and one real part | GREEN |
| stopped integer chain and one short correction | GREEN |
| exact tent, zero diagonal, and final non-doubling link | GREEN |
| absolute-site-parity Haar identity | GREEN at exact doublings only |
| first-link power and endpoint coverage | GREEN locally; no owner-complete complement |
| literal cardinal interpolation and multiplicity | GREEN |
| character/ordinary Poisson constants | GREEN: \(i/2\) and \(1/8\) |
| ordinary-zero sector | GREEN only after full signed character-frequency recombination |
| physical versus dual diagonal | GREEN as distinct objects |
| endpoints, transitions, holes, and both parity branches | RETAINED |
| dechirped maximal-link control | GREEN as a coefficient-uniform falsifier |
| one-site and no-pair controls | GREEN as route diagnostics |
| both Fejer peaks and collar restoration | GREEN |
| signed nonzero ordinary-frequency aggregate | OPEN |
| factor \(L\) before positive norm | FAILS FOR THE AUDITED ROUTE |
| residual owner and downstream transfer | QUARANTINED |

## Conductor conclusion

The finite reduction, exact common-frequency transform, and collectively
recombined ordinary-zero estimate are stable.  The first unproved analytic
object is the complete signed \(\ell,\ell'\ne0\) contribution to the
stopped-chain aggregate; a linkwise \(L^3X^\varepsilon\) theorem would be
sufficient but is stronger than necessary because cross-link cancellation
has not been excluded.

The smallest durable result is a route-scoped obstruction to replacing
that signed actual-symbol aggregate by coefficient-uniform positive norms
before gaining the missing factor \(L\).  It does not prove or disprove
(165.K26), close a hard-TOP owner, or change a theorem or exponent.

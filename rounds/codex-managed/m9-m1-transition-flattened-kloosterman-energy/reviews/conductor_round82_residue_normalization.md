# Round 82 residue-normalization review

Campaign: `m9-m1-transition-flattened-kloosterman-energy`

Round: 82

Starting graph SHA-256:
`01333baabd40e4b9fb94aa16495fefdc5ec54e86fb56c43cada928ff55a9b835`

## Decision

The exact original-row residue decomposition is valid for every local
class and alias, and it strictly narrows the first upper-conductor
survivor. It proves no new conductor interval.

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad B=C/T.
\]

For a fixed nonaxial component and local class, the transition-flattened
principal row has the exact form

\[
 S_b=\sum_{r\in\mathscr R_{\kappa,b}}u_{\kappa,b,k}(r)R_{\kappa,b,k}(r),
 \tag{82.N1}
\]

where the exact odd or even local unit is constant on the admissible
progression \(c=r\pmod{4b}\), and

\[
 R_{\kappa,b,k}(r)=
 \sum_{\substack{c\asymp C\\c\equiv r\ (4b)}}
 V_{b,c,k}^{(\kappa)}e\!\left(\pm{A_{\kappa,b}\over c}\right).
 \tag{82.N2}
\]

The accepted global BV bound and Bourgain's audited proper-subinterval
estimate give

\[
 |R_{\kappa,b,k}(r)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.       \tag{82.N3}
\]

Consequently the complete same-residue energy and every one fixed
nonzero residue-offset layer are

\[
 \ll_\varepsilon X^\varepsilon
 B^2T^2Q^{-5/12}
 =X^\varepsilon C^2Q^{-5/12}.                    \tag{82.N4}
\]

They are target-safe for \(C\le J^{47/60}\), in particular throughout
\(J^{13/18}<C\le J^{3/4}\). The only remaining smooth-main object in
that band is the coherent sum of all nonzero offsets

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp B}\sum_{\substack{r,s\in\mathscr R_{\kappa,b}\\r\ne s}}
 u(r)\overline{u(s)}R(r)\overline{R(s)}.          \tag{82.N5}
\]

## Arithmetic check

There are \(O(B)\) moduli \(b\), \(O(B)\) admissible residues per
modulus, and at most one partner \(s=r+t\) for each residue when the
offset \(t\ne0\pmod{4b}\) is fixed. Thus (82.N4) has exactly two, not
three, factors of \(B\). Summing the \(O(B)\) offset layers absolutely
recovers

\[
 |\mathfrak X_C^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon{C^3\over TQ^{5/12}}.
 \tag{82.N6}
\]

Since the target is \(J^2/T=J^{7/5}\), the ratio in (82.N6) is one at
\(C=J^{13/18}\) and \(J^{1/12}\) at \(C=J^{3/4}\). A gain
\(B^{-\delta}\) reaches

\[
 C\le J^{c_\delta},\qquad
 c_\delta={13/6-3\delta/5\over3-\delta}.          \tag{82.N7}
\]

Thus \(B^{-1/2}\) reaches \(J^{56/75}\), while \(B^{-5/9}\) closes the
whole first residual band. These are conditional range maps, not
proved estimates.

## Odd product transform and self-return

For the odd class, with \(q=4b\), define

\[
 \mathcal C_q(d,t)={1\over q}\sum_{r\bmod q}
 S(r+d,k;q)\overline{S(r,k;q)}e_q(-tr).
\]

Finite orthogonality gives

\[
 \mathcal C_q(d,t)=
 \sum_{\substack{y\bmod q\\(y(y+t),q)=1}}
 e_q\!\left(d(y+t)+k(\overline{y+t}-\bar y)\right),
 \qquad \mathcal C_q(d,0)=c_q(d).                 \tag{82.N8}
\]

The zero product-frequency is precisely the safe same-residue mode;
the nonzero product-frequencies are precisely (82.N5). Complete
Poisson inversion, with all stationary lower terms, supports, and tails
retained, returns exactly to (82.N1). It supplies no analytic gain.

## Source normalization correction

The Round-82 packet's single Voronoi center \(X/4\) is not universal for
the level-four spectrum. After newform/oldform and cusp bookkeeping,
the Assing--Corbett denominator is

\[
 L_f=[1,M_f,N_f],
\]

and the raw centers form a finite family

\[
 m=L_fX/4+O(T),
\]

including \(X/4\), \(X/2\), and \(X\) before finite oldform dilation.
Every center has the same \(T\)-window and the same \(J^{1/10}=X^{1/20}\)
short-coefficient deficit. This correction changes no accepted range.

## Scope

The residue reduction is performed in the exact original smooth row, so
it does not require the two even spectral transforms or any truncated
stationary expansion. The transition error and axes retain their
separate accepted owners. No estimate is proved for (82.N5), for the
upper band \(C>J^{3/4}\), cone edges, other radial sectors, full
`M9-M1`, `M9-M2`, `M9`, or the global exponent.

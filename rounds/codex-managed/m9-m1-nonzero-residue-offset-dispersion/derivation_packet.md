# Round 83 derivation packet: coherent nonzero residue-offset dispersion

## 1. Accepted starting point

Put

\[
 J=X^{1/2},\qquad Q=J^{2/5},\qquad T=J^{3/5},\qquad
 B=C/T,
\]

and assume

\[
 J^{13/18}<C\le J^{3/4}.                         \tag{83.1}
\]

For each fixed smooth-interior nonaxial M1 component, local class
\(\kappa\in\{1/4,1/2,1\}\), alias, orientation, and compatible fixed
nonzero \(k=\rho\sigma=O(1)\), Round 82 proves the exact original-row split

\[
 S_b=\sum_{r\in\mathscr R_{\kappa,b}}u_{\kappa,b,k}(r)
 R_{\kappa,b,k}(r),\qquad b\asymp B,              \tag{83.2}
\]

\[
 R_{\kappa,b,k}(r)=
 \sum_{\substack{c\asymp C\\c\equiv r\pmod{4b}}}
 V_{b,c,k}^{(\kappa)}
 e\!\left(\pm{A_{\kappa,b}\over c}\right),     \tag{83.3}
\]

Here

\[
 A_{\kappa,b}=\left(\sqrt{bX}+\sqrt{\kappa k/b}\right)^2
 \asymp bX,
 \qquad
 \|V\|_\infty+\operatorname {Var}_{[C,2C]}V
 \ll_\varepsilon X^\varepsilon.                 \tag{83.3a}
\]

where the exact odd or even local unit is constant on the progression,
the admissible residue set retains every parity and gcd condition, and

\[
 |R_{\kappa,b,k}(r)|
 \ll_\varepsilon X^\varepsilon TQ^{-5/24}.       \tag{83.4}
\]

The pointwise transition remainder and both axes are separately accepted
and excluded from this packet.  No stationary truncation is made in
(83.2)--(83.3).

## 2. Exact survivor and target

The complete same-residue energy and every fixed nonzero residue-offset
layer are already target-safe.  The only surviving principal energy is

\[
 \mathfrak X_C^{(\kappa,k)}=
 \sum_{b\asymp B}\sum_{\substack{r,s\in\mathscr R_{\kappa,b}\\r\ne s}}
 u(r)\overline{u(s)}R(r)\overline{R(s)}.          \tag{83.5}
\]

Equivalently, with \(q=4b\) and residue offset
\(a=s-r\not\equiv0\pmod q\),

\[
 \mathfrak X_C^{(\kappa,k)}
 =\sum_{b\asymp B}\sum_{a\ne0\ (q)}\mathfrak X_{b,a},
\]

\[
 \mathfrak X_{b,a}=
 \sum_{\substack{r\in\mathscr R_{\kappa,b}\\r+a\in\mathscr R_{\kappa,b}}}
 u(r)\overline{u(r+a)}R(r)\overline{R(r+a)}.      \tag{83.6}
\]

Every one fixed \(a\) obeys

\[
 |\mathfrak X_{b,a}|\hbox{ summed over }b
 \ll_\varepsilon X^\varepsilon C^2Q^{-5/12},    \tag{83.7}
\]

but absolute summation over the \(O(B)\) offsets gives only

\[
 |\mathfrak X_C^{(\kappa,k)}|
 \ll_\varepsilon X^\varepsilon{C^3\over TQ^{5/12}}.
 \tag{83.8}
\]

The frozen target is

\[
 \boxed{\mathfrak X_C^{(\kappa,k)}
 \ll_\varepsilon X^\varepsilon{J^2\over T}.}     \tag{83.9}
\]

A proved gain \(B^{-\delta}\) over (83.8) reaches

\[
 C\le J^{c_\delta},\qquad
 c_\delta={13/6-3\delta/5\over3-\delta}.          \tag{83.10}
\]

Thus any fixed \(\delta>0\) is a nonempty range extension,
\(\delta=1/2\) reaches \(J^{56/75}\), and \(\delta=5/9\) closes (83.1).

## 3. Exact odd inverse-unit form

For \(\kappa=1/4\),

\[
 u(r)=u_{b,k}e_q(k\bar r),\qquad (r,q)=1,
\]

so the offset unit is exactly

\[
 u(r)\overline{u(r+a)}
 =e_q\!\left(k(\bar r-\overline{r+a})\right)
 =e_q\!\left(ka\,\overline{r(r+a)}\right).       \tag{83.11}
\]

Opening (83.3), the odd offset layer is

\[
 \sum_{r}^{*}e_q\!\left(ka\,\overline{r(r+a)}\right)
 \sum_{\ell_1,\ell_2}
 V(r+q\ell_1)\overline{V(r+a+q\ell_2)}
 e\!\left(\pm A_b
 \left({1\over r+q\ell_1}-{1\over r+a+q\ell_2}\right)\right),
 \tag{83.12}
\]

with exact dyadic support and one-count endpoints.  This rational
inverse-unit phase is the arithmetic structure that a new proof must
use.  It may not be replaced by an arbitrary bounded sequence.

The two even classes have their own exact progression units.  A proof in
the odd class alone is not an all-class range extension unless the even
units are derived and bounded separately.

## 4. Product-Kloosterman representation and forbidden return

For the odd class define

\[
 \mathcal C_q(d,t)={1\over q}\sum_{n\bmod q}
 S(n+d,k;q)\overline{S(n,k;q)}e_q(-tn).
\]

Finite orthogonality gives

\[
 \mathcal C_q(d,t)=
 \sum_{\substack{y\bmod q\\(y(y+t),q)=1}}
 e_q\!\left(d(y+t)+k(\overline{y+t}-\bar y)\right),
 \qquad \mathcal C_q(d,0)=c_q(d).                \tag{83.13}
\]

The zero product-frequency is exactly the already removed same-residue
mode.  The nonzero frequencies are exactly (83.5).  Complete Poisson
inversion, with all lower stationary terms, supports, and tails retained,
returns (83.13) to (83.11)--(83.12).  Neither direction is a saving by
itself.

An ordinary coefficient-blind Kloosterman large sieve has capacity

\[
 BQ^2T=B{J^2\over T},                            \tag{83.14}
\]

and loses exactly \(B\).  Current fixed-modulus bilinear theorems do not
automatically estimate the varying-modulus product kernel with its joint
actual symbol.

## 5. Frozen completion rule

Round 83 succeeds if it does one of the following.

1. Proves (83.9) for every local class and alias on all of (83.1).
2. Proves (83.8) with any fixed gain \(B^{-\delta}\), uniformly for all
   classes and transformed errors needed for the implication, and states
   the exact new endpoint (83.10).
3. Proves a rigorous actual-symbol no-go and reduces (83.5) to a strictly
   smaller named signed correlation after removing additional
   target-safe modes exactly once.

No result may promote \(C>J^{3/4}\), transition errors or axes outside
their accepted interval, cone edges, other radial sectors, full
`M9-M1`, `M9`, or the Gauss-circle exponent.

## 6. Required controls

- exact target and factor-\(B\) ledger;
- fixed nonzero nonaxial \(k\), the exact \(A_{\kappa,b}\), and the
  global symbol BV bound;
- residue-offset one-count and the removal of \(a=0\) exactly once;
- odd inverse-unit identity (83.11);
- both even local units and aliases;
- dependence of \(R(r)\) on the offset and reciprocal phase;
- rational complete sums, gcds, exceptional residues, and zero modes;
- small, large, and wraparound offsets;
- perfect-square, fourth-power, and phase-conjugating controls;
- complete transforms versus involutive self-return;
- current primary-source hypotheses at the literal modulus and lengths;
- transition/axis ownership and downstream scope.

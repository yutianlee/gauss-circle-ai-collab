# Blind review of the fixed-wrap lemma

## 1. Result

The fixed-wrap estimate remains valid for the actual full range
$1\leq L_i\ll E$. The frozen row gives

$$
q_i\asymp L_iQ,\qquad r_i=\frac{q_i}{h}\asymp\frac{L_iQ}{h},
\tag{1.1}
$$

not $r_i\asymp Q/h$ unless $L_i\asymp1$. With (1.1), every fixed
integer wrap $k$ contributes

$$
\mathcal C_d(k)\ll_\varepsilon QX^\varepsilon
\tag{1.2}
$$

to the coefficient-weighted absolute collar mass of one row. Therefore
any specified packet of

$$
J\ll1+\frac{R^2}{Q}\asymp1+\frac{\sqrt M}{D}
$$

wraps contributes

$$
\ll_\varepsilon JQD X^\varepsilon
\ll_\varepsilon R^2D X^\varepsilon
\tag{1.3}
$$

after the $O(D)$ rows. This is a packet lemma only; it does not prove
that the complete collar has only $J$ wrap classes.

## 2. Exact statement and hypotheses

Fix $d\asymp D$. Sum over

$$
1\leq L_i\ll E,\quad q_i\asymp L_iQ,\quad
q_i=hr_i,\quad (r_1,r_2)=1,
$$

and put

$$
\delta=L_1r_2-L_2r_1,\qquad
\rho=N\delta-khr_1r_2.
$$

Retain $0<|\rho|\leq hr_1r_2/D$. Assume the sampled profile values are
uniformly $O(1)$ and use, for $L=acs^2$ with $a\mid d_{\mathrm o}$,

$$
|B_{d,U}(L)|\ll_\varepsilon \frac{X^\varepsilon}{c}.
\tag{2.1}
$$

Then the sum, for fixed $k$, of

$$
\frac{|B_{d,U}(L_1)B_{d,U}(L_2)|}{L_1L_2}
|\mathscr W_{d,U}(L_1/q_1)|
|\mathscr W_{d,U}(L_2/q_2)|
$$

over all $h,L_i,r_i$ above is bounded by (1.2). Oddness, characters,
coprimality, squarefree-row restrictions, centering, and exact-pair
exclusion can be retained; dropping them only enlarges this absolute
upper bound.

## 3. Proof or derivation

Set

$$
S=NL_1-khr_1,\qquad A=NL_2r_1,\qquad b=\frac{hr_1}{D}.
$$

The collar inequality, enlarged harmlessly to include $\rho=0$, gives

$$
|Sr_2-A|\leq br_2.
\tag{3.1}
$$

If a supported solution exists, (1.1) implies

$$
\frac{A}{r_2}=NL_2\frac{r_1}{r_2}\asymp NL_1,
\qquad
\frac{b}{NL_1}\ll\frac{Q}{ND}
=\frac{2}{\sqrt{NDE}}\ll R^{-2}.
$$

Hence $S\asymp NL_1$ and $S>b>0$. All supported $r_2$ lie in

$$
\frac{A}{S+b}\leq r_2\leq\frac{A}{S-b}.
$$

This interval has length

$$
\frac{2Ab}{S^2-b^2}
\ll\frac{hL_2r_1^2}{DNL_1^2}
\ll\frac{L_2Q^2}{DN h}
=\frac{4L_2}{Eh}
\ll\frac1h,
\tag{3.2}
$$

because $L_2\ll E$. Thus each $r_1$ permits $O(1)$ values of $r_2$.
Reversing the roles, with $T=NL_2+khr_2$, gives an interval for $r_1$
of length $\ll4L_1/(Eh)\ll1/h$. Consequently

$$
\#\mathcal T_{h,k}(L_1,L_2)
\ll\frac{Q\min(L_1,L_2)}{h}.
\tag{3.3}
$$

This proof covers both signs of $k$ and $k=0$; it never divides by $k$.
Existence of a supported solution proves the needed signs of $S$ and
$T$. Exact-pair exclusion only decreases the count. For $D=1$, the
relative error is $O(Q/N)=O(R^{-2})$, so there is no endpoint loss.

The full half-weight norm also holds. From (2.1), for sufficiently small
$\eta>0$,

$$
\begin{aligned}
\sum_{L\ll E}\frac{|B_{d,U}(L)|}{\sqrt L}
&\ll_\eta X^\eta
\sum_{a\mid d_{\mathrm o}}a^{-1/2}
\sum_{c\ll E/a}c^{-3/2}
\sum_{s\ll\sqrt{E/(ac)}}s^{-1}\\
&\ll_\eta X^\eta\tau(d_{\mathrm o})\log(2E)
\ll_\varepsilon X^\varepsilon.
\end{aligned}
\tag{3.4}
$$

The $c$-sum converges; the global square-variable sum costs only
$\log E$; divisor and logarithmic losses are absorbed by relabelling
$\varepsilon$. Using

$$
\frac{\min(L_1,L_2)}{L_1L_2}
\leq\frac1{\sqrt{L_1L_2}},
$$

(3.3) and (3.4) give, at fixed $h,k$,

$$
\mathcal C_{d,h}(k)
\ll_\varepsilon\frac QhX^\varepsilon.
$$

Since $h\ll EQ\ll X$, summing $h^{-1}$ proves (1.2).

Finally,

$$
JQ\ll Q+R^2\ll R^2,
$$

because $D\leq\sqrt M$ and $DE\asymp M$ imply $D\ll E$ and hence
$Q=2\sqrt{ND/E}\ll R^2$. Also

$$
\frac{R^2}{Q}
=\frac12\sqrt{\frac XN}\sqrt{\frac ED}
\asymp\frac{\sqrt M}{D}.
$$

Multiplying by the $O(D)$ rows proves (1.3).

## 4. First doubtful or unproved step

There is no remaining gap in the fixed-wrap estimate after replacing
the former dyadic-shell norm by the global norm (3.4). The first
unsupported step would be to assert that the entire centered collar
uses only $O(1+R^2/Q)$ wrap integers. The interval proof controls one
fixed wrap but does not count all wraps present. The supplied $D=1$
no-go remains compatible with this lemma because its full-collar mass
may occupy many wrap classes.

## 5. Required controls and outcomes

| Control | Outcome |
|---|---|
| Actual support | Passed after correction: $r_i\asymp L_iQ/h$. |
| All $1\leq L_i\ll E$ | Passed: (3.2) is $\ll4L_i/(Eh)\ll1/h$, and (3.4) is global. |
| Sign and zero factors | Passed: supported solutions force $S\asymp NL_1$ and $T\asymp NL_2$. |
| Both signs and $k=0$ | Passed: no division by $k$ occurs. |
| $D=1$ | Passed for each fixed wrap; it does not bound the number of wraps. |
| Exact-pair exclusion | Passed: exclusion decreases the absolute sum. |
| $h$-summation | Passed: (3.3) supplies $1/h$, costing only $\log X$. |
| Global $L$-weights | Passed by the half-weight norm (3.4). |
| Profiles and prefix factors | Passed for this absolute bound using only their stated pointwise bounds. |
| Packet versus full collar | Not established globally; packet cardinality is a separate hypothesis. |

## 6. Dependencies and exact artifacts used

Only these supplied artifacts were inspected:

1. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/blind_statement.md
2. rounds/codex-managed/m9-m1-lower-cone-t1-squarefree-moving-coefficient-near-collision-gate/reports/blind_nonexact_correlation_feasibility.md

The proposed lemma and the conductor's correction that all
$1\leq L_i\ll E$ are summed were the only additional inputs. No
discovery report, shared proof state, web source, or computation was
used.

## 7. Recommended state effect

Promote the result as a conditional global-in-$L$ fixed-wrap packet
lemma, with actual support $r_i\asymp L_iQ/h$, range
$1\leq L_i\ll E$, uniform sampled-profile boundedness, and an explicitly
selected set of at most $J\ll1+R^2/Q$ wrap integers.

Do not promote it as a complete-collar bound. A separate argument must
establish the required wrap cardinality or control all remaining wraps.

## Final verdict

**GREEN** - the fixed-wrap $O(QX^\varepsilon)$ row bound survives the
full $L_i\ll E$ summation; the packet-to-full-collar step remains open.

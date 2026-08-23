# Blind literal-energy rederivation

## 1. Result: exact connector lemma and a broad-part no-go

Let

\[
b(h,k)=\eta(\gcd(h,k)/G_0)A(h,k),\qquad
a(h,k)=\chi _4(h)b(h,k).
\]

For the supplied fixed block, the smallest lawful squared object is the
scalar energy \(|T_{\rm low}|^2\).  Its true phase diagonal is

\[
g^2uv=g'^2u'v',
\quad\text{equivalently}\quad hk=h'k',
\]

not \(uv=u'v'\).  This full-product diagonal is
\(O_\varepsilon(LKX^\varepsilon)=O_\varepsilon(L^2X^\varepsilon)\),
and hence is one power of \(L\) below the allowed energy \(L^3\).

There are three exact but logically different interfaces:

1. grouping the scalar energy by \(r=hk-h'k'\) is an exact
   shifted-product decomposition;
2. either row or column mean square implies the scalar target after a
   Cauchy cost, but is a stronger, diagonal-critical assertion;
3. \(\rho=hk'-h'k=hq-kp\) is an exact transverse ray defect, with an
   exact rank-one tangent remainder.

The natural curvature-narrow band \(|\rho|\ll1\) at
\(L\asymp R^{1/3}\), and in fact every band \(|\rho|\le Q\) with
\(Q\le L\), has adequate absolute capacity.  The curvature-narrow band
has absolute mass \(O(L^2\log L)\), a strict saving relative to \(L^3\).
Nothing in the supplied identities bounds the complementary broad part.
Both proposed mean squares are false for arbitrary coefficients of the
same magnitude, while their actual-symbol versions remain unproved.
Thus the exact connectors and the narrow count are valid progress, but
they do not prove the fixed-block target.

## 2. Exact statement and hypotheses

Assume all hypotheses in the statement-only packet.  In particular,
\(h\asymp L\), \(k\asymp K\), \(1\le K/L\le16\),
\(G_0=\sqrt L/2\), and the support of \(\eta\) implies
\(d:=\gcd(h,k)\ll\sqrt L\).  All constants below may depend on the fixed
support intervals and on the uniform symbol bounds.

The following assertions hold.

**(a) Literal scalar energy.**  With

\[
c(g,u,v)=\eta(g/G_0)\chi _4(g)\chi _4(u)A(gu,gv),
\]

one has

\[
\begin{aligned}
|T_{\rm low}(R)|^2
=\sum_{\substack{g,u,v\ge1\\(u,v)=1}}
 \sum_{\substack{g',u',v'\ge1\\(u',v')=1}}
&c(g,u,v)\overline{c(g',u',v')}\\
&\times e\!\left(R\bigl(g\sqrt{uv}-g'\sqrt{u'v'}\bigr)\right).
\tag{114.1}
\end{aligned}
\]

Both lift variables \(g,g'\) are indispensable.  In physical
coordinates this is

\[
|T_{\rm low}(R)|^2
=\sum_{h,k,h',k'}a(h,k)\overline{a(h',k')}
e\!\left(R(\sqrt{hk}-\sqrt{h'k'})\right).
\tag{114.2}
\]

The phase diagonal is the full equality
\(g^2uv=g'^2u'v'\), or \(hk=h'k'\).

**(b) Exact shifted-product grouping and its diagonal.**  If
\(r=hk-h'k'\), then

\[
|T_{\rm low}(R)|^2=\sum_{r\in\mathbb Z} C_r,
\tag{114.3}
\]

where

\[
C_r=\sum_{hk-h'k'=r}a(h,k)\overline{a(h',k')}
e\!\left(\frac{Rr}{\sqrt{hk}+\sqrt{h'k'}}\right).
\tag{114.4}
\]

Moreover,

\[
C_0=\sum_n\left|\sum_{hk=n}a(h,k)\right|^2
\ll_\varepsilon LKX^\varepsilon
\ll_\varepsilon L^2X^\varepsilon.
\tag{114.5}
\]

Formula (114.4), by itself, supplies no cancellation for
\(\sum_{r\ne0}C_r\).

**(c) Exact mean-square implications.**  Define the minimal first Gram
with its ineffective even rows removed,

\[
M_h=\sum_h\left|\sum_k a(h,k)e(R\sqrt{hk})\right|^2
=\sum_{\substack{h\\h\ {\rm odd}}}
\left|\sum_k b(h,k)e(R\sqrt{hk})\right|^2,
\tag{114.6}
\]

and

\[
M_k=\sum_k\left|\sum_h\chi _4(h)b(h,k)e(R\sqrt{hk})\right|^2.
\tag{114.7}
\]

Then

\[
|T_{\rm low}|^2\ll L M_h,
\qquad
|T_{\rm low}|^2\ll K M_k.
\tag{114.8}
\]

Consequently \(M_h\ll L^2X^\varepsilon\) or
\(M_k\ll L^3K^{-1}X^\varepsilon\) is sufficient for the scalar target.
Since \(K\asymp L\), both required bounds are of order \(L^2\).  The
first orientation loses the nonzero values of \(\chi _4(h)\), which are
constant on a row and disappear in the modulus; the second retains the
character inside.

**(d) Literal ray identity and narrow capacity.**  For
\((h',k')=(h+p,k+q)\) with all four coordinates positive, put

\[
\rho=hk'-h'k=hq-kp
\]

and

\[
\mathcal B=1+\frac12\left(\frac ph+\frac qk\right)
+\sqrt{\left(1+\frac ph\right)\left(1+\frac qk\right)}.
\]

Then \(\mathcal B>0\), and on the fixed block \(\mathcal B\asymp1\),
and the exact identity is

\[
\sqrt{h'k'}-\sqrt{hk}
=\frac{kp+hq}{2\sqrt{hk}}
-\frac{\rho^2}{4(hk)^{3/2}\mathcal B}.
\tag{114.9}
\]

If \(N(Q)\) denotes the number of ordered supported pairs satisfying
\(|\rho|\le Q\), then for every \(Q\ge0\),

\[
N(Q)\ll LK\bigl(Q+\log(2L)\bigr).
\tag{114.10}
\]

The same bound holds for their absolute weighted contribution to
(114.2).  Hence \(Q\le L\) is within the \(L^3X^\varepsilon\) energy
budget.  The threshold at which the phase contribution of the remainder
in (114.9) is \(O(1)\) is

\[
Q_{\rm curv}\asymp
\left(\frac{(LK)^{3/2}}R\right)^{1/2}.
\tag{114.11}
\]

At the critical persistent scale this is \(Q_{\rm curv}\asymp1\), so
the naturally linearizable narrow band costs only
\(O(L^2\log L)\).

## 3. Proof or derivation

The unique lift map is

\[
g=\gcd(h,k),\qquad u=h/g,\qquad v=k/g.
\]

It is a bijection between positive \((h,k)\) and positive
\((g,u,v)\) with \((u,v)=1\).  Complete multiplicativity of \(\chi _4\),
including its zero values, gives
\(\chi _4(g)\chi _4(u)=\chi _4(gu)=\chi _4(h)\).  This proves the
coefficientwise passage from (B114.1) to (B114.2).  The quarter-shift
difference is consistent with

\[
e(g/4)-e(3g/4)=2i\chi _4(g),
\]

and the supplied identity therefore keeps the exact placement
\(Z=2iT_{\rm low}\).  In particular \(|Z|^2=4|T_{\rm low}|^2\); no
linear budget is confused with its square.

Expanding the modulus gives (114.1) and (114.2).  Positivity of all lift
variables shows

\[
g\sqrt{uv}=g'\sqrt{u'v'}
\quad\Longleftrightarrow\quad
g^2uv=g'^2u'v'.
\]

Equality \(uv=u'v'\) neither suffices when \(g\ne g'\), nor is necessary
when the square factors in \(g^2,g'^2\) differ.  Thus dropping either lift
changes the diagonal.

For (114.3)--(114.4), use the exact rationalization

\[
\sqrt{hk}-\sqrt{h'k'}
=\frac{hk-h'k'}{\sqrt{hk}+\sqrt{h'k'}}.
\]

For \(r=0\), let \(r_S(n)\) count supported factorizations \(hk=n\).
Boundedness of \(a\), Cauchy on each product fiber, and
\(r_S(n)\le\tau(n)\) give

\[
\begin{aligned}
C_0
&\le \sum_n r_S(n)\sum_{hk=n}|a(h,k)|^2\\
&\le \max_{n\ll LK}\tau(n)\sum_{h,k}|a(h,k)|^2
\ll_\varepsilon LKX^\varepsilon.
\end{aligned}
\]

This proves (114.5).  Notice that pairwise phase-diagonal equality is
not the same notion as an individual term having square product.

For the mean squares, write

\[
T_{\rm low}=\sum_h
 \left(\sum_k a(h,k)e(R\sqrt{hk})\right)
=\sum_k\left(\sum_h\chi _4(h)b(h,k)e(R\sqrt{hk})\right).
\]

Cauchy in the outer variable proves (114.8).  Expanding the two Gram
forms also shows their different sign content:

\[
M_h=\sum_h\sum_{k,k'}a(h,k)\overline{a(h,k')}
e\!\left(R\sqrt h(\sqrt k-\sqrt{k'})\right),
\tag{114.12}
\]

where \(\chi _4(h)\overline{\chi _4(h)}=1\) on every surviving row, so
the sign has disappeared, whereas

\[
M_k=\sum_k\sum_{h,h'}\chi _4(h)\chi _4(h')
b(h,k)\overline{b(h',k)}
e\!\left(R\sqrt k(\sqrt h-\sqrt{h'})\right)
\tag{114.13}
\]

retains it.  Each Gram diagonal has size at most \(O(LK)\), which is of
the required order \(L^2\).  Its absolute maximum is of order \(L^3\),
so a factor \(L\) of off-diagonal saving is still required.

To derive (114.9), set \(x=p/h\), \(y=q/k\).  The elementary identity

\[
\left(1+\frac{x+y}{2}\right)^2-(1+x)(1+y)
=\frac{(x-y)^2}{4}
\]

and rationalization give

\[
\sqrt{(1+x)(1+y)}-1-\frac{x+y}{2}
=-\frac{(x-y)^2}
 {4\left(1+(x+y)/2+\sqrt{(1+x)(1+y)}\right)}.
\]

Multiplication by \(\sqrt{hk}\), together with
\(x-y=(kp-hq)/(hk)=-\rho/(hk)\), proves (114.9).

It remains to prove the count (114.10).  Fix a supported \((h,k)\) and
write \(d=(h,k)\), \(h=dh_0\), \(k=dk_0\), with
\((h_0,k_0)=1\).  The value \(\rho=d(h_0q-k_0p)\) is a multiple of
\(d\).  For each admissible value, all solutions are translates by
\((p,q)\mapsto(p+h_0t,q+k_0t)\).  The fixed support boxes allow
\(O(d)\) such translates, and there are \(O(1+Q/d)\) admissible values.
Thus a fixed base point has \(O(d+Q)\) partners.  Since nonzero
coefficients have \(d\ll\sqrt L\),

\[
\sum_{(h,k)\ {\rm supported}}d\ll LK\log(2L).
\]

For example, this last estimate follows from
\(d=\sum_{m\mid d}\varphi(m)\) and counting multiples of each
\(m\ll\sqrt L\); the endpoint errors are smaller because \(K\asymp L\).
Summing \(O(d+Q)\) proves (114.10).

Finally, (114.9) shows that the phase size of its quadratic remainder is
\(\asymp R\rho^2/(LK)^{3/2}\), which proves (114.11).  This is an exact
literal connector for the ray defect, but it is not an estimate for the
remaining pairs.

The superficially similar identity for \(f(u,m)=u^2/m\) does not by
itself connect to this packet.  Identifying its variables with the lift
variables would require \(k=u^2/m\), which is neither a bijection of the
integer support nor compatible with the full product \(g^2uv\) in
general.  It can motivate (114.9), but only (114.9) supplies the lawful
literal connector.

## 4. First doubtful or unproved step

The first unproved step is any estimate for the broad complement

\[
|\rho|>Q
\]

that saves a full factor \(L\) in the scalar energy, or equivalently any
diagonal-critical bound for (114.6) or (114.7).  The exact
shifted-product grouping (114.4) also leaves this same cancellation
unproved: its denominator depends on both products, so it is not a
constant Fourier coefficient in \(r\).

No implication in the permitted material turns the rank-one identity
into broad cancellation.  In particular, an invertible regrouping of
the same pairs cannot be counted as a saving.  The scalar target might
use cancellations between different rows or columns that either Gram
form discards, so the mean-square bounds are sufficient but not
equivalent to the direct target.

## 5. Control tests and outcomes

| Control | Exact input and test | Outcome | Implication |
|---|---|---|---|
| `literal_packet_to_physical_sum_identity` | Apply the unique \(g=(h,k)\), \(u=h/g\), \(v=k/g\) map coefficientwise. | Pass. It gives \(a(h,k)=\chi _4(h)\eta((h,k)/G_0)A(h,k)\). | (114.1) and (114.2) are the same literal sum. |
| `gcd_lift_and_full_product_retention` | Retain \(g,g'\) before comparing phases. | Pass; the equality is \(g^2uv=g'^2u'v'\). | Reject \(uv=u'v'\) as the energy diagonal. |
| `quarter_shift_and_character_placement` | Keep \(Z=2iT_{\rm low}\) and use \(e(g/4)-e(3g/4)=2i\chi _4(g)\). | Pass. | The character is on \(h=gu\), and \(|Z|^2=4|T|^2\). |
| `linear_vs_energy_capacity` | Compare \(L^{3/2}\) with \(L^3\). | Pass. Whole absolute scalar energy has capacity \(L^4\); its true diagonal has capacity \(L^2X^\varepsilon\). | The off-diagonal must save one factor \(L\). |
| `mean_square_orientation_and_cauchy_cost` | Expand both Grams and pay outer cardinality \(L\) or \(K\). | Pass as an implication, not as a bound. | Both require an \(L^2\)-scale estimate; only the \(k\)-oriented Gram retains \(\chi _4\). |
| `equal_full_product_diagonal` | Group pairs with \(hk=h'k'\). | Pass; (114.5) is \(O(L^2X^\varepsilon)\). | The phase diagonal is not the bottleneck. |
| `shifted_product_connector` | Rationalize the square-root difference with \(r=hk-h'k'\). | Pass exactly at (114.4), but no saving follows. | Retain as a formulation only; a correlation theorem is still needed. |
| `ray_defect_connector_and_rank_one_identity` | Use \(\rho=hq-kp\) and derive the tangent remainder. | Pass exactly at (114.9). | The curvature-narrow band is lawful and has the capacity (114.10); the broad estimate remains open. |
| `coefficient-adversary` | In (114.6), take unit coefficients \(e(-R\sqrt{hk})\) on the effective odd support. In (114.7), take \(\chi _4(h)e(-R\sqrt{hk})\) on that support. | Under the coefficient-robust shadow allowing arbitrary bounded phases, both Grams become \(\asymp L^3\), violating their \(L^2\) targets by a factor \(L\). | Reject the bounded-arbitrary-coefficient versions. This does not refute the fixed smooth symbol, because the adversaries are highly oscillatory. |
| `no_shellwise_l1_or_cross_block_cancellation` | Keep \(\eta=\sum_\sigma\psi_\sigma\) inside \(a(h,k)\) before the modulus and use one physical block only. | Pass. | No shellwise triangle inequality or inter-block cancellation was used. |
| `square_near_square_high_gcd_owner_scope` | Add no terms outside the supplied \(T_{\rm low}\). Distinguish pairwise product equality from an individual square product. | Pass. | No separately owned term is recounted. |
| `critical_j1_and_exact_square_j2_boundary` | Use only persistent \(j=1\), \(K\asymp L\), \(L\asymp R^{1/3}\). | Pass. | The fact that the algebra also makes sense at ratio 16 does not discharge the separately owned exact-square \(j=2\) boundary. |
| `involution_barrier_and_downstream_scope` | Check whether any reindexing was treated as cancellation. | Pass. No involution or self-return was used as a bound. | Results concern this fixed balanced packet only and imply no full M2 or Gauss-circle conclusion. |

The requested capacity table is:

| Object | Absolute capacity | Diagonal capacity | Cauchy cost to scalar | Bound sufficient for \(|T|^2\ll L^3X^\varepsilon\) | Character status |
|---|---:|---:|---:|---:|---|
| Direct scalar \(|T|^2\) | \((LK)^2\asymp L^4\) | \(LKX^\varepsilon\asymp L^2X^\varepsilon\) | none | \(L^3X^\varepsilon\) directly | retained across all pairs |
| \(h\)-row Gram \(M_h\) | \(LK^2\asymp L^3\) | \(LK\asymp L^2\) | \(L\) | \(M_h\ll L^2X^\varepsilon\) | lost outside each row modulus |
| \(k\)-column Gram \(M_k\) | \(KL^2\asymp L^3\) | \(KL\asymp L^2\) | \(K\asymp L\) | \(M_k\ll L^3K^{-1}X^\varepsilon\asymp L^2X^\varepsilon\) | retained inside each column modulus |

## 6. Dependencies and exact artifacts used

This statement-only derivation used exactly:

1. `problems/gauss_circle.md`;
2. `state/control_models.md`;
3. `rounds/codex-managed/m9-m2-balanced-literal-energy-connector-fork/blind_statement.md`;
4. the assigned task brief.

No strategy file, proof graph, proof draft, derivation packet, prior-round
report, sibling report, external source, or numerical experiment was
used.

## 7. Recommended state effect

**Revise.**  Promote as internal support the literal two-lift energy
formula, the full-product diagonal bound (114.5), the exact
shifted-product formula (114.4), the exact ray identity (114.9), and the
narrow-capacity estimate (114.10).  Retain the actual-symbol
\(k\)-oriented mean square and the broad ray complement as open
possibilities.  Reject \(uv=u'v'\) as the diagonal, reject a connector
based only on the model \(u^2/m\) identity, and reject both
arbitrary-coefficient mean-square shadows.  No change to the fixed-block
target, M2, or the global exponent is justified.

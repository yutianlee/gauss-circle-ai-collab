# Round 112 blind statement

Let \(R=\sqrt X\), \(1\le L\le R^{1/2}\), and consider one real smooth
balanced residual label after a fixed finite subdivision of
\(1\le K/L\le16\):

\[
 \mathcal T_A(R)
 =\sum_{h,k}\chi_4(h)A(h/L,k/K)e(R\sqrt{hk}),
\tag{B112.1}
\]

where \(A\) is a literal real compact smooth profile. All hard-endpoint,
exact-square, \(R^{-1}\)-near-square, and large-gcd owners are already
separate. Choose one fixed smooth dyadic partition of
\(g=(h,k)\). On \(g\asymp G<L^{1/2}\), write

\[
 h=gu,\qquad k=gv,\qquad (u,v)=1.
\tag{B112.2}
\]

Every nonzero term has \(h\) odd, hence \(g,u\) odd and
\(\chi_4(h)=\chi_4(g)\chi_4(u)\). Let \(F_{\omega,u,v,G}(t)\) be the
compact real \(g/G\)-profile for the literal label \(\omega\), including
the fixed gcd partition and all smooth physical weights. With

\[
 \widehat F(\xi)=\int_{\mathbb R}F(t)e(-t\xi)\,dt,
\qquad
 \chi_4(g)={e(g/4)-e(3g/4)\over2i},
\tag{B112.3}
\]

define

\[
 \begin{aligned}
 \mathcal Q_{\omega,G}(R)
 =\sum_{\substack{u,v\\(u,v)=1\\u\ {\rm odd}}}
 \chi_4(u)\sum_{n\in\mathbb Z}
 \Big[&
 \widehat F_{\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-1/4)\big)\\
 -&
 \widehat F_{\omega,u,v,G}
   \big(G(n-R\sqrt{uv}-3/4)\big)
 \Big].
 \end{aligned}
\tag{B112.4}
\]

The proposed exact positive-frequency identity is

\[
 \mathcal T_{\omega,\mathrm{small}}^+(R)
 ={1\over2i}\sum_{G<L^{1/2}}G\mathcal Q_{\omega,G}(R).
\tag{B112.5}
\]

The actual negative-frequency block is to be handled only through the
literal real-even conjugacy of the physical coefficient. The open direct
target is

\[
 \left|\sum_{\omega}\sum_{G<L^{1/2}}
 G\mathcal Q_{\omega,G}(R)\right|
 \ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{B112.6}
\]

The absolute value stays outside every physical label and \(G\)-shell
that the one-count assembly permits to cancel. Shellwise
\(\sum G|\mathcal Q_G|\), product-fibre absolute values, and a Cauchy Gram
are stronger surrogates.

Derive only what follows from this statement. Audit the two quarter shifts,
the \(1/(2i)\) normalization, parity, frequency conjugacy, finite support,
and norm hierarchy. Do not infer (B112.6), the hard endpoint, M9-M2, M9,
or an exponent.


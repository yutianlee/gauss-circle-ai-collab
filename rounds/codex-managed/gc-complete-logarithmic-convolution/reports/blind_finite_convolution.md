# Round 225: isolated finite logarithmic convolution

## 1. Result

The logarithmic identity
\[
 f\log=f*(\Lambda+\chi\Lambda),\qquad f=1*\chi,
\]
and the requested four-term identity for each of the two characters hold coefficientwise. The full contraction below retains every convolution factor, both characters, all prime powers and all literal truncation boundaries.

These are finite algebraic identities. They supply no power saving or orthogonality. An exact positive one-point control attains the coefficient triangle.

This reused agent retains earlier research roles and reports. The present task is statement-only isolation, not history-free work. I read only the assigned statement and protocol; no application, graph, manifest, strategy, sibling, web source or experiment was used.

## 2. Exact hypotheses and statements

All functions are on positive integers. Dirichlet convolution is
\[
 (u*v)(n)=\sum_{de=n}u(d)v(e),
\]
and \(\delta=\mathbf1_{\{1\}}\) is its identity. All products involving \(\log\) or a character outside a convolution are pointwise. Let \(\chi=\chi_4\), with its even zero values, and let
\(\Lambda(p^j)=\log p\) for \(j\ge1\), zero otherwise.

For each function \(\psi\in\{1,\chi\}\), put
\[
 a_\psi=\psi,\quad g_\psi=\mu\psi,\quad
 b_\psi=\Lambda\psi,\quad c_\psi=\psi\log.
\]
For real \(U,V\ge1\), subscripts \(\le U,>U,\le V,>V\) mean multiplication by the indicated literal integer predicates. Then
\[
 \boxed{
 b_\psi=(b_\psi)_{\le V}+(g_\psi)_{\le U}*c_\psi
 -(g_\psi)_{\le U}*(b_\psi)_{\le V}*a_\psi
 +(g_\psi)_{>U}*(b_\psi)_{>V}*a_\psi.}
 \tag{1}
\]
Every equality is coefficientwise, without a convergence or analytic Dirichlet-series hypothesis.

For a finitely supported complex \(F\) with \(F(1)=0\), set
\[
 B=\max(\{1\}\cup\operatorname{supp}F),\qquad
 H_F(n)=
 \begin{cases}F(n)/\log n,&n\ge2,\\0,&n=1.\end{cases}
 \tag{2}
\]
This gives the unweighted contraction in (6). The direct contraction of the logarithmic identity is also specified there.

## 3. Proof and full contraction

### Finite convolution relations

Prime factorization gives
\[
 \sum_{d\mid n}\Lambda(d)=\log n,\qquad
 \sum_{d\mid n}\mu(d)=\delta(n).
 \tag{3}
\]
Indeed the first sum contributes \(v_p(n)\log p\) for each prime; the second is the product of \(1-1\) over the distinct prime divisors when \(n>1\).

Complete multiplicativity, including the zero values of \(\chi\), implies
\[
 a_\psi*g_\psi=\delta,\qquad a_\psi*b_\psi=c_\psi,\qquad
 g_\psi*c_\psi=b_\psi.
 \tag{4}
\]
For example the first two sums are respectively
\(\psi(n)\sum_{d\mid n}\mu(d)\) and
\(\psi(n)\sum_{d\mid n}\Lambda(d)\).
There is no division by \(\psi(n)\), so even \(n\) in the \(\chi\) branch causes no exception.

The operator \(D u=u\log\) satisfies
\(D(u*v)=(Du)*v+u*(Dv)\), since \(\log(de)=\log d+\log e\).
Using \(\log=1*\Lambda\) and \(\chi\log=\chi*(\chi\Lambda)\) from (3)--(4), we obtain
\[
 D(1*\chi)=(1*\Lambda)*\chi+1*(\chi*(\chi\Lambda))
         =f*(b_1+b_\chi).
 \tag{5}
\]

To prove (1), abbreviate the subscripts of the fixed \(\psi\) branch. From (4),
\[
 b=g_{\le U}*c+g_{>U}*(b*a)
   =g_{\le U}*c+g_{>U}*b_{\le V}*a
                       +g_{>U}*b_{>V}*a.
\]
Because \(g_{>U}=g-g_{\le U}\) and \(g*a=\delta\), the middle term is
\(b_{\le V}-g_{\le U}*b_{\le V}*a\).
This proves every sign in (1). In particular the high-high convolution has a plus sign even though its Möbius coefficients need not be positive.

Coefficientwise, the same calculation states
\[
 \begin{aligned}
 b_\psi(n)={}&\mathbf1_{n\le V}b_\psi(n)
 +\sum_{\substack{dt=n\\d\le U}}g_\psi(d)c_\psi(t)\\
 &-\sum_{\substack{det=n\\d\le U,\ e\le V}}
      g_\psi(d)b_\psi(e)a_\psi(t)
 +\sum_{\substack{det=n\\d>U,\ e>V}}
      g_\psi(d)b_\psi(e)a_\psi(t).
 \end{aligned}
\]
This is a finite divisor identity for each \(n\).

### Explicit finite product sums

Substitute (1) for both \(b_1\) and \(b_\chi\) in (5), retain the outer \(f\), and pair with \(H_F\). All indices below are positive integers:
\[
 \boxed{\begin{aligned}
 \sum_{n\ge1}f(n)F(n)
 =\sum_{\psi\in\{1,\chi\}}\Bigg[&
 \sum_{\substack{re\le B\\e\le V}}
   f(r)\Lambda(e)\psi(e)H_F(re)\\
 &+\sum_{\substack{rdt\le B\\d\le U}}
   f(r)\mu(d)\psi(d)\psi(t)\log t\,H_F(rdt)\\
 &-\sum_{\substack{rdet\le B\\d\le U,\ e\le V}}
   f(r)\mu(d)\psi(d)\Lambda(e)\psi(e)\psi(t)H_F(rdet)\\
 &+\sum_{\substack{rdet\le B\\d>U,\ e>V}}
   f(r)\mu(d)\psi(d)\Lambda(e)\psi(e)\psi(t)H_F(rdet)
 \Bigg].
 \end{aligned}}
 \tag{6}
\]
The direct log-weighted contraction is the same displayed right side with every \(H_F\) replaced by \(F\), and left side
\(\sum_n f(n)\log n\,F(n)\). Thus (6) neither loses a logarithm nor divides by \(\log1\).

The first term has \(e\le V\); the second has \(d\le U\); the third has both. The last has \(d>U,e>V\), hence \(de>UV\). The factors \(r\) and \(t\) remain in full, as do \(\psi(d),\psi(e),\psi(t)\) where present. There is no additional factor \(\psi(r)\). In the twisted branch, an even one of \(d,e,t\) makes the corresponding term zero, but an even \(r\) is not discarded.

Finite support makes every displayed sum finite even when \(U\) or \(V\) is large. For fixed \(r,d,e\), the last variable satisfies the inclusive bound \(t\le\lfloor B/(rde)\rfloor\). The smaller products have the analogous exact floor. Holes in the support of \(F\) remain through \(H_F\); replacing support by the containing interval does not fill them.

### Local logarithmic kernel

The kernel in (5) is \(K(n)=(1+\chi(n))\Lambda(n)\). It vanishes at \(1\) and at non-prime-powers, and its complete local list is
\[
 \begin{array}{c|c}
 \text{argument}&K(\text{argument})\\ \hline
 p^j,\ p\equiv1\pmod4,\ j\ge1&2\log p\\
 p^j,\ p\equiv3\pmod4,\ j\text{ odd}&0\\
 p^j,\ p\equiv3\pmod4,\ j\text{ even}&2\log p\\
 2^j,\ j\ge1&\log2 .
 \end{array}
 \tag{7}
\]
Even powers of inert primes and all powers of two are therefore compulsory.

## 4. First unproved step

No step is missing in the finite identities or contractions. Any estimate exploiting cancellation in (6), orthogonality between its product sums, or a power saving requires additional hypotheses and analysis absent from the statement. The identities neither prescribe nor prove such estimates.

The condition \(de>UV\) is only a support restriction. It is not cancellation, and the plus sign on the high-high convolution is not coefficient positivity. Likewise a formal splitting into two character branches does not make those branches orthogonal.

## 5. Exact controls and outcomes

### Identity point and prime powers

At \(n=1\), \(\Lambda(1)=\log1=0\), and every term of (1) and (5) is zero. Although \(f(1)=1\), the assumption \(F(1)=0\) makes (6) exact with no missing singleton. If \(F=0\), \(B=1\) and all displayed contractions vanish.

For any prime \(p\), let \(z=\psi(p)\), which can be zero. For \(\nu\ge1\),
\[
 a_\psi(p^\nu)=z^\nu,\quad
 b_\psi(p^\nu)=z^\nu\log p,\quad
 c_\psi(p^\nu)=\nu z^\nu\log p,
\]
while \(g_\psi(1)=1,\ g_\psi(p)=-z,\ g_\psi(p^j)=0\) for \(j\ge2\). Put
\[
 u=\mathbf1_{p\le U},\quad
 v_\nu=\mathbf1_{p^\nu\le V},\quad
 B_\nu=\#\{1\le j\le\nu:p^j\le V\},\quad B_0=0.
\]
The four terms in (1), at \(p^\nu\), are respectively \(z^\nu\log p\) times
\[
 v_\nu,\quad
 \nu-u(\nu-1),\quad
 -B_\nu+uB_{\nu-1},\quad
 -(1-u)(\nu-1-B_{\nu-1}).
 \tag{8}
\]
These four factors sum to one because \(B_\nu-B_{\nu-1}=v_\nu\).
Equation (8) multiplies by \(z^\nu\); it never divides by it. It therefore covers the zero twisted coefficients at powers of two, as well as split and inert primes. The equalities \(U=p\) and \(V=p^\nu\) are included on the low side exactly.

Also
\[
 f(p^\nu)=
 \begin{cases}
 \nu+1,&p\equiv1\pmod4,\\
 1,&p\equiv3\pmod4,\ \nu\text{ even},\\
 0,&p\equiv3\pmod4,\ \nu\text{ odd},\\
 1,&p=2.
 \end{cases}
 \tag{9}
\]
At split powers, the convolution in (5) is
\(2\log p\sum_{j=1}^{\nu}(\nu-j+1)=\nu(\nu+1)\log p\).
At an even inert power \(\nu=2m\), exactly \(m\) even powers contribute \(2\log p\) each; at an odd inert power every remaining \(f\)-factor is zero. At \(2^\nu\), all \(\nu\) terms contribute \(\log2\). These equal \(f(p^\nu)\log(p^\nu)\) in every case. A singleton test at any \(p^\nu\) consequently verifies both versions of the contraction.

### Support and large parameters

All real truncations mean \(d\le\lfloor U\rfloor\) versus \(d\ge\lfloor U\rfloor+1\), and similarly for \(V\). There is no overlap or omitted boundary. If \(UV\ge B\), the high-high term of (6) is empty, including equality, since \(de>UV\).

If \(U\ge B\), on every relevant divisor \(g_{\le U}=g\) and \(g_{>U}=0\). The second term of (1) is \(b\), and the third cancels \(b_{\le V}\). If \(V\ge B\), the high-high term is zero, \(b_{\le V}=b\), and \(g_{\le U}*c\) cancels \(g_{\le U}*b*a\). Thus either large-parameter limit gives exactly \(b\), before and after convolution with \(f\).

### Positive one-point control

Take \(F=\delta_5\) and \(U=V=1\). In (1) the low \(b\) and negative term vanish, \(g_{\le1}=\delta\), and no high-high product divides \(5\). In (6), only the second term contributes, with \(r=d=1,t=5\). Each of the two character branches contributes
\[
 \psi(5)\log5\,H_F(5)=1.
\]
Hence \(\sum_n f(n)F(n)=2\), and the coefficient triangle is exactly \(2\). In the log-weighted version both sides and that triangle equal \(2\log5\). There is no cross-character cancellation.

More generally \(K\ge0\), and (9) and multiplicativity give \(f\ge0\). For \(F=\delta_{5^\nu}\), every nonzero term of the basic contraction of (5) with \(H_F\) is positive; its coefficient triangle equals \(\nu+1\), the exact left side. Thus even at arbitrarily large support points the finite logarithmic identity supplies no automatic power reduction of that triangle. This control does not rule out other estimates under additional hypotheses.

All requested finite controls pass. Zero mathematical experiments were used.

## 6. Exact inputs and provenance

Campaign: gc-complete-logarithmic-convolution. Round: 225. Role: blind_finite_convolution. Current statement-only task with retained prior agent history disclosed in Section 1.

Exactly two input files were read:

| Input | SHA-256 |
|---|---|
| protocol.md | f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a |
| rounds/codex-managed/gc-complete-logarithmic-convolution/briefs/blind_finite_convolution_statement.md | a5e2bc3a6d7b07e43bcfcfbd4db63d15f9120c3be00ea5b4257abde8e1b2a5b7 |

The proofs use only finite divisor algebra, the given completely multiplicative characters and prime factorization. No analytic theorem or source is imported. No graph hash or application status is inferred from retained history. Effort is entirely analytical; this report is the sole output.

## 7. Recommended state effect

Retain the finite identities, complete contraction and exact scope controls as statement-only evidence for the conductor's review. No analytic bound, orthogonality, application target or owner closure is asserted. No shared state is changed and no successor is proposed. Stop after freezing this report.

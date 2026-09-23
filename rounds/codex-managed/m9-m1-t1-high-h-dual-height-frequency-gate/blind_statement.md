# Statement-only packet: Round 189 dual height frequency

Fix \(X\ge2\), \(L\ge2\), \(Q=\lfloor(\log(2X))^B\rfloor\), and a
nonempty dyadic integer block \(Y<h\le2Y\) with \(Y>Q\). Fixed
polylogarithms may enter \(X^\varepsilon\), but no positive power of
\(Y\) may be absorbed.

Consider one complex aggregate under one outer real part:

\[
 \Re\!\sum_{\omega}\sum_{\kappa,u,U,m,q,a,h,v,t}
 \frac1m c_q(a)e\!\left(\frac{\epsilon_\omega a\bar v h}{q}\right)
 (-1)^tB_{\kappa,u,U,m,q,a,h,v,t,\omega}.
\tag{B189.1}
\]

Here \(\epsilon_+=1\), \(\epsilon_-=-1\), and

\[
 U=mq\mid u,quad q>Q,quad U>4Q,quad (a,q)=1,quad
 m|a|_q>Q,quad Qm<Y,
\tag{B189.2}
\]

\[
 u\asymp L/\kappa,quad v\asymp L/\kappa,quad (u,v)=1,quad
 (U,h)=1,quad Y<h\le2Y.
\tag{B189.3}
\]

The inverse \(\bar v\) is modulo \(q\),
\(|x|_q=\min([x]_q,q-[x]_q)\), and

\[
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}},\qquad
 \sum_{(a,q)=1}|c_q(a)|\ll\log(2q).
\tag{B189.4}
\]

For fixed \((\kappa,u,U,h,v,\omega)\), at most \(O(\kappa)\) indices
\(t\) are live and \(|B|\ll_\varepsilon X^\varepsilon\). Literal
deletions are inside \(B\) and only reduce capacity. No periodicity,
bounded variation, factorization, or smoothness of \(B\) in \(h,v,t\)
is supplied.

Define

\[
 j_q(a,v)=|a\bar v|_q.
\tag{B189.5}
\]

Because \(q\mid u\) and \((u,v)=1\), \(v\) is a unit modulo \(q\).
The proposed strict sector is

\[
 1\le j_q(a,v)\le\left\lfloor\frac {mq}Y\right\rfloor
 =\left\lfloor\frac UY\right\rfloor.
\tag{B189.6}
\]

Prove or refute that (B189.6) contains \(O(um/Y)\) possible \(v\)'s in
(B189.3), including \(\lfloor U/Y\rfloor=0\). Price the resulting
factor \(m\) against the exact prefactor \(1/m\), restore all remaining
powers, and decide whether this whole sector is
\(O_{B,\varepsilon}(L^2X^\varepsilon)\) after \(U=mq\mid u\).
Retain its exact complement under the same real part;
attempt the full target only with a proved variation/discrepancy of the
fixed amplitudes, otherwise state the first missing relation and deficit.

As an independent control, let

\[
 E_q(b)=(-1)^{[b]_q},\quad
 K_q(b)=\sum_{(a,q)=1}c_q(a)e(ab/q),\quad
 K_q^\circ(b)=K_q(b)-\mu(q)/q.
\tag{B189.7}
\]

Check, for \((b,q)=1\),

\[
 K_q(b)=\frac1q\sum_{d\mid q}\mu(q/d)dE_d(b).
\tag{B189.8}
\]

For prime \(p\), test \(K_p^\circ(b)=E_p(b)\) and the
\((p-1)/2\) unit-height prefix discrepancy at \(b=-2\bmod p\). This
is only a falsifier of a uniform polylogarithmic prefix theorem.

Even a complete proof affects only one inherited original-\(t=1\)
residual, not original \(t\ge2\), a parent, bridge, quarter theorem, or
global exponent.

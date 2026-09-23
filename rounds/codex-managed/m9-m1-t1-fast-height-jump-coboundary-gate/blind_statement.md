# Statement-only packet: Round 191 fast height jumps

Fix \(X\ge2\), \(L\ge2\), \(Q=\lfloor(\log(2X))^B\rfloor\), and a
nonempty integer block \(Y<h\le2Y\) with \(Y>Q\). Fixed logarithmic
powers may enter \(X^\varepsilon\), but no positive power of \(Y\) may be
absorbed.

Fix positive integers \(\kappa,u,m,q\), a unit \(a\bmod q\), and put

\[
 U=mq\mid u,\qquad g=u/U,\qquad
 U>4Q,\quad q>Q,\quad m|a|_q>Q,\quad Qm<Y.
\tag{B191.1}
\]

All of \(\kappa,g,U\) are odd. Literal rows have

\[
 (u,v)=1,\qquad (U,h)=1,\qquad
 0<2\kappa gh<\lceil L\rceil,\qquad v\asymp L/\kappa.
\tag{B191.2}
\]

For \(U>1\), let \(\bar v_Uv\equiv1\pmod U\) and choose the canonical
anchors

\[
 S_{0,+}=[\bar v_Uh]_U,\quad
 w_{0,+}=(S_{0,+}v-h)/U,
\]

\[
 S_{0,-}=[-\bar v_Uh]_U,\quad
 w_{0,-}=(h+vS_{0,-})/U.
\tag{B191.3}
\]

For \(\omega\in\{+,-\}\), put

\[
 S_{t,\omega}=S_{0,\omega}+Ut,\qquad
 s_{t,\omega}=gS_{t,\omega},\qquad
 w_{t,\omega}=w_{0,\omega}+vt,
\]

\[
 I_{h,v,\omega}
 =\{t\in\mathbb Z:S_{t,\omega}>0,\ w_{t,\omega}>0\}.
\tag{B191.4}
\]

Let \(\lambda_{N,\sigma}(d)\) be a fixed zero-extended literal endpoint
coefficient. It is zero unless \(N>0\), \(d\mid N\), \(N\) is
squarefree, \(d\) is odd, and every original selector, coprimality, shell,
cone, profile, floor, star, half-weight, hard-sample, crossing, endpoint,
and sign predicate holds. On support

\[
 |\lambda_{N,\sigma}(d)|\ll_\varepsilon X^\varepsilon.
\tag{B191.5}
\]

For \(r=2\kappa gh\), define

\[
 N_{h,v,t}^{+}=\kappa gU(\kappa v+2w_{t,+}),\qquad
 N_{h,v,t}^{+}+r=(\kappa gU+2s_{t,+})\kappa v,
\]

\[
 N_{h,v,t}^{-}=(\kappa gU+2s_{t,-})\kappa v,\qquad
 N_{h,v,t}^{-}+r=\kappa gU(\kappa v+2w_{t,-}).
\tag{B191.6}
\]

The literal affine amplitudes are

\[
 B_{h,v,+}^{\sigma}(t)=
 \left(1-\frac r{\lceil L\rceil}\right)
 \lambda_{N_{h,v,t}^{+}+r,\sigma}(\kappa gU+2s_{t,+})
 \overline{\lambda_{N_{h,v,t}^{+},\sigma}(\kappa gU)}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N_{h,v,t}^{+}+r}+\sqrt{N_{h,v,t}^{+}}}\right),
\]

\[
 B_{h,v,-}^{\sigma}(t)=
 \left(1-\frac r{\lceil L\rceil}\right)
 \lambda_{N_{h,v,t}^{-}+r,\sigma}(\kappa gU)
 \overline{\lambda_{N_{h,v,t}^{-},\sigma}(\kappa gU+2s_{t,-})}
 e\!\left(\frac{\sigma\sqrt X\,r}
 {\sqrt{N_{h,v,t}^{-}+r}+\sqrt{N_{h,v,t}^{-}}}\right).
\tag{B191.7}
\]

Positivity is imposed before every square root. Define the complete
zero-extended height sequence

\[
 W_{v,\omega}(h)=
 \mathbf1_{Y<h\le2Y}\mathbf1_{(U,h)=1}
 \mathbf1_{0<2\kappa gh<\lceil L\rceil}
 \sum_{t\in I_{h,v,\omega}}(-1)^tB_{h,v,\omega}^{\sigma}(t),
\tag{B191.8}
\]

with every undeclared literal predicate already inside the two
\(\lambda\)'s. The anchor factor \((-1)^{S_{0,\omega}}\) has already
been replaced exactly by its Fourier phase and is therefore not also
present in \(W\). For fixed \(h,v,\omega\), at most \(O(\kappa)\)
affine sites are live.

Let \(\bar v_q\) be the inverse modulo \(q\),

\[
 j_q(a,v)=|a\bar v_q|_q,\qquad
 T_Q=\min\left\{\frac{q-1}{2},
 \left\lfloor\frac{Qmq}{Y}\right\rfloor\right\}.
\tag{B191.9}
\]

Fix a nonempty fast dyadic band

\[
 J\le j_q(a,v)<2J,\qquad j_q(a,v)>T_Q,
\tag{B191.10}
\]

and put

\[
 z_{\omega,v}=e(\epsilon_\omega a\bar v_q/q),\qquad
 \epsilon_+=1,\quad\epsilon_-=-1,\qquad
 \Delta^-W(h)=W(h)-W(h-1).
\tag{B191.11}
\]

The proposed signed packet is

\[
 \mathscr J=
 \sum_{\substack{\omega,v\ {\rm literal}\\
 J\le j_q(a,v)<2J}}
 \frac1{1-z_{\omega,v}}
 \sum_h\Delta^-W_{v,\omega}(h)z_{\omega,v}^h.
\tag{B191.12}
\]

Independently prove the endpoint-exact Abel identity behind (B191.12),
including its sign. Then determine whether the stated literal hypotheses
prove

\[
 |\mathscr J|\ll_{B,\varepsilon}Qm\kappa uX^\varepsilon,
\tag{B191.13}
\]

prove a genuinely smaller strict packet with an exact complement, or
establish a rigorous insufficiency/no-go result. The report must identify
the exact common-range and birth/death decomposition and the first missing
property. It may use adversarial bounded arrays only to refute a theorem
for the stated coefficient class, not as a lower bound for the fixed
literal packet.

On the band, \(|1-z_{\omega,v}|^{-1}\asymp q/J\). Individual positive
variation would require total scale \(Qm\kappa uJ/q\), while the available
pointwise scale is \(Y\kappa uJ/q\). The missing factor is \(Y/(Qm)\).
Do not move an absolute value inside the complete packet, separately
absolutize orientations, assume a mask is periodic or smooth, or assert an
orientation involution or projective-neighbor identity without proof.

Even a complete proof affects only one inherited original-\(t=1\)
residual. It proves no \(t\ge2\) incidence, parent, bridge, quarter
theorem, or global exponent by itself.

# Blind rederivation of the one-sided divisor false-theta kernel

## 1. Result

The proposed generating identity is correct. More precisely, after the
boundary-preserving change of variables \(k=q-4h\),

\[
 \mathscr F(z)=\sum_{h\geq 1}\sum_{\substack{k\geq1\\k\ {\rm odd}}}
 \chi _4(k)z^{4h^2+hk}
 =\sum_{h\geq1}\frac{z^{4h^2+h}}{1+z^{2h}},\qquad |z|<1.
\]

It has an exact signature-\((1,1)\) sign-kernel representation, but one of
the two cone edges is isotropic. Thus it is a degenerate indefinite/false
theta, not an ordinary modular theta merely by inspection. Under the
packet's precise convention (63.5), however, the alternative level-four
Appell sum does give an exact completion:
\[
 \mathscr F(z)=\frac12
 \left(A_4(1/2,-3\tau/2;\tau)-\frac12\right),
 \qquad z=e^{\pi i\tau}.
\]
Equivalently, in the Semikhatov convention,
\[
 \mathscr F(z)=\frac12\mathscr K_4
 \!\left(\tau,\frac{\tau}{8},\frac12-\frac{\tau}{8}\right)-\frac14.
\]
The correction \(1/2\) in the bilateral sum and the final factor \(1/2\)
are essential. By contrast, the tempting specialization
\(\mathscr K_4(\tau,0,1/2)\) collapses to an ordinary theta.
I also derive an exact one-sided character-Poisson formula. Its explicit
correction is \(\frac12\sum_h w(4h^2)\), even though the arithmetic line
\(q=4h\) contains no odd \(q\), and an exact Abel--Fourier representation
whose essential radial compensation is \(\rho^{-u}\).

None of these exact representations proves the requested square-root-phase estimate.
In the Poisson formula, stationary phase produces the reciprocal cone

\[
 X^{-1/4}\sum_{\substack{h,j>0\\j\asymp h\sqrt{X/N}}}
 \frac{\chi _4(j)}{h}
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j),
\]

up to displayed constants and controlled interior stationary-phase errors.
Its sum of termwise magnitudes is of order \(X^{1/4}\). Consequently a
Poisson, modular, or additive-phase transform followed only by absolute
values does not establish \(\mathcal L_{X,V}(N)\ll X^\varepsilon\) on any
nonempty radial interval. A new cancellation theorem for this reciprocal
cone (including its endpoint transitions) would still be required.

## 2. Exact statement and hypotheses

Write \(e(t)=e^{2\pi i t}\), and extend \(\chi _4\) to all integers in the
usual way: it is \(0\) on even integers, \(1\) modulo \(4\), and \(-1\)
modulo \(4\). Let \(V\in C_c^\infty((0,\infty))\), with
\({\rm supp}(V)\subset[a,b]\), \(0<a<b<\infty\), and put

\[
 w(u)=V(u/N)u^{-3/4}e(\sqrt{Xu})\quad (u>0),
\]

extended by zero off its compact positive support. Then the following
statements are exact.

1. The coefficient and generating identities are

\[
 \mathcal D(n)=
 \sum_{\substack{h\ge1,\ k\ge1\ {\rm odd}\\n=4h^2+hk}}\chi _4(k),
 \qquad
 \mathscr F(z)=\sum_{h\ge1}\sum_{k\ge1\ {\rm odd}}
 \chi _4(k)z^{4h^2+hk}.
 \tag{2.1}
\]

2. With \(Q(h,k)=4h^2+hk\),

\[
 \boxed{\displaystyle
 \mathscr F(z)=\frac14
 \sum_{\substack{h\in\mathbb Z\setminus\{0\}\\k\in\mathbb Z,\ k\ {\rm odd}}}
 \chi _4(k)\bigl({\rm sgn}(h)+{\rm sgn}(k)\bigr)z^{Q(h,k)}}.
 \tag{2.2}
\]

Only equal-sign pairs contribute, so (2.2) is absolutely convergent for
\(|z|<1\). The matrix of \(Q\) is
\(\left(\begin{smallmatrix}4&1/2\\1/2&0\end{smallmatrix}\right)\), of
signature \((1,1)\). For the associated bilinear form

\[
 B((r,s),(h,k))=8rh+rk+sh,
\]

the sign kernel is
\({\rm sgn}B((1,-8),(h,k))-{\rm sgn}B((0,-1),(h,k))\).
Here \(Q(1,-8)=-4\), whereas \(Q(0,-1)=0\). Thus the \(h=0\) edge is
null. It cannot simply be inserted: its formal contribution has \(Q=0\)
and \(\chi _4(k){\rm sgn}(k)=\chi _4(|k|)\), whose individual terms do not
tend to zero as \(|k|\to\infty\); hence the boundary series diverges.

3. Put \(z=e^{\pi i\tau}\), \(Q=z^2\), with
\({\rm Im}(\tau)>0\), and use exactly the packet's conventions
(63.4)--(63.5). For (63.4), at \((\nu,\mu)=(0,1/2)\), direct pairing gives

\[
 \frac{z^{4h^2}}{1+z^{2h}}+
 \frac{z^{4h^2}}{1+z^{-2h}}=z^{4h^2},
\]

and the \(h=0\) term is \(1/2\). Hence that specialization is exactly
\[
 \frac12+\sum_{h\ge1}z^{4h^2},
\]
an ordinary bilateral theta half-sum, not \(\mathscr F\).
For the convention (63.5), substituting
\(u=1/2,\ v=-3\tau/2\) gives
\[
 A_4(1/2,-3\tau/2;\tau)
 =\sum_{r\in\mathbb Z}\frac{z^{4r^2+r}}{1+z^{2r}}.
\]
This bilateral series is absolutely convergent. Its zero term is \(1/2\),
and the negative summand paired with \(r=h>0\) satisfies
\[
 \frac{z^{4h^2-h}}{1+z^{-2h}}
 =\frac{z^{4h^2+h}}{1+z^{2h}}.
\]
Consequently the exact, audited Appell completion is
\[
 \boxed{\displaystyle
 A_4(1/2,-3\tau/2;\tau)=\frac12+2\mathscr F(z),\qquad
 \mathscr F(z)=\frac12A_4(1/2,-3\tau/2;\tau)-\frac14.}
 \tag{2.2A}
\]
Direct comparison with (63.4) also gives, term by term,
\[
 \boxed{\displaystyle
 \mathscr K_4\!\left(\tau,\frac{\tau}{8},
 \frac12-\frac{\tau}{8}\right)
 =A_4(1/2,-3\tau/2;\tau)
 =\frac12+2\mathscr F(z).}
 \tag{2.2K}
\]
Indeed \(8\pi i r(\tau/8)=\pi i r\tau\), and
\(\nu+\mu=1/2\), so its numerator is \(z^{4r^2+r}\) and denominator is
\(1+z^{2r}\).

This exact identity is not itself a modular law for \(\mathscr F\). The
elliptic point moves with \(\tau\). Under the parameter rescaling appearing
in an \(S\)-transformation, it would become
\[
 \left(\frac{\nu}{\tau},\frac{\mu}{\tau}\right)
 =\left(\frac18,\frac1{2\tau}-\frac18\right),
 \tag{2.2S}
\]
whereas the defining path at \(\tau'=-1/\tau\) is
\[
 (\nu',\mu')=\left(-\frac1{8\tau},
 \frac12+\frac1{8\tau}\right).
\]
These pairs are not equal for general \(\tau\). Thus the modular orbit is
not closed on the single function \(\mathscr F\) by direct substitution;
an exact Appell transformation theorem would introduce a different
specialization and its Mordell correction. No such theorem is imported
here.

4. For \(j\ne0\), define

\[
 I_{h,j}:=\frac1h\int_{4h^2}^{\infty}
 w(u)e\!\left(-\frac{ju}{4h}\right)\,du.
 \tag{2.3}
\]

Then the exact, boundary-explicit one-sided Poisson formula is

\[
 \boxed{\displaystyle
 \mathcal L_{X,V}(N)
 =\frac12\sum_{h\ge1}w(4h^2)
 +\frac{i}{2}\sum_{h\ge1}\sum_{\substack{j\in\mathbb Z\\j\ne0}}
 \chi _4(j)
 \left(I_{h,j}-\frac{2w(4h^2)}{\pi i j}\right).}
 \tag{2.4}
\]

The \(h\)-sum is finite, and the subtracted \(j\)-sum is absolutely
convergent. In particular,

\[
 \frac12\sum_{h\ge1}w(4h^2)\ll_V N^{-1/4}.
 \tag{2.5}
\]

5. For every \(0<\rho<1\), set

\[
 w_\rho(u)=\rho^{-u}w(u),\qquad
 \widehat w_\rho(\alpha)=\int_{\mathbb R}w_\rho(u)e(-\alpha u)\,du.
\]

There is the coefficient-preserving Abel--Fourier identity

\[
 \boxed{\displaystyle
 \mathcal L_{X,V}(N)=
 \int_{\mathbb R}\widehat w_\rho(\alpha)
 \mathscr F(\rho e(\alpha))\,d\alpha.}
 \tag{2.6}
\]

Equivalently, after folding the Schwartz kernel,

\[
 \mathcal L_{X,V}(N)=\int_0^1K_\rho(\beta)
 \mathscr F(\rho e(\beta))\,d\beta,
 \qquad
 K_\rho(\beta)=\sum_{\ell\in\mathbb Z}
 \widehat w_\rho(\beta+\ell).
 \tag{2.7}
\]

No limiting interchange at \(|z|=1\) is needed in (2.6).
Moreover, define
\[
 \tau_{\rho,\alpha}=2\alpha-\frac{i}{\pi}\log\rho,
 \qquad e^{\pi i\tau_{\rho,\alpha}}=\rho e(\alpha).
\]
Combining (2.2K) with (2.6) gives the exact radial-Appell representation
\[
 \boxed{\displaystyle
 \mathcal L_{X,V}(N)=\frac12\int_{\mathbb R}
 \widehat w_\rho(\alpha)
 \mathscr K_4\!\left(\tau_{\rho,\alpha},
 \frac{\tau_{\rho,\alpha}}8,
 \frac12-\frac{\tau_{\rho,\alpha}}8\right)d\alpha.}
 \tag{2.8}
\]
Thus modular use would have to be uniform on an entire horizontal
\(\tau\)-line and on its moving elliptic path, not merely at one fixed
Appell specialization.

## 3. Proof or derivation

For the generating identity, put \(k=q-4h\). The strict inequality
\(q>4h\) is exactly \(k\ge1\); since \(4h\equiv0\pmod4\), \(k\) is odd and
\(\chi _4(q)=\chi _4(k)\). Also \(hq=4h^2+hk\), proving the coefficient
identity (2.1). Summing the positive odd \(k\)'s gives

\[
 \sum_{k\ge1\ {\rm odd}}\chi _4(k)z^{hk}
 =\sum_{r\ge0}\bigl(z^{h(4r+1)}-z^{h(4r+3)}\bigr)
 =\frac{z^h}{1+z^{2h}},
\]

which proves the boxed identity in the packet.

To prove (2.2), pair \((h,k)\) with \((-h,-k)\). The quadratic value is
unchanged, \(\chi _4(-k)=-\chi _4(k)\), and the sign sum changes sign.
Thus the two members of a negative/positive pair make two equal
half-contributions. Opposite-sign pairs have zero sign kernel. This also
proves convergence and exposes the null \(h=0\) edge; the bilinear-form
calculation in Section 2 verifies the claimed signature data directly.
The termwise substitutions and positive/negative-index pairing in item 3
prove (2.2A)--(2.2K); absolute convergence justifies that pairing.

For Poisson summation, fix \(h\) and write

\[
 W_h(t)=w(h(4h+t))\quad(t\ge0),\qquad
 S_h=\sum_{k\ge1}\chi _4(k)W_h(k).
\]

Extend \(W_h\) by zero to \(t<0\), using the symmetric value at \(0\), and
denote its Fourier transform on the half-line by

\[
 \widehat H_h(\xi)=\int_0^\infty W_h(t)e(-\xi t)\,dt.
\]

Poisson summation in the two residue classes modulo \(4\) uses the exact
Gauss sum

\[
 \sum_{a\bmod4}\chi _4(a)e(aj/4)=2i\chi _4(j)
\]

and yields, initially in symmetric summation,

\[
 S_h=\frac{i}{2}\sum_{j\in\mathbb Z}\chi _4(j)
 \widehat H_h(j/4).
 \tag{3.1}
\]

Integration by parts gives, for \(j\ne0\),

\[
 \widehat H_h(j/4)=\frac{2W_h(0)}{\pi i j}+O_{W_h}(j^{-2}).
\]

Since

\[
 \sum_{j\in\mathbb Z\setminus\{0\}}\frac{\chi _4(j)}j
 =2\sum_{j\ge1}\frac{\chi _4(j)}j
 =2\sum_{r\ge0}\frac{(-1)^r}{2r+1}=\frac\pi2.
\]

because \(\chi _4(-j)=-\chi _4(j)\), so
\(\chi _4(-j)/(-j)=\chi _4(j)/j\). Hence the extracted leading term in
(3.1) is
\[
 \frac{i}{2}\frac{2W_h(0)}{\pi i}\frac{\pi}{2}
 =\frac{W_h(0)}2,
\]
with positive sign. Finally,

\[
 \widehat H_h(j/4)
 =\frac1h\int_{4h^2}^\infty
 w(u)e\!\left(-\frac{ju}{4h}\right)du=I_{h,j};
\]

the factor \(e(jh)\) from the change of variables is \(1\). Summing over
the finitely many possible \(h\) proves (2.4). Estimate (2.5) follows
because \(4h^2\asymp N\) on the support: there are \(O(\sqrt N)\) such
\(h\), and every summand is \(O_V(N^{-3/4})\).

For (2.6), Fourier inversion gives

\[
 \int_{\mathbb R}\widehat w_\rho(\alpha)e(\alpha n)d\alpha
 =w_\rho(n)=\rho^{-n}w(n).
\]

Expanding the absolutely convergent \(\mathscr F(\rho e(\alpha))\) and
interchanging sum and integral therefore gives exactly
\(\sum_n\mathcal D(n)w(n)\). Splitting the real line into unit intervals
proves (2.7). Notice that replacing \(w_\rho\) by \(w\) would leave an
incorrect factor \(\rho^n\); this is the required Abel correction.
Substitution of (2.2K) into (2.6) gives (2.8), because Fourier inversion
also gives
\[
 \int_{\mathbb R}\widehat w_\rho(\alpha)\,d\alpha=w_\rho(0)=0;
\]
the \(-1/4\) completion constant therefore contributes exactly zero.

It remains to audit what (2.4) does to the square-root phase. The phase in
\(I_{h,j}\) is

\[
 \phi_{h,j}(u)=\sqrt{Xu}-\frac{ju}{4h},
\]

and its stationary point is

\[
 u_0=\frac{4Xh^2}{j^2}.
\]

There is no stationary point for \(j<0\). For \(j>0\), a stationary point
in the radial support and above the cone endpoint must satisfy

\[
 2h\sqrt{\frac{X}{bN}}\ \le j\le\
 2h\sqrt{\frac{X}{aN}},\qquad j\le\sqrt X.
 \tag{3.2}
\]

On any fixed interior subcone for which
\(v_0=u_0/N\) stays in a compact subset of the interior of the support and
\(4h^2/N\) stays a fixed distance below it, ordinary uniform stationary
phase gives

\[
 I_{h,j}=\frac{2X^{-1/4}}h
 V(v_0)e(Xh/j-1/8)
 +O_V\!\left(\frac{X^{-1/4}}h(XN)^{-1/2}\right).
 \tag{3.3}
\]

Indeed, after \(u=Nv\), the large parameter is
\(\lambda=\sqrt{XN}\); the factor \(v_0^{-3/4}\) in the amplitude cancels
the \(v_0^{3/4}\) from \(|\phi''(v_0)|^{-1/2}\). Explicitly, the phase in
\(v\) is \(\lambda f(v)\), where
\[
 f(v)=\sqrt v-\frac{j\sqrt N}{4h\sqrt X}v,\qquad
 f''(v_0)=-\frac1{4v_0^{3/2}}.
\]
The \(e(t)=e^{2\pi it}\) stationary-phase factor is
\[
 e(-1/8)\bigl(\lambda|f''(v_0)|\bigr)^{-1/2}
 =2e(-1/8)\lambda^{-1/2}v_0^{3/4}.
\]
Multiplication by the outside amplitude
\(h^{-1}N^{1/4}V(v_0)v_0^{-3/4}\) gives exactly
\[
 \frac2hN^{1/4}(XN)^{-1/4}V(v_0)e(-1/8)
 =\frac{2X^{-1/4}}hV(v_0)e(-1/8),
\]
confirming both the constant and sign in (3.3). Equation (3.3), inserted
in (2.4), is the reciprocal cone displayed in Section 1. If \(V\) is
nonzero on an interval, one may take \(h\asymp\sqrt N\) in a sufficiently
small fixed range below the endpoint. There are
\(\asymp h\sqrt{X/N}\) admissible odd \(j\)'s for each such \(h\). Hence
the sum of the magnitudes of the stationary main terms is

\[
 X^{-1/4}\sum_{h\asymp\sqrt N}
 \frac{h\sqrt{X/N}}h\asymp X^{1/4}.
 \tag{3.4}
\]

Thus the needed saving is cancellation in a new two-variable sum, not a
consequence of the transform.

The same obstruction is visible in (2.6). Taking
\(\rho=e^{-1/N}\) and \(u=Nv\) gives

\[
 \widehat w_\rho(\alpha)=N^{1/4}\int
 V(v)e^v v^{-3/4}
 e\bigl(\sqrt{XN}\sqrt v-\alpha Nv\bigr)\,dv.
 \tag{3.5}
\]

Its stationary band has length \(\asymp\sqrt{X/N}\), and interior
stationary phase has magnitude \(\asymp X^{-1/4}\). For fixed nonzero
\(V\), therefore, as \(XN\to\infty\),

\[
 \|\widehat w_\rho\|_1\asymp_V X^{1/4}N^{-1/2}
 \tag{3.6}
\]

up to harmless fixed-support endpoint constants. An additive-phase
estimate inserted pointwise into (2.6) necessarily pays this explicit
Fourier/Abel mass unless it also exploits cancellation in the folded
kernel \(K_\rho\). The same mass is present in the exact Appell integral
(2.8); the Appell name alone does not remove it.
For \(\rho=e^{-1/N}\),
\[
 {\rm Im}\,\tau_{\rho,\alpha}=\frac1{\pi N},
\]
while the stationary \(\alpha\)-band in (3.5) has length
\(\asymp\sqrt{X/N}\). It therefore traverses
\(\asymp\sqrt{X/N}\) unit additive-phase periods before folding.
A modular treatment local to the zero cusp is not uniform on this radial
integral; one must either resolve all folded cusp pieces with their
corrections or prove cancellation among them.

## 4. First doubtful or unproved step

All identities (2.1)--(2.8), the explicit boundary term, and the interior
stationary-phase reduction are proved above. The first unproved step
toward the requested bound is a uniform cancellation estimate for

\[
 \sum_{\substack{h,j>0\\(h,j)\ {\rm in}\ (3.2)}}
 \frac{\chi _4(j)}h
 V\!\left(\frac{4Xh^2}{j^2N}\right)e(Xh/j),
\]

together with uniform treatment of the support endpoints and the
coalescence \(j=\sqrt X\) of the stationary point with \(u=4h^2\).
Neither the character nor stationary phase alone supplies this
cancellation. Although (2.2A)--(2.2K) are exact Appell completions under
the packet's conventions, using a modular transformation for that Appell
sum would require an exact theorem and an audit of the non-closed
parameter orbit (2.2S) and every Mordell/null-edge correction. No such
transformation theorem is assumed or proved here. Therefore no estimate
of the form (63.2), and no radial interval on which it holds, is claimed.

## 5. Required control test and outcome

**Coefficient and strict-boundary test.** The \(h=1\) contribution is
\(z^5-z^7+z^9-z^{11}+\cdots\), corresponding exactly to
\(q=5,7,9,11,\ldots>4\); the \(h=2\) contribution begins
\(z^{18}-z^{22}+\cdots\), corresponding to \(q=9,11,\ldots>8\).
Thus neither \(q=4h\) nor an incorrect weak inequality has entered.

**Poisson boundary test.** For the decaying diagnostic
\(W(t)=e^{-ct}\), \(c>0\), the original one-sided character sum is

\[
 \sum_{k\ge1}\chi _4(k)e^{-ck}
 =\frac{e^{-c}-e^{-3c}}{1-e^{-4c}}=\frac1{2\cosh c}.
\]

As \(c\downarrow0\) this tends to \(1/2\). In (2.4) the extracted term is
exactly \(W(0)/2=1/2\), while the absolutely convergent residual tends to
zero. This confirms the sign and size of the otherwise easy-to-miss
half-boundary correction.

**Cusp test.** Directly from the proved identity, a Riemann-sum limit gives

\[
 \mathscr F(e^{-t})\sim\frac{\sqrt\pi}{8\sqrt t}
 \qquad(t\downarrow0),
\]

because \(\sqrt t\) times the \(h\)-sum tends to
\(\frac12\int_0^\infty e^{-4y^2}dy\). Thus at
\(\rho=e^{-1/N}\) the zero cusp has size \(\asymp\sqrt N\). Combining a
hypothetical uniform pointwise bound of this cusp size with (3.6) would
have capacity \(X^{1/4}\), not \(X^\varepsilon\).

**Bilateral convention control.** The exact calculations after (2.2)
show that \(\mathscr K_4(\tau,0,1/2)\) collapses to
\(\frac12+\sum_{h\ge1}z^{4h^2}\), while the \(A_4\) specialization and the
corrected
\(\mathscr K_4(\tau,\tau/8,1/2-\tau/8)\) specialization both equal
\(\frac12+2\mathscr F(z)\). Outcome: the first identification is false,
whereas the corrected ones are coefficient-preserving only after the
exact factor \(1/2\) and subtraction \(1/4\) in (2.2A)--(2.2K). Their
moving, non-closed elliptic path and any Mordell correction remain
mandatory in modular use.

**Perfect-fourth-power coherence test.** If \(X=T^4\) with
\(T\in\mathbb Z\), then for every integer \(s\),

\[
 e(\sqrt{Xs^2})=e(T^2s)=1.
\]

In particular the Poisson boundary squares \(4h^2\) are completely
coherent. Their total is nevertheless only \(O_V(N^{-1/4})\) by (2.5),
so this test does not refute the target; it does show that rational/integer
cusps cannot be discarded by a generic-irrational-phase argument. The
bulk reciprocal cone remains the genuine unresolved control.

No numerical result is used in any conclusion.

## 6. Dependencies and exact artifacts used (strict isolation ledger)

The only pre-existing repository artifact read was
rounds/codex-managed/m9-m1-one-sided-divisor-false-theta/derivation_packet.md,
first in its original form and then again after the conductor authorized
the convention-control additions (63.4)--(63.7).
The assignment message supplied the output contract and isolation rule.
I did not open the claim graph, proof draft, protocol, active-campaign
state, prior reports or syntheses, any other brief, any legacy round, or
any source/literature material. No theorem was imported from the web.
The newly written report itself was reread only for formatting and
consistency checks. One optional local numerical diagnostic was attempted,
but no Python interpreter was available, so it produced no numerical
result and was not used. No computational artifact or prior calculation
was used. The only file written is this report.

## 7. Recommended state effect

**Promote, but only as a scoped exact reduction:** promote the verification
of (63.3), the degenerate sign-kernel formula (2.2), the audited Appell
identities (2.2A)--(2.2K), and the boundary-explicit Poisson and
Abel--Fourier identities (2.4) and (2.6).
**Retain unresolved** the square-root-phase estimate. Reject any inference
that the appearance of (63.3), or a pointwise additive-phase/modular bound,
already proves (63.2). The report supplies no new exponent, no lower-radial
closure, and no authorization for a shared-state change.

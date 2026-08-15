# Blind M1 frequency phase diagram

- Campaign: `m9-m1-frequency-phase-diagram`
- Round: 10
- Task: `blind_m1_phase_diagram`
- Role: statement-only parameter deriver
- Isolation: no other Round-10 report was read
- Status: candidate evidence only; no shared proof state was edited

## 1. Result

Let

\[
B_1(D,L;X)=
\sum_{h\asymp L}\frac{\Phi(h/(H_D+1))}{h}
\sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d),
\qquad H_D\asymp DX^{-1/4},
\]

where the denominator profile is one of the fixed-BV profiles in the
authorized packet and the notation \(h\asymp L\) includes a fixed-BV
dyadic frequency cutoff. Uniformly in the active range, the following
direct estimates hold (powers of \(\log X\) are absorbed in \(X^\varepsilon\)):

\[
\tag{A}\label{A}
B_1(D,L;X)\ll 1+\min\left(D,\frac{LX}{D}\right),
\]

by summation by parts against the bounded partial sums of \(\chi _4\);

\[
\tag{G}\label{G}
B_1(D,L;X)\ll_\varepsilon X^\varepsilon
\left(1+\frac DL\right),
\]

by summing the actual frequency block first and using the divisor bound;
and, for any certified exponent pair \((\kappa,\lambda)\),

\[
\tag{EP}\label{EP}
B_1(D,L;X)\ll_\varepsilon
X^\varepsilon X^\kappa L^\kappa D^{\lambda-2\kappa}.
\]

The second-derivative estimate, retained separately because it has a useful
endpoint not captured by the certified modern pair, is

\[
\tag{V2}\label{V2}
B_1(D,L;X)\ll
\left(\frac{LX}{D}\right)^{1/2}
+\left(\frac{D^3}{LX}\right)^{1/2}.
\]

With the accepted Tao--Trudgian--Yang pair

\[
(\kappa,\lambda)=\left(\frac{89}{1282},\frac{997}{1282}\right),
\]

\eqref{EP} proves the desired \(X^{1/4+\varepsilon}\) estimate precisely
on the certified wedge

\[
\boxed{178\ell+1638\delta\le 463.}
\]

The geometric estimate \eqref{G} proves the terminal line
\(\ell=\delta-1/4\), and \eqref{V2} additionally proves the isolated
point \((\delta,\ell)=(1/2,0)\). Estimate \eqref{A} adds only the bottom
point/edge \(\delta=1/4\), already contained in the exponent-pair wedge.
Consequently these direct methods do **not** prove all of M1. Their exact
uncovered set is

\[
\boxed{
\mathcal U_1=
\left\{(\delta,\ell):
\frac14\le\delta\le\frac12,
\ 0\le\ell<\delta-\frac14,
\ 178\ell+1638\delta>463
\right\}
\setminus\left\{\left(\frac12,0\right)\right\}.}
\]

Here “exact” means exact relative to the proved direct estimates above,
not a theorem that no other method can work. In particular, the hard top
denominator profile \(D=X^{1/2}\) is proved on its terminal frequency block
\(L\asymp X^{1/4}\) and on its bounded-frequency point \(L=X^{o(1)}\), but
its middle-frequency blocks \(0<\ell<1/4\) remain open. The first missing
input is a bound with genuine cancellation jointly in \(h,d\), or an
equivalent post-transform signed product-phase estimate, that improves on
both \(D/L\) and the exponent-pair bound in \(\mathcal U_1\).

## 2. Exact statement and hypotheses

Assume \(X\) is sufficiently large and

\[
X^{1/4}\le D\le X^{1/2},\qquad
1\le L\ll H_D,\qquad H_D=\lfloor DX^{-1/4}\rfloor
\]

(changing the height by fixed absolute factors has no effect on the
statements). Write

\[
D=X^\delta,\qquad L=X^\ell,
\qquad \frac14\le\delta\le\frac12,
\qquad 0\le\ell\le\delta-\frac14.
\]

The profile \(w_D\) is real, supported on a fixed shell \(d\asymp D\),
bounded by an absolute constant, and has uniformly bounded discrete BV
norm. This includes every interior active profile and the one-sided hard
top profile from the authorized profile rederivation. The hard top profile
need not be continuum smooth.

Insert a fixed dyadic cutoff \(v_L(h)\) into \(h\asymp L\). The actual
frequency coefficient

\[
a_{L,H}(h)=v_L(h)\frac{\Phi(h/(H+1))}{h}
\]

satisfies

\[
\tag{2.1}
\sup_h|a_{L,H}(h)|+
\sum_h|a_{L,H}(h+1)-a_{L,H}(h)|\ll L^{-1}.
\]

Indeed, \(0\le\Phi\le1\) and \(\Phi\) is monotone on \([0,1]\) in the
accepted normalization; multiplication by a fixed-BV dyadic cutoff and by
\(1/h\asymp1/L\) gives (2.1). In particular

\[
\tag{2.2}
\sum_{h\asymp L}|a_{L,H}(h)|\ll1.
\]

All estimates below are for the actual coefficient. The fixed factor
\(-1/(2\pi i)\), the outer M1 factor, and conjugate frequency merely change
absolute constants.

## 3. Proof of the direct estimates

### 3.1 Spatial-character summation by parts

The primitive character has bounded partial sums:

\[
\left|\sum_{n\le t}\chi _4(n)\right|\le1.
\]

For fixed \(h\), discrete Abel summation therefore gives

\[
\left|\sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d)\right|
\ll \|w_D e(hX/\,\cdot)\|_{\mathrm{BV}_d}.
\]

On a fixed shell,

\[
|e(hX/(d+1))-e(hX/d)|
\ll \min\left(1,\frac{hX}{D^2}\right).
\]

There are \(O(D)\) differences. Using the fixed BV norm of \(w_D\),

\[
\tag{3.1}
\sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d)
\ll 1+\min\left(D,\frac{hX}{D}\right).
\]

Summing (3.1) with (2.2), and using \(h\asymp L\), proves \eqref{A}.
In exponent notation its nontrivial branch has size
\(X^{1+\ell-\delta}\). Since
\(1+\ell-\delta\ge1-\delta\ge1/2\), that branch never reaches
\(X^{1/4}\) in the active rectangle. The trivial branch reaches the target
only when \(\delta=1/4\).

This calculation is also what results if one sums the frequency kernel
first and then uses only its total variation against \(\chi _4\): the
normalized Dirichlet kernel can vary on scale \(L\), yielding
\(1+LX/D\), not a new region.

### 3.2 Frequency-first geometric kernel

For fixed \(d\), Abel summation in \(h\), using (2.1), gives

\[
\tag{3.2}
\left|\sum_{h\asymp L}a_{L,H}(h)e(hX/d)\right|
\ll
\min\left(1,\frac{1}{L\|X/d\|}\right).
\]

Choose an integer \(m=m(d)\) nearest to \(X/d\), and put \(n=dm\).
Then, for \(d\asymp D\),

\[
d\|X/d\|=|X-n|\asymp D\|X/d\|.
\]

After preserving \(\chi _4(d)\) through (3.2), take absolute values.
For each integer \(n\asymp X\), the number of participating divisors
\(d\) is at most \(\tau(n)\ll_\varepsilon X^\varepsilon\). Hence

\[
\begin{aligned}
|B_1(D,L;X)|
&\ll_\varepsilon X^\varepsilon
\sum_{\substack{n\in\mathbb Z\\|n-X|\ll D}}
\min\left(1,\frac{D}{L|X-n|}\right)\\
&\ll_\varepsilon X^\varepsilon\left(1+\frac DL\right).
\end{aligned}
\]

The term with \(X=n\) is interpreted as \(1\). The last sum is bounded by
the \(O(D/L+1)\) closest integers plus a harmonic tail; its logarithm is
absorbed by \(X^\varepsilon\). This proves \eqref{G}. Since

\[
\frac DL=X^{\delta-\ell},
\]

it reaches \(X^{1/4+\varepsilon}\) exactly when
\(\ell\ge\delta-1/4\). The allowed height inequality is the reverse, so
this proves exactly the terminal line.

No cancellation of the spatial character was asserted after the divisor
grouping. A uniform improvement would require a new estimate for the
\(\chi _4(d)\)-weighted participating divisors or a genuinely bilinear
argument; the ordinary divisor bound alone cannot supply it.

### 3.3 Exponent pairs after preserving the character

Split the denominator sum into the two residue classes
\(d\equiv1,3\pmod4\). On each class \(\chi _4(d)\) is constant. After
writing \(d=4n+r\), the sampled denominator weight still has uniform BV
norm and fixed-shell support. Thus a certified exponent pair
\((\kappa,\lambda)\) for the reciprocal phase gives, uniformly for
\(h\asymp L\),

\[
\tag{3.3}
\sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d)
\ll_\varepsilon
X^\varepsilon
\left(\frac{hX}{D^2}\right)^\kappa D^\lambda.
\]

The parameter \(hX/D^2\ge1\) throughout the active range. Summing (3.3)
against the actual \(1/h\)-scale Vaaler coefficient gives

\[
|B_1(D,L;X)|
\ll_\varepsilon
X^\varepsilon X^\kappa L^\kappa D^{\lambda-2\kappa},
\]

which is \eqref{EP}. The spatial character has not been replaced by an
arbitrary coefficient: it was resolved exactly into its two constant
residue classes.

For the accepted pair \((89/1282,997/1282)\), the power of \(X\) is

\[
\frac{89(1+\ell)+819\delta}{1282}.
\]

Demanding that it be at most \(1/4\), and clearing the denominator, gives

\[
2\{89(1+\ell)+819\delta\}\le641,
\]

or exactly

\[
178\ell+1638\delta\le463.
\]

The wedge covers the complete frequency section whenever

\[
178(\delta-1/4)+1638\delta\le463,
\qquad\text{i.e.}\qquad
\delta\le\frac{1015}{3632}.
\]

It covers a nonempty bottom slice through
\(\delta\le463/1638\). These are bookkeeping consequences, not new
exponent-pair claims.

### 3.4 The second-derivative endpoint

Again split into the two odd residue classes so the amplitude has fixed
BV. On a shell \(d\asymp D\), the reciprocal phase satisfies

\[
\left|\frac{d^2}{dd^2}\frac{hX}{d}\right|
\asymp\frac{hX}{D^3}.
\]

The van der Corput second-derivative estimate and partial summation of the
fixed-BV amplitude give

\[
\sum_{d\asymp D}\chi _4(d)w_D(d)e(hX/d)
\ll
\left(\frac{hX}{D}\right)^{1/2}
+\left(\frac{D^3}{hX}\right)^{1/2}.
\]

Averaging this over \(h\asymp L\) with coefficients of size \(1/L\)
proves \eqref{V2}. The two powers are at most \(X^{1/4}\) only if

\[
\ell\le\delta-\frac12,
\qquad
\ell\ge3\delta-\frac32.
\]

Inside the active rectangle the first inequality forces
\((\delta,\ell)=(1/2,0)\), and the second then holds with equality. Thus
this method contributes exactly that isolated endpoint (up to
\(X^\varepsilon\), so \(L=X^{o(1)}\) is harmless).

A first-derivative test gives no additional uniform region. After resolving
the character into residue classes, the phase derivative can approach an
integer/stationary dual frequency inside the shell. Excluding such points
would be an extra Diophantine hypothesis not present here; treating them
leads to the already open transformed cone rather than a direct estimate.

## 4. Region synthesis and no-go calculation for the direct menu

The allowed parameter triangle is

\[
\frac14\le\delta\le\frac12,qquad
0\le\ell\le\delta-\frac14.
\]

Within it:

1. spatial Abel/trivial estimation supplies only \(\delta=1/4\);
2. the geometric kernel supplies exactly \(\ell=\delta-1/4\);
3. the TTY pair supplies \(178\ell+1638\delta\le463\);
4. the second-derivative estimate supplies \((1/2,0)\).

Their complement is exactly \(\mathcal U_1\) stated in Section 1. It is
nonempty. For example, at \((\delta,\ell)=(3/8,0)\), the spatial and
frequency-first bounds are at least \(X^{3/8}\), the first V2 term is
\(X^{5/16}\), and the TTY exponent is

\[
\frac{89+819(3/8)}{1282}>\frac14.
\]

Thus no selection or interpolation among these upper bounds proves the
whole M1 range. An interpolation of two failed pointwise upper bounds
cannot improve below their minimum without a new norm or correlation
input.

## 5. Hard top profile versus smooth interior profiles

All four direct arguments use only boundedness and discrete BV of \(w_D\),
not continuum differentiability. They therefore apply unchanged to the
hard one-sided top profile

\[
w_0(d)=\mathbf 1_{d\le y}W(d/y),\qquad y=\lfloor\sqrt X\rfloor.
\]

No smoothing/unsmoothing transfer is needed for these statements. At
\(D=X^{1/2}\):

- \(L\asymp H_D\asymp X^{1/4}\) is closed by \eqref{G};
- bounded or subpolynomial \(L\) is closed by \eqref{V2};
- \(X^\eta\ll L\ll X^{1/4-\eta}\) lies in \(\mathcal U_1\) for fixed
  \(\eta>0\).

The exact one-sided transform in the graph remains useful structural
information, but it is not needed to prove the terminal frequency block.
It does not by itself close the middle-frequency hard-top blocks, because
those become the still-open signed product-phase cone.

## 6. Required controls and outcomes

### Both frequency signs: pass

For real \(w_D\), the negative-frequency block is the complex conjugate of
the positive-frequency block after restoring the audited Vaaler
coefficient. All norm estimates are unchanged. Directly, replacing
\(h\) by \(-h\) also leaves \(\|X/d\|\), the derivative magnitudes, and
the exponent-pair scale unchanged.

### \(L=1\): pass, with an exposed gap

The coefficient mass is \(O(1)\). TTY proves the target for
\(\delta\le463/1638\), and V2 proves it at \(\delta=1/2\). The interval

\[
463/1638<\delta<1/2
\]

remains uncovered at bounded frequency. At \(\delta=1/4\), all elementary
bounds are already target-sized.

### \(L\asymp H_D\): pass

Here \(\ell=\delta-1/4\), so

\[
D/L\asymp X^{1/4}.
\]

The geometric estimate proves the desired bound for every active \(D\),
including the hard top profile.

### \(D=X^{1/4}\): pass

Here \(H_D\asymp1\), hence only \(L\asymp1\) occurs. The trivial bound
\(|B_1|\ll D=X^{1/4}\) and the geometric bound both close the block.

### \(D=X^{1/2}\): partial pass

Here \(H_D\asymp X^{1/4}\). The terminal frequency and bounded-frequency
point pass as described above. Exactly the exponent-plane interval
\(0<\ell<1/4\) remains uncovered by the direct menu.

### Exact-square \(X\): pass without an artificial separation assumption

If \(X\) is an integer square, exact resonances \(X=dm\) can occur in the
frequency-first argument. They contribute the value \(1\) in (3.2) and
are counted with multiplicity at most \(\tau(X)\ll_\varepsilon
X^\varepsilon\). The V2 and exponent-pair bounds are uniform in the
arithmetic nature of \(X\). Thus exact squares create no failure in the
proved regions, but they also yield no cancellation closing
\(\mathcal U_1\).

### Normalization powers: pass

The four relevant powers are

\[
\begin{array}{c|c}
\text{method}&\text{power of }X\\ \hline
\text{spatial Abel, oscillatory branch}&1+\ell-\delta\\
\text{frequency geometric}&\delta-\ell\\
\text{exponent pair}&\kappa(1+\ell)+(\lambda-2\kappa)\delta\\
\text{V2 terms}&(1+\ell-\delta)/2,\ (3\delta-1-\ell)/2.
\end{array}
\]

All include the \(L\) frequencies and their actual \(1/L\)-scale Vaaler
weight. No factor \(L\), \(D\), or \(X^{1/4}\) is omitted.

## 7. First doubtful or unproved step

There is no doubtful step in the elementary bounds or the exponent
arithmetic. Formula \eqref{EP} depends on the already accepted certified
exponent-pair interface and its normalized-BV partial-summation transfer;
this report does not re-audit the primary source.

The first genuinely unproved mathematical step is any improvement in
\(\mathcal U_1\). One needs, for example, a uniform estimate of the shape

\[
B_1(D,L;X)\ll_\varepsilon X^{1/4+\varepsilon}
\qquad ((\delta,\ell)\in\mathcal U_1),
\]

using correlation between the spatial \(\chi _4(d)\) and reciprocal
phases across frequencies. Neither bounded character partial sums, the
ordinary divisor multiplicity bound, nor one-variable exponent pairs
provide that correlation. On the hard top profile this is equivalent in
difficulty to controlling the accepted signed product-phase cone after the
one-sided transform; the transform alone is not an estimate.

## 8. Exact dependencies and artifacts used

Only the brief-authorized files were read:

- `protocol.md`;
- `state/proof_obligations.yml`;
- `state/active_campaign.yml`;
- `state/best_proof_draft.md`;
- `rounds/codex-managed/m9-endpoint-kernel-validation/reports/blind_profile_rederivation.md`.

No other Round-10 report, campaign synthesis, validation matrix, or web
source was read. The only external analytic input invoked is the
Tao--Trudgian--Yang exponent pair already recorded as accepted in the
authorized proof draft.

## 9. Recommended state effect

1. **Promote the M1 direct phase diagram after conductor validation.** The
   terminal-frequency estimate holds uniformly for every actual active
   profile, including the hard top profile; the certified TTY wedge and
   isolated V2 endpoint hold with the spatial character preserved exactly.
2. **Retain `M9-M1` as open.** The exact residual corridor is
   \(\mathcal U_1\), which is nonempty.
3. **Revise the role of `M9-M1-top-endpoint-signed-cone`.** It is not needed
   for the terminal frequency block, but remains an equivalent open route
   for the hard-top middle-frequency corridor.
4. **Do not promote `M9` or the Gauss circle target.** This report proves a
   region decomposition, not the missing signed correlation estimate.

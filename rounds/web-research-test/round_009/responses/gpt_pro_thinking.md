Summary:

Source anchors: Round 9 packet and active workflow directives are in the uploaded prompt packet. The background Gauss circle survey packet is available as. I also used the local TeX source `/mnt/data/Li-Yang-arXiv-2308.14859v2.tex`, especially the source labels `\label{definition of S}`, `\label{condition on F 1}`, `\label{condition on F 2}`, `\label{main theorem}`, and `\label{goal}`.

Main outcome of this Stage A packet:

1. The Li--Yang source audit gives a negative theorem-import conclusion for the current endpoint target. Li--Yang's exponential-sum theorem is structurally relevant to our reciprocal phases, but it does **not** directly prove H5r-F, H5r-B, H5a, or H5b at the endpoint range required by the conjectural Gauss circle exponent.

2. The previous classification of H5r-F as the central open bottleneck should be revised. Assuming the Vaaler majorant H4 in its standard Fejer-kernel form, the fixed-Fejer residual H5r-F appears to be controllable by an elementary divisor-bound / short-product-interval argument:
$$
   \frac{1}{H_D}
   \sum_{d\sim D} K_{H_D}(X/d)
   \ll_\epsilon X^{1/4+\epsilon},
$$
   with analogous estimates for the shifted second-leg residuals. This would discharge the actual Vaaler residual target H5r-F without Li--Yang technology.

3. H5r-B and H5r-L1 remain much stronger and generally divisor-problem-like, but they may not be needed for the Vaaler residual. The proof route should therefore return attention to the main Vaaler sums H5a/H5b, with exact coefficient norms rather than arbitrary-coefficient overstrengthening.

Main claim or direction:

The correct Round 9 direction is:

$$
\text{do not import Li--Yang as an endpoint theorem;}
$$

instead,

$$
\text{prove the fixed-Fejer residual directly by kernel/product counting,}
$$

then reformulate the remaining main-term targets H5a/H5b at the exact fixed-coefficient norm forced by Vaaler.

The revised dependency map should become:

$$
\text{H4 Vaaler majorant}
+
\text{R5 Fejer product-count lemma}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

This would replace the earlier dependency

$$
\text{H5r-F as an open endpoint reciprocal-sum target}
\Longrightarrow
\text{Vaaler residual}\ll_\epsilon X^{1/4+\epsilon}.
$$

The central unsolved analytic targets would then be the Vaaler main terms:

$$
\sum_{1\le |h|\le H_D}\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
$$

and

$$
\sum_{1\le |h|\le H_D}\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)),
$$

with

$$
H_D\asymp D X^{-1/4},
\qquad
X^{1/4}\le D\le X^{1/2}.
$$

Detailed reasoning:

## 1. Li--Yang source audit

Li--Yang's exponential sum is defined in their TeX source at `\label{definition of S}` as

$$
S
=
\sum_{H\le h\le 2H}
g(h/H)
\sum_{M\le m\le 2M}
G(m/M)
e\left(\frac{hT}{M}F(m/M)\right),
$$

where $g,G$ are of bounded variation and $F$ is $C^3$ on $[1,2]$.

The two structural hypotheses on $F$ are, at `\label{condition on F 1}` and `\label{condition on F 2}`,

$$
C_r\ge |F^{(r)}(x)|\ge C_r^{-1}
\qquad
(r=1,2,3),
$$

and

$$
|F'(x)F'''(x)-3F''(x)^2|\ge C_4^{-1}.
$$

The theorem labelled `\label{main theorem}` is not simply a black-box endpoint theorem for all such sums. It is embedded in the Bombieri--Iwaniec/Huxley parameter structure, with Case (A), Case (B), the auxiliary parameter $N$, the range of $q$, and the condition `\label{condition 1-------}`.

The final reduction to the circle/divisor problems occurs near `\label{definition of S again}` and `\label{goal}`. There Li--Yang reduce to sums of the same broad form and need

$$
\frac{S}{H}\lesssim_\epsilon T^{\theta^*+\epsilon},
$$

where

$$
\theta^*=0.3144831759741\cdots.
$$

They use a sawtooth truncation height

$$
Y=MT^{-\theta^*},
$$

and the relevant dyadic range includes

$$
1\le H\le MT^{-\theta^*}.
$$

This is the first decisive mismatch with our endpoint Vaaler scale. In our notation $T=X$ and $M\asymp D$. The endpoint residual/main-term scale is

$$
H_D\asymp D X^{-1/4}.
$$

Since

$$
\theta^*>1/4,
$$

we have

$$
D X^{-1/4}
\gg
D X^{-\theta^*}
$$

for large $X$.

For example, at the critical block

$$
D\asymp X^{1/2},
$$

our endpoint height is

$$
H_D\asymp X^{1/4},
$$

whereas Li--Yang's final range for their exponent only reaches

$$
M X^{-\theta^*}
\asymp
X^{1/2-\theta^*}
=
X^{0.1855168\cdots}.
$$

Therefore Li--Yang's final theorem range is far below the endpoint height required by the conjectural $X^{1/4+\epsilon}$ target.

## 2. Phase dictionary: structural match but not theorem import

The H5r residual families are

$$
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d),
$$

and

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
\qquad
\rho\in\{1,3\}.
$$

For $S_\rho$, set $T=X$, $M=D$, $h=k$, and $z=d/D$. Then

$$
e(k\rho/4)e(kX/(4d))
=
e\left(\frac{kX}{D}
\left(
\frac{1}{4z}+\frac{\rho D}{4X}
\right)\right).
$$

Thus it has Li--Yang form with

$$
F_{\rho,D,X}(z)
=
\frac{1}{4z}+\frac{\rho D}{4X}.
$$

The additive constant has no effect on derivatives, and on $[1,2]$,

$$
F'F'''-3(F'')^2
=
-\frac{3}{8}z^{-6}\ne0.
$$

For $S_{\mathrm{odd}}$, write $d=2m+1$ and take $M\asymp D/2$, $z=m/M$. Then

$$
e(kX/(2m+1))
=
e\left(\frac{kX}{M}
\frac{1}{2z+1/M}\right).
$$

So the relevant phase is

$$
F_{\mathrm{odd},M}(z)=\frac{1}{2z+1/M}.
$$

This satisfies the Li--Yang derivative conditions uniformly for large $M$, since for a phase of the form

$$
F(z)=\frac{A}{Bz+C}+C_0
$$

one has

$$
F'F'''-3(F'')^2
=
-\frac{6A^2B^4}{(Bz+C)^6}.
$$

Thus H5r is structurally in the Li--Yang reciprocal phase class.

However, structural compatibility is not theorem applicability. The mismatches are:

1. Li--Yang's final range is $H\le MT^{-\theta^*}$, while our endpoint range requires $H\le MT^{-1/4}$.

2. Li--Yang proves a bound with exponent $\theta^*$, not $1/4$.

3. Li--Yang's final $S$ has bounded-variation weights $g,G$, not arbitrary coefficients $v_k$. Therefore it does not directly imply H5r-B or H5r-L1.

4. H5r-F uses a fixed Fejer average over $1\le |k|\le H_D$, while Li--Yang's theorem is dyadic in $h$. A dyadic decomposition and triangle inequality would discard possible cross-scale Fejer cancellation.

The source audit therefore supports the following lemma-bank entry.

## L9.1 Li--Yang structural compatibility but endpoint non-import

Status: proved source-audit conclusion.

The H5r residual phases can be written in Li--Yang's reciprocal-sum form

$$
e\left(\frac{hT}{M}F(m/M)\right),
$$

with $F$ satisfying Li--Yang's two derivative hypotheses. However, Li--Yang's theorem as used for the circle/divisor problems proves

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
\qquad
\theta^*=0.314483\cdots,
$$

in a range whose final truncation height is

$$
H\le MT^{-\theta^*}.
$$

It does not directly cover the endpoint Vaaler range

$$
H\le MT^{-1/4}.
$$

It also does not supply arbitrary-coefficient H5r-B or termwise H5r-L1 estimates.

## 3. Direct Fejer-kernel bound for H5r-F

The key new observation is that H5r-F should not first be converted into an arbitrary-coefficient reciprocal sum. The fixed Fejer residual has a positive kernel interpretation.

Let

$$
K_H(t)
=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt)
=
\frac{1}{H+1}
\left(
\frac{\sin \pi(H+1)t}{\sin \pi t}
\right)^2.
$$

It satisfies the standard pointwise bound

$$
K_H(t)
\ll
\min\left(H,\frac{1}{H\|t\|^2}\right),
$$

where $\|t\|$ denotes distance to the nearest integer.

After the Vaaler residual majorant, the first-leg residual on a dyadic block has the shape

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d),
$$

up to harmless absolute constants. The second-leg residuals have the shapes

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right),
\qquad
\rho\in\{1,3\}.
$$

In the endpoint setup,

$$
H=H_D\asymp D X^{-1/4},
$$

so

$$
\Delta:=\frac{D}{H}\asymp X^{1/4}.
$$

I claim the following elementary bound.

## R5. Fejer product-count bound for H5r-F

Status: proposed proved lemma, conditional only on the standard Vaaler majorant and the divisor bound.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and

$$
H\asymp D X^{-1/4}.
$$

Let $w_D$ be a nonnegative dyadic weight supported on $d\asymp D$ with $0\le w_D(d)\le 1$. Then, for every $\epsilon>0$,

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon},
$$

and, for $\rho\in\{1,3\}$,

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

Proof for the first estimate:

Using

$$
\frac{1}{H}K_H(t)
\ll
\min\left(1,\frac{1}{H^2\|t\|^2}\right),
$$

and for each $d$ choosing an integer $m$ nearest to $X/d$, we get

$$
\|X/d\|
\asymp
\frac{|X-md|}{D}
$$

unless the distance is zero, in which case the bound is interpreted by the first branch. Hence

$$
\frac{1}{H}K_H(X/d)
\ll
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right),
\qquad
\Delta=\frac{D}{H}.
$$

Summing over all possible $m$ only overcounts, so

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll
\sum_{\substack{d\sim D\\m\asymp X/D}}
\min\left(1,\frac{\Delta^2}{|X-md|^2}\right).
$$

Group by the integer product

$$
n=md.
$$

For $n\asymp X$, the number of representations $n=md$ is at most

$$
\tau(n)\ll_\epsilon X^\epsilon.
$$

Therefore the preceding expression is

$$
\ll_\epsilon
X^\epsilon
\sum_{n\asymp X}
\min\left(1,\frac{\Delta^2}{|X-n|^2}\right).
$$

The one-dimensional sum is

$$
\ll
\Delta+1,
$$

because the terms with $|X-n|\le \Delta$ contribute $O(\Delta+1)$, and the dyadic annuli

$$
2^j\Delta<|X-n|\le2^{j+1}\Delta
$$

contribute

$$
O(2^j\Delta)\cdot O(2^{-2j})
=
O(2^{-j}\Delta).
$$

Thus

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll_\epsilon
X^\epsilon(\Delta+1).
$$

Since

$$
\Delta=\frac{D}{H}\asymp X^{1/4},
$$

this gives

$$
\frac{1}{H}
\sum_{d\sim D}K_H(X/d)
\ll_\epsilon
X^{1/4+\epsilon}.
$$

The odd restriction only reduces the sum.

For the shifted second-leg estimate, the condition that

$$
\left\|\frac{X/d+\rho}{4}\right\|
$$

is small is equivalent, up to fixed constants, to

$$
|X-md|
$$

being small for an integer

$$
m\equiv -\rho \pmod 4.
$$

The same divisor-bound argument applies, with a congruence restriction on $m$ that can only reduce the count.

This proves R5.

## 4. R5 implies H5r-F and the Vaaler residual bound

The H5r-F nonzero-frequency target was stated as

$$
\left|
\frac1H
\sum_{1\le |k|\le H}
\eta_{k,H}S_\star(k,D)
\right|
\ll_\epsilon
X^{1/4+\epsilon},
$$

where

$$
\eta_{k,H}=1-\frac{|k|}{H+1}.
$$

For the first residual family,

$$
S_\star(k,D)
=
S_{\mathrm{odd}}(k,D)
=
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)e(kX/d).
$$

Including the zero mode gives

$$
\frac1H
\sum_{|k|\le H}
\eta_{k,H}S_{\mathrm{odd}}(k,D)
=
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d).
$$

Therefore

$$
\left|
\frac1H
\sum_{1\le |k|\le H}
\eta_{k,H}S_{\mathrm{odd}}(k,D)
\right|
\le
\frac1H
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
+
\frac{1}{H}S_{\mathrm{odd}}(0,D).
$$

By R5, the first term is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

The zero term is

$$
\frac{D}{H}\asymp X^{1/4}.
$$

Hence H5r-F follows for the first residual family.

The same argument applies to

$$
S_\rho(k,D)
=
e(k\rho/4)
\sum_{d\sim D}w_D(d)e(kX/(4d)),
$$

because

$$
\sum_{|k|\le H}
\eta_{k,H}S_\rho(k,D)
=
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right).
$$

Thus R5 proves H5r-F for both residual families.

Consequently, assuming the Vaaler theorem H4 in the Fejer-majorant form, the total Vaaler residual over dyadic blocks is

$$
\ll_\epsilon X^{1/4+\epsilon}.
$$

The logarithmic number of dyadic $D$-blocks is absorbed into $X^\epsilon$.

## 5. Consequence for the research state

This changes the bottleneck diagnosis.

Previous rounds treated

$$
\text{H5r-F}
$$

as the central minimal residual bottleneck. R5 suggests that H5r-F is not the right hard target. It is the right formal target, but it may be provable by elementary product-counting once one uses the Fejer kernel directly rather than expanding it into arbitrary dyadic coefficient sums.

The stronger estimates

$$
\text{H5r-B}
$$

and

$$
\text{H5r-L1}
$$

remain hard and divisor-like, but R5 indicates they are unnecessary for controlling the actual fixed Fejer residual.

Thus the remaining hard analytic tasks should be:

1. verify H4 exactly from a standard Vaaler reference;
2. insert R5 into the proof draft;
3. reformulate H5a/H5b at the exact fixed-coefficient norm;
4. audit Li--Yang only for those fixed-coefficient main sums, not for H5r-B/L1.

## 6. H5r-F versus H5r-B/L1

Round 8's Abel identity remains correct:

For one-sided positive frequencies and

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac{1}{H+1}
\sum_{j=1}^{H}A(j).
$$

This proves that a proof of H5r-F based only on uniform partial-sum bounds for $A(j)$ may inherit an H5r-B-type difficulty.

But it does **not** prove that H5r-F is equivalent to H5r-B. Simple model sequences show non-equivalence.

If

$$
a_k=(-1)^k,
$$

then

$$
\sum_{k\le H}\eta_{k,H}a_k=O(1),
$$

while

$$
\sum_{k\le H}|a_k|=H.
$$

Thus fixed Fejer averaging may be much smaller than L1.

If

$$
a_k=1,
$$

then

$$
\sum_{k\le H}\eta_{k,H}a_k\asymp H,
$$

and the fixed Fejer average behaves like L1.

For the actual residual sums, R5 gives a direct reason the fixed Fejer average is controlled: it is a positive kernel measuring near-products $md\approx X$, and the divisor bound controls those near-products at the endpoint scale.

Dependencies:

1. H1--H3: proved balanced arithmetic reduction.

The proof still begins from

$$
P(X)
=
-4\sum_{a\le y}\chi_4(a)\psi(X/a)
+
4\sum_{b\le y}
\left[
\psi\left(\frac{X/b+1}{4}\right)
-
\psi\left(\frac{X/b+3}{4}\right)
\right]
+
O(1),
$$

with

$$
y=\lfloor X^{1/2}\rfloor.
$$

2. H4: standard Vaaler majorant.

Needed form:

$$
\psi(t)
=
\sum_{1\le |h|\le H}\alpha_h e(ht)+R_H(t),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

and

$$
|R_H(t)|
\le
\frac{C}{H}K_H(t)
$$

with

$$
K_H(t)=
\sum_{|k|\le H}
\left(1-\frac{|k|}{H+1}\right)e(kt).
$$

The exact constant and coefficient formula still need reference verification. R5 only needs the majorant form.

3. Divisor bound.

The proof of R5 uses

$$
\tau(n)\ll_\epsilon n^\epsilon.
$$

A restricted divisor count with congruence conditions is no larger.

4. Nonnegative dyadic partition.

The residual proof should choose $w_D\ge0$. If the existing smooth partition has signed weights, replace it by a nonnegative partition or apply the argument to $|w_D|$.

5. Li--Yang source theorem.

The audit uses the actual TeX source definitions of $S$, the $F$ hypotheses, and the final target $S/H\lesssim_\epsilon T^{\theta^*+\epsilon}$.

Potential gaps:

1. Exact Vaaler normalization remains unverified.

R5 proves the residual bound once the Fejer majorant is available. The repo still needs a precise imported theorem statement, including whether the majorant is

$$
(2H+2)^{-1}K_H(t)
$$

or differs by a harmless absolute constant.

2. R5 needs to be inserted carefully into both legs.

The first leg uses

$$
K_H(X/d)
$$

with odd support from $|\chi_4(d)|$.

The second leg uses

$$
K_H\left(\frac{X/d+1}{4}\right)
$$

and

$$
K_H\left(\frac{X/d+3}{4}\right).
$$

The proof draft must track both signs and both shifts.

3. R5 controls fixed Fejer residuals, not arbitrary coefficient residuals.

The lemma does not prove H5r-B or H5r-L1. Those should be kept only as stress-test norms or stronger sufficient estimates, not as required dependencies.

4. The product-count proof uses only the divisor bound and may lose $X^\epsilon$.

This is acceptable for the conjectural $X^{1/4+\epsilon}$ target, but constants and small-$X$ cases should be handled separately.

5. Li--Yang compatibility for main terms is still incomplete.

H5a/H5b with exact Vaaler coefficients may have bounded-variation frequency weights, but H5a has $\chi_4(d)$ in the denominator variable and H5b has $\chi_4(h)$ in the frequency variable. Residue splitting can transform them into finite combinations of reciprocal phases, but the endpoint height remains outside Li--Yang's proven range.

6. The main-term coefficient norm is overstrengthened in the current H5a/H5b.

The existing H5a/H5b targets allow arbitrary bounded $u_h$. The actual Vaaler main terms have structured coefficients $\alpha_h\asymp 1/h$. The next proof draft should distinguish fixed-coefficient targets from arbitrary-coefficient stress tests.

Counterexample or obstruction search:

1. Parameter obstruction to importing Li--Yang.

At the endpoint block

$$
D\asymp X^{1/2},
$$

our Vaaler height is

$$
H_D\asymp X^{1/4}.
$$

Li--Yang's final circle/divisor range for their exponent has

$$
H\le M X^{-\theta^*}
\asymp
X^{1/2-\theta^*}
=
X^{0.1855\cdots}.
$$

Thus Li--Yang's final theorem does not cover the top part of the endpoint Vaaler frequency range.

2. Coefficient obstruction to importing Li--Yang as H5r-B.

Li--Yang's $S$ has bounded-variation weights $g(h/H),G(m/M)$. It does not allow arbitrary signs $v_k$ with no variation control. Therefore it cannot imply H5r-B or L1.

3. Fejer/L1 non-equivalence model.

The sequence $a_k=(-1)^k$ has small fixed Fejer average but large L1. Therefore H5r-F is logically weaker than H5r-L1.

4. Fejer no-cancellation model.

The sequence $a_k=1$ has fixed Fejer average comparable to L1. Thus H5r-F is not automatically easier unless the arithmetic structure is used.

5. Product-count spike test.

The worst Fejer spikes occur when $X/d$ or $(X/d+\rho)/4$ is close to an integer. R5 shows that such spikes correspond to near-products

$$
md\approx X
$$

in an interval of width

$$
\Delta=D/H\asymp X^{1/4}.
$$

The divisor bound controls the number of such products by

$$
O_\epsilon(X^{1/4+\epsilon}).
$$

This should be numerically stress-tested for $X$ with unusually many divisors and for near-square $X$.

Useful lemmas:

## Lemma R5: Fixed-Fejer residual via product counting

Status: proposed proved lemma.

Let $X\ge2$, $X^{1/4}\le D\le X^{1/2}$, and $H\asymp D X^{-1/4}$. Then

$$
\frac{1}{H}
\sum_{\substack{d\sim D\\2\nmid d}}
w_D(d)K_H(X/d)
\ll_\epsilon X^{1/4+\epsilon},
$$

and

$$
\frac{1}{H}
\sum_{d\sim D}
w_D(d)
K_H\left(\frac{X/d+\rho}{4}\right)
\ll_\epsilon X^{1/4+\epsilon},
\qquad
\rho\in\{1,3\}.
$$

This proves H5r-F for the Vaaler residual families.

## Lemma L9.1: Li--Yang structural compatibility but endpoint non-import

Status: proved source-audit lemma.

The H5r, H5a, and H5b phases can be put into Li--Yang's reciprocal phase form after residue splitting and phase-shift bookkeeping. But Li--Yang's theorem, as used in their final reduction, applies to the range

$$
H\le MT^{-\theta^*},
$$

and proves

$$
S/H\lesssim_\epsilon T^{\theta^*+\epsilon},
$$

with

$$
\theta^*=0.314483\cdots.
$$

It does not supply the endpoint range

$$
H\le MT^{-1/4}
$$

or the endpoint exponent $1/4$.

## Lemma R4: Abel identity for Fejer weights

Status: proved diagnostic.

For

$$
A(j)=\sum_{1\le k\le j}a_k,
$$

one has

$$
\sum_{k=1}^{H}
\left(1-\frac{k}{H+1}\right)a_k
=
\frac{1}{H+1}
\sum_{j=1}^{H}A(j).
$$

This explains why partial-sum-only proofs of H5r-F may inherit H5r-B-type difficulty, but it does not prove equivalence.

## Lemma M9: Exact main-term norm reformulation needed

Status: proposed next lemma.

Replace arbitrary-coefficient H5a/H5b by fixed Vaaler coefficient versions.

For H5a, the actual target should involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h
\sum_{d\sim D}\chi_4(d)w_D(d)e(hX/d),
\qquad
|\alpha_h|\ll |h|^{-1},
$$

not arbitrary $u_h$ unless the proof explicitly needs the stronger form.

For H5b, the actual target should involve

$$
\sum_{1\le |h|\le H_D}
\alpha_h\chi_4(h)
\sum_{d\sim D}w_D(d)e(hX/(4d)).
$$

The arbitrary-coefficient versions remain stress tests, not minimal dependencies.

What should be tested next:

1. Verify H4 from a standard Vaaler reference.

Record the exact coefficient formula, the exact Fejer majorant, and the discontinuity convention. The proof only needs

$$
|R_H(t)|\ll H^{-1}K_H(t).
$$

2. Insert R5 into `state/best_proof_draft.md`.

Replace H5r-F as an open target with R5 as a conditional proved residual lemma, pending H4 reference verification.

3. Numerically test R5.

For square, nonsquare, divisor-rich, and near-square $X$, compute

$$
\frac{1}{H_D}\sum_{d\sim D}K_{H_D}(X/d),
$$

and

$$
\frac{1}{H_D}
\sum_{d\sim D}K_{H_D}\left(\frac{X/d+\rho}{4}\right).
$$

Compare with $X^{1/4}$.

4. Reclassify H5r-B and H5r-L1.

Keep them as stronger stress-test norms, but do not require them for the proof unless R5 fails after formalization.

5. Reformulate H5a/H5b exactly.

Separate:

- fixed Vaaler coefficient targets;
- bounded-variation frequency-weight targets;
- arbitrary-coefficient stress-test targets.

6. Continue Li--Yang audit for H5a/H5b only after coefficient reformulation.

The next audit question should be:

Does Li--Yang's theorem apply to fixed-coefficient, residue-split main Vaaler sums in any subrange of

$$
1\le H\le D X^{-1/4}?
$$

The expected answer is: only below Li--Yang's own truncation scale

$$
H\le D X^{-\theta^*},
$$

unless a stronger theorem is supplied.

7. Keep signed Fourier truncation as a comparison route.

The signed tail formally preserves characters:

$$
\sum_{|h|>H_D}
\frac{1}{h}
\sum_{d\sim D}\chi_4(d)e(hX/d),
$$

and

$$
\sum_{|h|>H_D}
\frac{\chi_4(h)}{h}
\sum_{d\sim D}e(hX/(4d)).
$$

But no endpoint tail estimate is known. If the tail is bounded absolutely, it likely recreates an L1-type obstacle.

8. Keep Mellin--Perron as a comparison route.

It preserves the arithmetic Dirichlet series

$$
4\zeta(s)L(s,\chi_4),
$$

but after truncation and functional equation it likely reconstructs Voronoi/Bessel reciprocal sums. This remains diagnostic, not a proof route.

Confidence:

High confidence in the Li--Yang source-audit conclusion: the phase class matches structurally, but the theorem does not directly cover the endpoint height or endpoint exponent.

High confidence that Li--Yang does not imply H5r-B or H5r-L1, because those require arbitrary-coefficient or termwise absolute-value control not present in the final $S$ theorem.

High confidence in the algebraic structure of R5: Fejer residuals are positive kernel sums, and their spikes correspond to near-products $md\approx X$.

Moderate-to-high confidence that R5 proves H5r-F using only $\tau(n)\ll_\epsilon n^\epsilon$, once H4's Fejer majorant is confirmed.

Moderate confidence that this demotes H5r-F from central bottleneck to technical residual lemma.

Low confidence that current Li--Yang/Bombieri--Iwaniec technology proves the remaining endpoint main-term estimates H5a/H5b at height $D X^{-1/4}$.

No new Gauss circle exponent is proved here. The concrete Round 9 progress is a sharper theorem audit and a plausible proof of the fixed-Fejer residual target, shifting the hard analytic focus back to the Vaaler main sums.

# Conductor Independent Analysis — Research Round 1

## Verdict

The Round 9 proposal

$$
\Sigma_{\rm abs}\left(0<|N|\le D^4/X\right)
\ll_\epsilon (D+D^4/X)X^\epsilon
$$

is false for the frozen coefficient-weighted quantity. The obstruction survives the actual $\beta$ weights because it may be restricted to the single frequency $h=1$, where $|\beta_{1,H}|$ is bounded below under H4. The correct candidate lower bound is

$$
\boxed{
\Sigma_{\rm abs}(0<|N|\le M)
\ge c\min(D^4,MD)-C_\epsilon D^2X^\epsilon.
}
$$

At $M=D^4/X$ this becomes

$$
\Sigma_{\rm abs}\left(0<|N|\le D^4/X\right)
\ge cD^5/X-C_\epsilon D^2X^\epsilon,
$$

so the absolute target fails by a power for $D\ge X^{1/3+\delta}$. This is conditional on the H4 lower envelope and the accepted conditional exact-$N=0$ closure. It does not prove a lower bound for the full signed mass.

## Independent derivation

Restrict to

$$
h_1=h_2=h_3=h_4=1
$$

and denominators in a block $\mathcal D_D=[D,2D)\cap\mathbb Z$. Define the ordered pair sums

$$
s(a,c)=\frac1a+\frac1c.
$$

There are $\asymp D^2$ such pairs, and every $s(a,c)$ lies in an interval of length at most $D^{-1}$. Partition that interval into windows of width

$$
\eta=\frac{M}{16D^4}.
$$

For $M\ll D^3$, the number of windows is $K\ll D^3/M$. If $v_j$ denotes the number of ordered pairs in window $j$, Cauchy--Schwarz gives

$$
\sum_jv_j^2
\ge \frac{(\sum_jv_j)^2}{K}
\gg \frac{D^4}{D^3/M}
=MD.
$$

Each pair of pairs in the same window produces a denominator quadruple satisfying

$$
\left|\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}\right|<\eta.
$$

Since $Q=d_1d_2d_3d_4<16D^4$ and

$$
N=Q\left(\frac1{d_1}-\frac1{d_2}+\frac1{d_3}-\frac1{d_4}\right),
$$

all these tuples have $|N|<M$. Under H4, $|\beta_{1,H}|\ge b_0>0$, so the same-window absolute $\beta$ mass is $\gg MD$. Subtracting the accepted conditional bound

$$
\Sigma_{\rm abs}(N=0)\ll_\epsilon D^2X^\epsilon
$$

gives the stated nonzero-band lower bound. The truncation is harmless because $h=1$ is supported throughout the active range. There are no reduced-fraction lifts: $1/d$ is already reduced.

For an actual smooth dyadic weight, the same argument requires a subinterval of $\asymp D$ denominators on which $|w_D|$ has a fixed positive lower bound. For a uniform claim over bounded dyadic weights, the admissible choice $w_D=1$ on the block already supplies the counterexample.

## Crossover

In the fat band $M=D^4/X$, the lower-bound-to-budget ratio is

$$
\frac{D^5/X}{D^2}=\frac{D^3}{X}.
$$

Thus the natural crossover of the unit-frequency obstruction is $D=X^{1/3}$, not $X^{3/8}$.

The older $X^{3/8}$ scale is recovered by restricting to a bulk frequency block $h\asymp P\asymp H_D$: the window lower bound is $MD/P$, and $P=H_D\asymp DX^{-1/4}$ gives $D^4X^{-3/4}$ at the fat band. Choosing $P=1$ is stronger. Therefore $X^{3/8}$ is a bulk-frequency specialization, not a raw-versus-weighted boundary.

## Equal-denominator error in A4-009

If $d_1=d_2=d_3=d_4=d$, then

$$
N=d^3(h_1-h_2+h_3-h_4).
$$

The relation $h_1+h_3=h_2+h_4$ used in A4-009 forces $N=0$. It cannot support a claim about $0<|N|\le D^4/X$. Consequently, both A4-009's displayed raw nonzero count and its proposed weighted upper bound should be rejected as Round 1 candidates.

## Comparison with the blind upper bound

The statement-only report proves the universal but coarse estimate

$$
\mathcal M_{\rm abs}(D,H;K)
\ll D^3(\log(1+H))^3\left(1+K/D^2\right),
$$

up to the stated $\Phi$ and dyadic-weight factors. At $K=D^4/X$ this is $\ll D^3\log^3X$. It is compatible with the unit-frequency lower bound, which reaches $D^3$ at $D=X^{1/2}$. It neither proves the desired $D^2X^\epsilon$ estimate nor rescues A4-009. Its useful contribution is a complete coefficient/lift accounting and an independent warning that no special $X^{3/8}$ transition follows from definition-level packing.

## Scope across the four frozen quantities

- **Raw count:** the unit-frequency family gives the same $MD$ scale after exact-resonance subtraction.
- **Absolute $\beta$-weighted mass:** the lower bound applies because $|\beta_1|\asymp1$.
- **Unsigned/character-removed mass:** identical on this fourfold family and therefore equally obstructed.
- **True signed mass:** remains open. A positive $h=1$ subtotal can be cancelled by the complementary tuples; no sign-preserving lower bound has been proved.

## First doubtful step and state effect

The elementary window calculation is complete. The first conditional step is the uniform H4 lower bound for $|\beta_{1,H}|$; the second is the H4-dependent exact-$N=0$ mass closure used for subtraction. Both require the existing H4 source audit.

No graph mutation should occur in Round 1. The lower bound must first receive independent review of:

1. band and coefficient normalization;
2. same-window counting and exact-resonance subtraction;
3. the $h=1$ coefficient lower envelope and dyadic-weight transfer;
4. endpoint and epsilon uniformity.

Subject to those reviews, the likely state effect is to strengthen `M9-near-collision-absolute-lower-bounds` from the $X^{3/8}$ bulk-frequency threshold to the $X^{1/3}$ unit-frequency threshold while leaving every signed and pointwise obligation open.

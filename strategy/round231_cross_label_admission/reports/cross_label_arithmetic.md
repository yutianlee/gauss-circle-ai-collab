# Actual harmonic mean density and its signed cancellation

## 1. Result

Task `cross_label_arithmetic`; arithmetic discovery, nonblind; bounded
prelaunch231 admission screen, 2026-10-11. Analytic Round231 remains
unlaunched. Frozen graph SHA256
`a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b`.

There is an exact arithmetic cancellation of the complete smooth
mean density. It uses the actual harmonic means, the precise cosine
phase, and every harmonic. It is stronger than merely replacing the
squarefree coefficients by an unspecified constant density:

1. For every fixed `1/2<sigma<1`, `eta>0`, uniformly for all integers
   `s>=1` and real `x>=1`,

       A_s(x):=sum_(d<=x, d squarefree) r2(d s^2)
              =kappa_s x+O_(sigma,eta)(s^eta x^sigma),       (A1)

       kappa_s=kappa product_(p=1 mod4, p^a||s)
                             [1+2a(p+1)/(p+2)],
       sum_(s>=1) kappa_s/s^2=pi.                          (A2)

2. Replacing each label measure `dA_s(x)` by its actual mean
   `kappa_s dx` on the full positive half-line gives a cosine waveform
   which is **exactly zero** whenever `R>1/sqrt(T)`.

3. On the literal retained region `d>Q=floor(T^(2/5))`, its mean
   waveform `C_Q` instead satisfies the complete bound

       |C_Q(R)| << R^(-1)Q^(-1/4) << T^(-11/10)           (A3)

   throughout the physical window. All harmonics and smoothing tails
   are included. Centering `Z_Q` by this density changes its twelfth
   moment by only `O_epsilon(T^(9beta-11/10+epsilon))`.

These are candidate arithmetic identities and a paid transfer, **not
a full moment gain**. The complete centered arithmetic discrepancy
still has only the inherited `T^(10beta+epsilon)` moment bound.
The preferred `29/25` estimate remains unpaid. The coarse mean law
(A1) does not control the required microscopic six-root correlations.
This report does not repeat an absolute-certificate lower bound and
does not claim that the new density identity passes admission.

## 2. Exact statement and hypotheses

Use exactly the fixed `rho`, `Psi`, `w`, `a_n`, `f_d`, `B_T`, `Z_Q`,
`E12`, `I12`, real `T>=2`, literal `Q=floor(T^(2/5))`, and `beta`
from the assigned complete-target brief. Thus

    a_(d s^2)=r2(d s^2)s^(-3/2)d^(-3/4)Psi(s sqrt(d/T)),
    Z_Q(R)=sum_(d>Q squarefree)sum_(s>=1)
               a_(d s^2)cos(2pi R s sqrt(d)-3pi/4).

Put `e(t)=exp(2pi i t)`. The positive constant in (A2) is

    kappa=pi(1-2^(-2))
       product_(p=1 mod4)(1-3p^(-2)+2p^(-3))
       product_(p=3 mod4)(1-p^(-2)).                       (A4)

Define, with no truncation in `s`,

    C_Q(R)=sum_(s>=1) kappa_s s^(-3/2)
        integral_Q^infinity x^(-3/4)Psi(s sqrt(x/T))
                              cos(2pi R s sqrt(x)-3pi/4)dx,
    D_Q(R)=Z_Q(R)-C_Q(R).                                 (A5)

`C_0` denotes the same integral starting at zero. These integrals
are integrable at zero and at infinity. They and the harmonic sum
are absolutely convergent before any oscillatory estimate. Their
constants depend only on the fixed functions and displayed fixed
exponents. No positivity of `Psi` beyond its defining assumptions
is used.

The precise complete transfer is

    integral w(R/T)D_Q(R)^12 dR
       =I12(T)+O_epsilon(T^(8beta-1/5+epsilon))
               +O_epsilon(T^(9beta-11/10+epsilon)).        (A6)

In particular the preferred one-sided `I12` target is equivalent,
at exponent `29/25`, to the twelfth moment bound for this actual
centered discrepancy. Equation (A6) uses the accepted collective
distinct-class deletion; it does not silently replace that deletion
by a continuum diagonal argument.

## 3. Proof or derivation

### Arithmetic harmonic means, including uniformity in the harmonic

The divisor formula gives zero for `r2(d s^2)` if squarefree `d`
contains a prime `3 modulo4`. For a split prime `p=1 modulo4` and
`a=v_p(s)`, the two possible squarefree-label local factors are

    2a+1 if p does not divide d; 2a+2 if p divides d.       (A7)

Prime 2 gives equal factors for the two possibilities, and an inert
prime in `s` has even exponent and does not change either supported
factor. In particular the mean coefficient is not `kappa g(s)`.

Define a coefficient sequence `h_s` by its formal Euler factors.
For `p=2` or `p=3 modulo4` its local polynomial is `1-z^2`. For a
split prime it is

    P_a(z)=[(2a+1)+(2a+2)z](1-z)^2
          =(2a+1)-2a z-(2a+3)z^2+(2a+2)z^3.             (A8)

Only finitely many local constant terms differ from 1. Consequently
`h_s(1)=product_(p=1 mod4)(2v_p(s)+1)`; it need not equal 1.
The exact coefficient identity is

    mu(d)^2 r2(d s^2)=sum_(m|d)h_s(m)r2(d/m).             (A9)

This follows by multiplying the squarefree local series (A7) by the
inverse local series for `r2/4`; the single global factor 4 is on
both sides of (A9). At `s=1`, the split factor is the familiar
`1-3z^2+2z^3`.

For every fixed `sigma>1/2`,

    sum_(m>=1)|h_s(m)|m^(-sigma) <<_(sigma,eta) s^eta.      (A10)

Here is the uniformity check. Unmodified split factors and all other
primes have nonconstant terms beginning at degree two, so their
absolute local product converges. Divide every modified split
factor by its constant `2a+1`; its absolute local value is at most
`1+C(p^(-sigma)+p^(-2sigma)+p^(-3sigma))`, with an absolute `C`
independent of `a`. The product of these factors over `p|s` is
`O_(sigma,delta)(s^delta)`: for sufficiently large `p`, each factor
is at most `p^delta`, and finitely many small primes contribute a
fixed constant. The product of the constants `2a+1` is bounded by
`tau(s^2)<<_delta s^delta`. Choose the two input deltas sufficiently
small for the stated `eta`. This proves (A10) with no harmonic
cutoff.

The elementary lattice-square comparison yields

    sum_(n<=y)r2(n)=pi y+O(sqrt(y)),  y>=1.

Sum (A9). The accumulated error and the tail of its main coefficient
are bounded by

    sqrt(x)sum_(m<=x)|h_s(m)|m^(-1/2)
       +x sum_(m>x)|h_s(m)|/m
       <=2x^sigma sum_m |h_s(m)|m^(-sigma).

This proves (A1), with `kappa_s=pi sum_m h_s(m)/m`.
Evaluating (A8) at `z=1/p`, and dividing by its `a=0` value, gives

    P_a(1/p)/P_0(1/p)
       =[(2a+1)p+2a+2]/(p+2)
       =1+2a(p+1)/(p+2).

This proves the first formula (A2). All factors are positive, and
`kappa_s<<_eta s^eta` also follows. The positivity and absolute
convergence in (A4) are immediate from
`1-3z^2+2z^3=(1-z)^2(1+2z)`.

For completeness, the second formula (A2) is an exact Euler identity,
not an asymptotic harmonic approximation. At a split prime set
`t=1/p`. Then

    sum_(a>=0)[1+2a(p+1)/(p+2)]p^(-2a)
      =1/[(1-t)^2(1+2t)].                                (A11)

This cancels precisely the split factor of `kappa/pi`. At prime 2
and inert primes the harmonic series is `(1-p^(-2))^(-1)`, which
cancels their factors. Absolute convergence licenses the product.
Every local factor cancels, proving `sum_s kappa_s/s^2=pi`.

### Exact cancellation of the complete smooth mean

Substitute `y=s sqrt(x)` in (A5). For every `Q>=0`,

    C_Q(R)=2sum_(s>=1)(kappa_s/s^2)
       integral_(s sqrt(Q))^infinity y^(-1/2)Psi(y/sqrt(T))
                                   cos(2pi R y-3pi/4)dy. (A12)

The total integral of the absolute integrand in each term of (A12)
is `O(T^(1/4))`, before its factor `kappa_s/s^2`. Hence (A2)
justifies the infinite summation. At `Q=0`,

    C_0(R)=2pi Re[e(-3/8)integral_0^infinity
                 y^(-1/2)Psi(y/sqrt(T))e(Ry)dy].          (A13)

Let `m(u)=integral_R rho(u,v)dv`. It is real, nonnegative, smooth,
even, supported in `[-1,1]`, and has integral 1. In particular

    Psi(z)=integral_(-1)^1 m(u)e(-zu)du.

Insert a regulator `exp(-lambda y)`, `lambda>0`, into (A13).
Fubini now holds absolutely. The elementary gamma integral gives

    integral_0^infinity y^(-1/2)exp(-lambda y)e(ay)dy
       =sqrt(pi)(lambda-2pi i a)^(-1/2),

with the continuous branch having positive real part. If
`R>1/sqrt(T)`, then `a=R-u/sqrt(T)>0` uniformly on the support of
`m`. As `lambda` decreases to zero the displayed expression tends
uniformly in `u` to `e^(i pi/4)/sqrt(2a)`. Thus

    e(-3/8)integral_0^infinity
         y^(-1/2)Psi(y/sqrt(T))e(Ry)dy
       =-i integral_(-1)^1 m(u)/sqrt(2(R-u/sqrt(T)))du.    (A14)

The left side also converges by dominated convergence because `Psi`
is Schwartz and `y^(-1/2)` is integrable at zero. The right side is
purely imaginary. This proves `C_0(R)=0` exactly. The physical
window satisfies `R>=T/2>1/sqrt(T)` for every `T>=2`.

The phase is essential: replacing `-3pi/4` by zero would leave a
nonzero real part. The equality is a property of the actual smooth
area density and actual cosine phase, not of arbitrary coefficients
or arbitrary signs.

### Literal large-class cutoff and every harmonic tail

Write `F_T(y)=y^(-1/2)Psi(y/sqrt(T))`. For every fixed `L>=0` and
`a>0`, Schwartz bounds imply

    |F_T(a)|+integral_a^infinity |F_T'(y)|dy
       <<_L a^(-1/2)(1+a/sqrt(T))^(-L).                  (A15)

For `a<=sqrt(T)`, the term with `Psi'` integrates to `O(T^(-1/4))`,
which is at most `O(a^(-1/2))`; for `a>=sqrt(T)`, arbitrary
Schwartz decay proves the stated bound. Integration by parts in
`e(Ry)` therefore bounds each complex integral in (A12) by

    O_L(R^(-1)(s sqrt(Q))^(-1/2)
                         (1+s sqrt(Q/T))^(-L)).           (A16)

Summing with its actual factor `2kappa_s/s^2` is harmless because
`sum_s kappa_s s^(-5/2)<infinity`. This proves (A3), including the
boundary at the literal integer `Q`, the infinitely many harmonics,
all signs of `Psi`, and the complete tail. No exact cancellation
between the discrete small head and the continuum is assumed.

### Full frequency density and the unpaid arithmetic measure

The positive-frequency atomic measure and its actual smooth density
on the retained region are

    mu_Q=sum_(d>Q squarefree,s>=1) a_(d s^2) delta_(s sqrt(d)),
    dmu_Q^0(y)=2y^(-1/2)Psi(y/sqrt(T))
                    [sum_(s<y/sqrt(Q)) kappa_s/s^2]dy.    (A17)

An equality at a step boundary has no effect on this Lebesgue density.
The measures are finite real signed measures; `Psi` need not be
positive. If `check(mu)` is reflection in zero, define the Hermitian
complex frequency measures

    nu_Q=[e(-3/8)mu_Q+e(3/8)check(mu_Q)]/2,
    nu_Q^0=[e(-3/8)mu_Q^0+e(3/8)check(mu_Q^0)]/2,
    epsilon_Q=nu_Q-nu_Q^0.                               (A18)

Their plus-sign Fourier transforms are respectively `Z_Q`, `C_Q`
and `D_Q`. Thus the full centered signed twelve-frequency measure
has the exact physical evaluation

    R12(T):=T integral w_hat(-T lambda)
                                d(epsilon_Q^(*12))(lambda)
           =integral w(R/T)D_Q(R)^12dR >=0.              (A19)

Every one of the 4096 cosine sign choices, every harmonic, every
mixed block and the tails are present in (A19). The smooth term
alone is at most `O(T^(1-12*11/10))=O(T^(-61/5))`.
The balanced six-plus/six-minus term alone is not the definition of
the full measure. At `Q=0`, (A14) says the two cosine branches are
`-iA(R)` and `+iA(R)`, with the same real `A(R)`; all twelve-sign
terms cancel by the exact binomial identity. Keeping only the
balanced sign pattern would hide that cancellation.

For distinct-class restoration, the accepted reduction gives
`M12(Z_Q)=I12+O(T^(8beta-1/5+epsilon))`. It also gives
`M10(Z_Q)<<T^(8beta+epsilon)`, since `8beta>1`, and the accepted
complete fallback with the paid small head gives
`M12(Z_Q)<<T^(10beta+epsilon)`. Cauchy--Schwarz yields

    integral w|Z_Q|^11 <= M10(Z_Q)^(1/2)M12(Z_Q)^(1/2)
                            <<T^(9beta+epsilon).          (A20)

Expand `(Z_Q-C_Q)^12-Z_Q^12`, take absolute values only in this
small centering error, and use (A3). The term linear in `C_Q` costs
`T^(9beta-11/10+epsilon)`. The quadratic term costs
`T^(8beta-22/10+epsilon)`. Every remaining term with a positive
power of `Z_Q` uses the accepted moments of order at most 9, costing
`O(T^(1+epsilon))`, and the constant term uses `integral w=O(T)`.
Their exponents are smaller. This proves (A6). In particular no
term involving a repeated squarefree label was discarded.

### Exact arithmetic remainder and the price of the mean-law error

Let `E_s(x)=A_s(x)-kappa_s x`, and set

    q_s(x;R)=s^(-3/2)x^(-3/4)Psi(s sqrt(x/T))
                                  cos(2pi R s sqrt(x)-3pi/4).

For each fixed `s`, the actual retained discrepancy is exactly

    integral_(Q,infinity) q_s(x;R)dE_s(x)
       =-q_s(Q;R)E_s(Q)-integral_Q^infinity
                                             E_s(x)q_s'(x;R)dx. (A21)

The boundary convention includes `d=Q` in `A_s(Q)` and excludes it
from the retained sum. For a fixed harmonic, all displayed integrals
converge by Schwartz decay. The sum of the original expressions on
the left of (A21) converges absolutely as the difference of the
atomic and density expressions already proved convergent. No
global bound is obtained by summing an uncontrolled majorant of
the right side of (A21).

The precise problem with (A1) can already be seen on a single smooth
label shell. Let `chi_N` be a fixed-shape smooth cutoff supported
in `[N,2N]`, with derivatives `O_j(N^(-j))`, `N>=1`. Partial
summation and (A1) give, for every fixed `L`,

    |integral chi_N(x)q_s(x;R)dE_s(x)|
       << s^(eta-3/2)N^(sigma-3/4)
           (1+Rs sqrt(N))(1+s sqrt(N/T))^(-L).            (A22)

The derivative of `Psi` is absorbed using a higher fixed Schwartz
order. This is a local, finite-shell estimate, not an illicit
summation over unbounded label and harmonic ranges. Its corresponding
direct absolute shell price is

    O(s^(eta-3/2)N^(1/4)(1+s sqrt(N/T))^(-L)),            (A23)

using the actual inequality `r2(d s^2)<=tau(s^2)r2(d)` and the
elementary `r2` summatory bound. The oscillatory-derivative term
in (A22), relative to (A23), has factor

    Rs N^(sigma-1/2),                                   (A24)

which is at least a constant times `T` on the physical window for
`s,N>=1`. Thus the proved coarse arithmetic law provides no saving
on even one such oscillatory shell. This is a limitation of this
specific estimate, not an impossibility theorem for actual arithmetic.
Equivalently, root resolution `1/T` means a label interval of length
`O(sqrt(N)/(Ts))`; (A1) does not give a useful error relative to
its smooth mass on that scale.

Taking the globally valid absolute mass bound instead gives
`|D_Q|<<T^(1/4)` and moment price `O(T^4)`. Retaining the stronger
accepted actual moment estimate in (A6) gives the unchanged
`R12<<T^(10beta+epsilon)`. Neither operation produces new signed
control of (A19).

## 4. First doubtful or unproved step

The arithmetic identities and transfers above are candidates for
independent review; no analytic remainder is intentionally hidden in
their statements. The first unproved research step is the new joint
estimate

    T integral w_hat(-T lambda)d(epsilon_Q^(*12))(lambda)
                        <=C_epsilon T^(29/25+epsilon),    (A25)

or any fully restored strict gain over the inherited exponent.
One-variable mean cancellation and the exact zero in (A14) do not
prove (A25). Its coefficients are actual signed arithmetic
discrepancies, and its convolution keeps all frequency correlations.
No independence, generic random-sign model, or microscopic
equidistribution hypothesis has been inserted.

The complete costs are explicit. If (A19) were bounded at exponent
`b`, the restored full twelfth moment would have exponent at most

    max(b,15/13,8beta-1/5,9beta-11/10).                  (A26)

The last entry is smaller than the repeated-class cost. Presently
`b=10beta=1.28966351948...`, so there is no gain. Strict moment
gain requires the complete maximum below `10beta`; strict pointwise
gain requires it below `13beta-1/2`. The preferred `b=29/25` would
pay the `15/13` head with slack `2/325` and produce `102/325`, not
the quarter exponent. No sufficient unbounded family of fixed
moment orders is supplied here.

## 5. Required controls and outcomes

| Control | Outcome |
| --- | --- |
| Actual squarefree support | An inert prime in squarefree `d` makes the full class zero; retained exactly in (A7)--(A9) |
| Split-prime harmonic law | For `s=5`, `kappa_5=(19/7)kappa`, not `3kappa`; the weighted frequency of `5|d` is `2/7`, giving `3-2/7` |
| Prime 2 and inert harmonics | `kappa_2=kappa_3=kappa`; these primes change root scale but not the harmonic mean factor |
| All harmonics | Uniform (A10), absolutely convergent (A11), and (A16) retain the infinite sum |
| Signed mollifier | No sign assumption on `Psi`; its compactly supported marginal is used only in the exact mean identity |
| Fresnel branch and phase | Abel regulator fixes the branch; `e(-3/8)e^(i pi/4)=-i`, giving zero real part |
| All cosine signs | The full Hermitian measure is retained; a balanced six-root term alone is insufficient |
| Literal cutoff | The boundary in (A21) is `-q_s(Q)E_s(Q)`; `Q` is never differentiated or replaced by a smooth mask |
| All distinct-class exclusions | Restored with accepted collective error `T^(8beta-1/5+epsilon)`; no continuum diagonal argument substitutes for it |
| Mixed terms | Every centering mixed term is paid using (A20) and the accepted lower moments |
| Microscopic scale | The factor (A24) explicitly shows why the global mean error does not close the required correlation scale |
| Real windows | No evenness of `w` is used; the physical support lies strictly beyond the mean-density support threshold |
| Complete exponent | Accepted `10beta` retained; no target, pointwise, parent or endpoint promotion |

All controls are exact algebra or analytical inequalities. No numerical
experiment, simulation, externally imported theorem, or computational
asymptotic certification was used. The shell estimate (A22) is an
information limit of the displayed proof, not an adversarial
counterexample to the actual coefficients.

## 6. Dependencies and exact artifacts used

Only the own brief and its permitted contexts were read. The graph
was initially too large for full tool output and was then queried
selectively for the accepted target, source-qualified exponent,
complete moment, distinct-class reduction and absolute-certificate
nodes. No sibling brief/report or unlisted source artifact was read.

| Artifact | SHA256 |
| --- | --- |
| `protocol.md` | `f26fb038496b5ae171b3352e7d02ba1a4b7dd808ef31bf8620e6d4930cea9d5a` |
| `state/proof_obligations.yml` | `a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b` |
| `state/active_campaign.yml` | `fd65ce5c6b117aa4ca8ed097f85e2c786621c8054ca81791aa6e5e17006a82fa` |
| `strategy/round231_cross_label_admission/briefs/cross_label_arithmetic.md` | `355220a5f98ed2d39588c11cf2a3f9a1989af6b7e98885689e8f89cda5b6b717` |
| `strategy/round231_cross_label_admission/briefs/complete_target.md` | `8ee37ee007ff58b8cda6db3d33205c0896639099a44be159ff930a7e86b19809` |
| `proofs/kernels/gc_complete_distinct_radical_moment_reduction.md` | `d7a5945f834c565c11cdc26bc3480de12d173e35de28c734381392f5feecb1ee` |
| `strategy/round231_harmonic_admission/reports/harmonic_pooling_discovery.md` | `d5c56d66442579162bb1440e1b13379439a0583a7afb5b854822c85a3239539e` |
| `rounds/codex-managed/gc-actual-vector-gram-correlations/synthesis.md` | `93413bbc466cd48bc9fe4ebeede40c62bb218bb077f8afda1750c23805fb05dd` |

The elementary squarefree convolution in the permitted harmonic
report is extended here to the actual means for every harmonic.
Accepted216 supplies the head, lower masked moments, repeated-class
error and exact full-target restoration. Accepted204 and the
source-qualified Li--Yang input supply the inherited full moment,
with their existing scope unchanged. The Round221 synthesis is used
only as a warning against discarding the arithmetic discrepancy
after isolating a small smooth main term.

Communication disclosure: the harmonic mean factors were being
derived from the split-prime local series when the conductor sent
the same proposed residue, its harmonic sum identity, and the
suggestion of exact Fresnel cancellation. Those suggestions were
independently checked algebraically and are used in (A11)--(A14).
The conductor later suggested the Cauchy--Schwarz route for (A20),
which is used. The conductor mentioned diagnostic checks, but their
outputs were not read and are not evidence for any assertion here.
This is not a statement-only blind report. No sibling findings or
proofs were received. All research effort was analytical/algebraic;
tools only read permitted files, write this report and freeze hashes.

## 7. Recommended state effect

**No graph change and no analytic launch.** Retain the actual uniform
harmonic mean formula, exact all-harmonic smooth cancellation and
the fully paid centering transfer as reviewed candidate evidence
after the required independent checks. Do not call them an improved
full estimate or an essential new reduction already enabling one.

The exact smooth density has now been removed without loss, but the
remaining arithmetic discrepancy (A25) is quantitatively unpaid.
Its available complete exponent is still `10beta`; no new input
passes the admission gate. The accepted graph, proof draft,
validation matrices, active campaign, legacy evidence and every
other report remain untouched. Stop after this assigned report and
its SHA256; no successor is designed.

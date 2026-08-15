# Round 28 analytic attack: two saddles and the outside-height survivor

## 1. Result

The proposed complete beta-transition proof is not established. The exact
signed Stirling phase has two stationary points, alpha=plus or minus
lambda, not one positive saddle plus a wholly nonstationary negative
sector. A Morse change of variables treats each entry and exit by an
incomplete Fresnel factor without an intrinsic q-power loss. On compact
patches separated from finite-height edges and the artificial rho seam,
both saddles retain the Round-27 local q^(-2) capacity.

The extension fails first at the finite v-height boundary. When the moving
hard-top pole reaches nu=plus or minus V, the truncated signed convolution
has a logarithmic edge term. No accepted formula cancels it with the
oriented outside-v side uniformly in the moving saddle. Consequently the
complete sums and finite-side limits cannot be certified from the local
stationary lemma.

## 2. Exact statement and hypotheses

Collecting the alpha-dependent terms in the accepted Round-20 phase gives

    dPsi/dalpha = log(|alpha| D_j/(pi q sqrt(Xx)))

on both signed Stirling branches. Set

    lambda = pi q sqrt(Xx)/D_j.

Then the stationary points are alpha=plus or minus lambda, with Hessians
plus or minus 1/lambda. For fixed beta and nu, the finite alpha interval is

    P=max(beta+nu-U,-2S-beta),
    Q=min(beta+nu+U, 2S-beta).

On a component with |alpha| comparable to lambda, assume the complete
signed, endpoint-recombined amplitude has a scaled C^2 norm M. The exact
Morse coordinate for the positive saddle is

    zeta(y)=sgn(y-1) sqrt(2[y log y-y+1]),

and the negative saddle has the reflected version. Each finite component
equals its saddle value times an incomplete Fresnel difference, plus
O(M), uniformly as P or Q crosses the saddle.

For the hard top, the physical distributional limit must be taken before
absolute values:

    (a+i mu)^(-1) -> pi delta_0(mu)-i PV(1/mu).

The compact local q^(-2) statement requires fixed b>0 and positive
separation from P,Q, nu=plus or minus V, rho=0, and v=0.

## 3. Proof or derivation

For alpha>0, subtracting the saddle phase gives

    Psi(alpha)-Psi(lambda)
      =lambda[(alpha/lambda)log(alpha/lambda)-alpha/lambda+1].

The Morse coordinate converts this exactly to a quadratic phase. The
negative signed Stirling phase gives the reflected quadratic with opposite
Hessian. Thus stationary entry and exit contribute incomplete Fresnel
factors; an exact endpoint saddle has one half of the full Gaussian
constant. No additional q power is created.

The post-endpoint R1 denominator has magnitude lambda^(-1) at either
separated saddle. The signed hard-top two-denominator convolution has
local magnitude O_b(lambda^(-2)) before the recorded stationary numerator,
so the same algebra as Round 27 gives D_j/(q lambda), hence q^(-2), on
both signs.

At finite v-height write

    C_{a,V}(L)=integral_{-V}^V H_b(nu)/(a+i(L-nu)) dnu.

At L=V and H_b(V) nonzero, setting y=V-nu gives

    C_{a,V}(V)=-i H_b(V) log(1/a)+O(1).

The same holds at -V. The accepted height transform is analytic and not
identically zero, so admissible edge points with nonzero H_b exist. This
prevents uniform scaled derivative bounds for the isolated finite segment.

A conditional exponent calculation is promising but not promotable. If
the full-line local convolution and Round-27 stationary monomial are used,
the hard-top main term simplifies schematically to

    q^(-2) D_j^(2-r) X^(r/2-1/2+b/4)
    x^(-r/2-b/2-5/4),

with radial phases involving sqrt(Xx)(2 plus or minus q/D_j). Radial
integration would make even the exact q=2D_j resonance target-compatible
because q^(-2) is at most D_j^(-2). But this calculation omits the
finite-height edge, transition derivatives, complete h/profile factors,
and oriented sides. It therefore diagnoses plausible capacity only.

## 4. First doubtful or unproved step

The first open step is an exact finite-contour combination of the
inside-v integral with the oriented outside-v side, followed by a justified
nested exhaustion in U,V,S and the physical top limit. It must cancel or
control the logarithmic moving-edge term uniformly in alpha, q, x, and
the dyadic scale. Only then can the scaled C^2 Fresnel hypothesis and the
complete q,h,scale,radial sums be proved.

## 5. Control tests and outcomes

- Signed versus unsigned: the second inverse frequency requires the signed
  PV/delta combination; the finite-edge logarithm exists before arithmetic
  signs. Outcome: local pass, global open.
- Endpoint uniformity: incomplete Fresnel normalization passes; the finite
  v-edge fails as a standalone segment.
- Negative alpha: a second saddle exists and has the same local capacity;
  assumed global nonstationarity is false.
- Residue: the exact omega-G/omega-E1 recombination remains required; no
  new residue is introduced.
- Scale: q^(-2) alone does not justify the dyadic sum without every other
  monomial and endpoint term.

## 6. Dependencies and exact artifacts used

This conductor-materialized report uses the accepted Round-20 phase, the
Round-27 synthesis and reports, the Round-28 blind and hostile seam
statements, and the conductor's independent algebraic audit. No numerical
experiment or external theorem was used. The assigned discovery agent did
not materialize its report within the strict round time box; no unwritten
claim from that task is treated as evidence.

## 7. Recommended state effect

Promote only the exact two-saddle correction and, after independent
agreement, the conditional endpoint-uniform Fresnel tool and finite-height
logarithmic no-go. Retain the complete beta transition, double-bounded
share, full sums, finite sides, M9-M1, M9, and the target as open. The next
frozen kernel should be the outside-v-side-reconciled truncated Hilbert
operator, not another isolated stationary-phase expansion.

# Conductor analysis: exact phase, Fresnel transition, and height-edge seam

## 1. Result

The finite beta trace admits an exact positive-alpha endpoint-stationary
normal form. Entry and exit do not intrinsically lose a power of q: they
replace the full stationary constant by an incomplete Fresnel factor.
However, this does not extend the Round-27 local q^(-2) bound to the finite
operator. Two independent uniformity conditions are missing:

1. scaled alpha-derivative bounds for the complete signed and recombined
   amplitude; and
2. cancellation or exhaustion of the logarithmic PV term created when the
   moving hard-top pole reaches the finite v-height edge.

The negative-alpha phase has no critical point once its signed Stirling
branch is written correctly, but its endpoint terms remain part of the
finite-side ledger.

## 2. Exact phase audit

For positive alpha, after collecting the alpha-dependent terms in the
accepted phase, direct differentiation gives

    dPsi_+/dalpha = log(alpha/lambda),
    lambda = pi q sqrt(Xx)/D_j,

up to the already isolated lower-order Stirling remainder. Hence

    Psi_+(alpha)-Psi_+(lambda)
      = lambda h(alpha/lambda),
    h(y)=y log y-y+1.

The exact Morse coordinate

    zeta(y)=sgn(y-1) sqrt(2h(y))

converts this phase to lambda*zeta^2/2. A finite positive component
[P,Q] therefore has the leading incomplete Fresnel factor with transition
parameters sqrt(lambda)zeta(P/lambda) and
sqrt(lambda)zeta(Q/lambda). At an exact entry or exit saddle, the remote
side contributes one half of the full Fresnel constant. This changes no
q-power.

For negative alpha, write alpha=-r with r>0 and use the signed Stirling
phase

    -[r log(r/2)-r+pi/4].

Differentiating the complete alpha-dependent phase gives

    dPsi_-/dalpha = log(r/lambda)

with the same positive lambda after the linear scale terms are collected.
Thus there are two signed saddles alpha=plus or minus lambda, with Hessians
plus or minus 1/lambda. The negative branch was incorrectly called
nonstationary in the Round-27 hostile narrative; that assertion was not
promoted into the scoped local lemma, but the full transition must include
this second saddle.

## 3. Finite polytope

For fixed beta and nu, the exact finite constraints give

    P=max(beta+nu-U,-2S-beta),
    Q=min(beta+nu+U, 2S-beta).

The transition endpoints therefore depend on U, S, beta, and nu. A uniform
Morse lemma must be applied after this intersection and after all masks
have been placed in the amplitude. Replacing P,Q by infinite endpoints
before proving side decay would erase the very terms that require control.

## 4. Signed hard-top order and edge term

For fixed positive b, the full-line signed hard-top convolution is

    C_0(L)=pi H(L)-i PV integral_R H(nu)/(L-nu) dnu.

Only this distributional sum may be inserted into the Morse amplitude.
Taking absolute values or differentiating the two pieces separately at
the pole is invalid.

At finite height,

    C_{a,V}(L)=integral_{-V}^V H(nu)/(a+i(L-nu)) dnu.

When L=V and H(V) is nonzero,

    C_{a,V}(V)=-i H(V) log(1/a)+O(1).

The same occurs at -V. It is a boundary term of the truncated Hilbert
transform, not an interior stationary loss. The exact finite vector
identity says the outside v-sides must be retained, but no accepted result
yet evaluates them in the same physical top limit. Consequently one may
not replace the finite convolution by its full-line counterpart until one
of the following is proved:

- a nested limit V->infinity before a->0, with uniform control of every
  other height and radial parameter; or
- an exact cancellation between the logarithm and the oriented outside-v
  side.

## 5. Sum-capacity implication

Conditional on a complete scaled C^2 bound for the recombined signed
amplitude, the Fresnel transition itself preserves the Round-27 q-power.
The q^(-2) interior would then be absolutely summable, and exact endpoint
half-Fresnel pieces would also be summable. But the derivative hypothesis
is stronger than a pointwise saddle estimate: differentiating the signed
PV amplitude can cost a distance-to-edge factor and differentiating the
rho split must retain omega-G and omega-E1 cancellation.

Therefore no honest complete q, h, scale, and radial summation can begin
from the current local lemma alone. The first quantitative survivor is the
connector-completed, outside-v-side-reconciled signed Fresnel amplitude,
with a uniform scaled C^2 norm.

There is nevertheless a promising conditional exponent check. If one
inserts the Round-27 hard-top convolution bound into its displayed
stationary amplitude and writes sigma=r+(a+b)/2, the main monomial
simplifies, up to fixed constants and bounded beta factors, to

    q^(-2) D_j^(2-r) X^(r/2-1/2+b/4)
    x^(-r/2-b/2-5/4).

At the two signed saddles the remaining radial phases are of the form

    exp(i pi sqrt(Xx)(2 plus or minus q/D_j)).

With y=sqrt(x), one radial integration by parts would give

    min(1, [sqrt(X)|2 plus or minus q/D_j|]^(-1)).

The q^(-2) weight makes even the exact minus-sign resonance q=2D_j cost
only D_j^(-2), which is at most X^(-1/2) in the active range. Summing q
would therefore contribute at most X^(-1/2) times logarithms. At
D_j=sqrt(X), the remaining scale monomial is then of normalized constant
size. This calculation suggests the completed stationary main terms may
be target-safe.

It is not yet a proof: the exact phase sign, the h-sum, all real-abscissa
factors, transition remainders, moving supports, and outside-side
reconciliation must be rederived together. It is recorded as the
conductor's next algebraic test, not as accepted evidence.

## 6. Controls

- Signed/unsigned: the height-edge logarithm exists before arithmetic
  signs, while the interior second inverse frequency requires the signed
  PV/delta combination.
- Residue: no new pole is introduced; the omega split and A=0 ledger remain
  unchanged.
- Endpoint: half-Fresnel normalization passes, but the finite v-edge fails
  as a standalone segment.
- Numerical allocation: no computation was used.

## 7. State recommendation

Promote only the conditional uniform Fresnel normal form and the exact
finite-height logarithmic edge obstruction after independent hostile
agreement. Keep the full beta transition open. The next proof kernel should
be the oriented outside-v-side plus truncated-Hilbert combination, not a
bare stationary-phase remainder estimate.

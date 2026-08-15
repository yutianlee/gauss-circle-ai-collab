# Round 27 synthesis: the post-endpoint radial gain

Campaign: m9-m1-beta-radial-pushforward-bv
Round type: beta radial pushforward and BV
Graph SHA-256 before patch: 8a92f4ad5e1067f9e184baa0d85c6eb71b1e1f2eee76261f66b6b437a5e27cac

## Conductor decision

Round 27 corrects the scope of Round 26 and promotes a narrower but materially stronger local mechanism.

The stationary coefficient is q^0 for the unsplit radial transform G=E1+R1. It is not q^0 for the actual post-endpoint survivor R1: its explicit factor 1/rho contributes one inverse q at a separated positive-alpha saddle. For the hard top, first taking the symmetric physical limit

    (a+i mu)^(-1) -> pi delta_0(mu) - i PV(1/mu)

and then evaluating the signed two-denominator convolution contributes a second inverse frequency. On every fixed line b=Re(v)>0, away from saddle entry, saddle exit, and the artificial-rho seam, the local post-endpoint coefficient is O_b(q^(-2)), up to the recorded scale, radial, and polylogarithmic factors.

This does not prove the beta trace. Uniform patching, the double-bounded share, complete scale/height/radial summation, endpoints, and finite outside-height limits remain open. The hostile report alone claims the compact double-bounded share is target-safe; because the statement-only derivation and discovery verdict do not independently prove that estimate, the graph retains it as open.

All work was analytical/algebraic. No numerical experiment or external theorem was used.

## Exact hierarchical and residue algebra

The accepted partition is

    1 = psi(beta) + (1-psi(beta))psi(alpha)
        + (1-psi(beta))(1-psi(alpha)).                         (27.1)

The beta branch owns the double-bounded box. Internally,

    psi(beta) = psi(beta)psi(alpha)
                + psi(beta)(1-psi(alpha)).                    (27.2)

The two internal psi'(alpha) connector edges cancel, and their A=0 weights add to one. Thus the hierarchical beta branch has one psi'(beta) connector and crosses the full arithmetic residue.

The displacement must first use G=E1+R1, in which the apparent rho=0 residues cancel. With r=-Im(rho), choose a smooth cutoff omega(r)=1 near zero. After the complete same-mask endpoint image has been assigned to the endpoint ledger, the exact survivor is

    R1 = omega G + (1-omega)R1 - omega E1.                      (27.3)

It is regular term-by-term in the appropriate region, carries the isolated artificial residue exactly once, and produces no new cutoff connector because the omega' terms cancel by G-E1-R1=0. All actual profiles, floors, stars, finite sides, and the external X^(1/4) normalization remain.

## Corrected stationary normalization

The exact height relations are

    r = (alpha+beta+nu)/2 = -Im(rho),
    mu = alpha-beta-nu,
    alpha = r+mu/2.                                           (27.4)

At

    alpha_0 = pi q sqrt(Xx)/D_j,

with bounded beta and separated local support,

    1/rho = 2i/alpha_0
            + O((1+|beta+nu|)/alpha_0^2).                     (27.5)

The x^(1/2) change in the integral defining R1 cancels the corresponding radial square root, so the post-endpoint stationary amplitude has an additional factor D_j/q relative to the unsplit q^0 transform. This is an operator distinction, not a contradiction: adding E1 back restores the q^0 boundary capacity of G.

## Signed hard-top convolution

For the hard top, the local height kernel before its stationary numerator is

    C_a(alpha,beta) =
      integral_R phi_hat(b+i nu) dnu
      / [{rho_0-i(nu-K)/2}{a+i(L-nu)}],                       (27.6)

where L=alpha-beta and K=-alpha-beta.

On fixed b>0, the accepted compact profile has sufficient transform decay. After the symmetric PV-plus-delta split, partial fractions and a Hilbert-transform subtraction give

    C_PV(alpha,beta) = O_b(alpha^(-2)),
    C_delta(alpha,beta) = O_b(alpha^(-4)).                    (27.7)

Restoring the R1 stationary numerator yields

    (D_j/q) alpha_0 C_PV
      <<_b D_j/(q alpha_0)
      = D_j/(q^2 theta_j(x)),
    theta_j(x) = pi sqrt(Xx)/D_j.                             (27.8)

For b=1/log(2X), the loss from the v=0 polar line is only polylogarithmic; the axial residue itself remains in the separate accepted ledger. Equations (27.7)-(27.8) are promoted only for the separated positive-alpha interior. They are not uniform transition or endpoint estimates.

## Falsified interface

Pointwise complete-profile q-BV before the signed top split is false. At an actual top-pole sample the factor

    {a+i(q theta-beta-nu)}^(-1)

has size 1/a. Absolute integration before the split incurs a logarithmic divergence. Therefore the accepted period-four Dirichlet-kernel lemma remains true, but it is not the correct principal mechanism for this post-endpoint hard-top piece. The signed PV/delta split must precede absolute estimates.

Round 26's rejected claim is corrected rather than erased: stationary phase alone applied to the unsplit G transform does not create a q^(-1) arctangent kernel. What was false was extending that conclusion to separated R1.

## Unresolved seams

The smallest remaining beta-branch target is a uniform decomposition that joins:

- separated stationary interior;
- saddle entry and exit, including half-Fresnel endpoint terms;
- nonstationary and negative-alpha zones;
- the exact recombined artificial-rho seam;
- the double-bounded kernel and connector edges;
- all dyadic scales, heights, radial endpoints, and finite outside sides.

No status changes are made to M9-M1, M9-M2, M9, or the final Gauss-circle target.

## Artifact assessment

- The statement-only report independently validates the hierarchy, residue signs, height algebra, R1 normalization, and exact omega-split.
- The hostile report validates the normalization correction, proves the scoped signed convolution estimate, and supplies the actual-profile BV and absolute-value falsifiers.
- The discovery task independently returned the same q^(-1)/q^(-2) verdict. Its concise seven-section report was materialized by the conductor after its report write exceeded the task time box.

The stronger hostile assertion about the double-bounded estimate is retained as candidate evidence, not accepted mathematics.

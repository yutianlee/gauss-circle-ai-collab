# Blind beta-connector identity

Campaign: `m9-m1-beta-transition-connector`  
Task: `blind_beta_connector_identity`  
Role: statement-only blind rederivation  
Status: candidate evidence only

## 1. Result

An exact finite Cauchy--Green rectangle identity is obtained, with the
Wirtinger sign, rectangle orientations, finite horizontal sides, and the
crossed (A=0) residue explicit.  However, the frozen
(psi(\beta))-only trace is an enlarged masked component rather than the
accepted single-transition partition.  The actual mask

\[
 \Theta_\beta(\alpha,\beta)=\psi(\beta)(1-\psi(\alpha))
\]

creates two strip-edge derivatives.  Moreover, its (A=0) residue is only
a masked share of the previously treated (R_1) residue.  Thus the exact
identity is established, but neither full residue reconciliation nor a
physical-kernel estimate follows from the frozen statement alone.

## 2. Exact statement and hypotheses

Fix (z) and put

\[
 A=s-\frac z2=x+iy,\qquad B=A+z,
\]

with

\[
 x_0=c'-\frac{\Re z}{2},\qquad x_1=-\kappa<x_0.
\]

Let (R=[x_1,x_0]\times[-T,T]), and assume no pole lies on
(\partial R).  Let (\mathcal F(A;z)) be the complete meromorphic
integrand before masking, containing

\[
 \zeta(1-A)X_4(B)L(B,\chi_4),
\]

the accepted radial remainder, all actual scale profiles and floors, the
top half-star, and every unchanged outer integration.  For an even
(\psi\in C_c^\infty(\mathbb R)), define upward vertical integrals

\[
 V_x[\psi]=\int_{-T}^{T}\psi(y)\mathcal F(x+iy;z)\,i\,dy
\]

and left-to-right horizontal integrals

\[
 H_\pm[\psi]=\int_{x_1}^{x_0}
 \psi(\pm T)\mathcal F(x\pm iT;z)\,dx.
\]

Then

\[
 \boxed{
 V_{x_0}[\psi]
 =V_{x_1}[\psi]+H_+[\psi]-H_-[\psi]
 +2\pi i\!\sum_{p\in R^\circ}\psi(\Im p)
       \operatorname{Res}_{A=p}\mathcal F
 -\iint_R\psi'(y)\mathcal F(x+iy;z)\,dx\,dy .}
 \tag{26.1}
\]

If (T>2B_0), both horizontal terms vanish for the stated compactly
supported mask.  They must nevertheless be retained in the general finite
identity and before this support condition is imposed.

For the actual beta-only partition

\[
 \Theta_\beta(y;z)=\psi(y)\{1-\psi(y+\Im z)\},
\]

(26.1) remains true after replacing (psi) by (Theta_\beta), with

\[
 \Theta_\beta'(y;z)
 =\psi'(y)\{1-\psi(y+\Im z)\}
  -\psi(y)\psi'(y+\Im z).
 \tag{26.2}
\]

All terms inherit, without alteration, the physical normalization

\[
 -\frac4\pi X^{1/4}\operatorname{Re}
 \{e(1/8)(\cdots)\}.
 \tag{26.3}
\]

## 3. Proof or derivation

Give (R) positive orientation: bottom left-to-right, right bottom-to-top,
top right-to-left, and left top-to-bottom.  Cauchy--Green for a meromorphic
(\mathcal F), after excising small positively oriented circles around its
poles, gives

\[
 \oint_{\partial R}\psi(y)\mathcal F(A;z)\,dA
 =2\pi i\sum_{p\in R^\circ}\psi(\Im p)
   \operatorname{Res}_{A=p}\mathcal F
 +2i\iint_R\bar\partial\{\psi(y)\mathcal F(A;z)\}\,dx\,dy.
\]

Away from poles, (\mathcal F) is holomorphic and

\[
 \bar\partial\psi(y)=\frac i2\psi'(y),
 \qquad 2i\bar\partial\psi(y)=-\psi'(y).
\]

The oriented boundary is

\[
 V_{x_0}[\psi]-V_{x_1}[\psi]-H_+[\psi]+H_-[\psi],
\]

which rearranges to (26.1).  Formula (26.2) is the ordinary derivative of
the true two-mask partition.

At (A=0),

\[
 \zeta(1-A)=-\frac1A+O(1),
\]

so the (A=0) residue has the negative zeta-residue sign.  In the
(psi(\beta))-only enlargement, (psi(0)=1), and this is the full crossed
moving arithmetic residue, which must be subtracted against the already
ledgered (R_1) term exactly once.  In the actual partition, however,

\[
 \Theta_\beta(0;z)=1-\psi(\Im z).
 \tag{26.4}
\]

Consequently the crossed term is only the share
((1-\psi(\Im z))\operatorname{Res}_{A=0}\mathcal F).  The full unmasked
Round-24 (R_1) estimate does not, by itself, identify or control this
masked share: an exact complementary-mask partition and recombination
identity is required before invoking the accepted (R_1) package.

## 4. First doubtful or unproved step

The permitted reference formula does not expose the complete
(R_{1,v}(1-s)) integrand sufficiently to decide whether its artificial
(M=1), (\rho=0) pole lies in the same displacement rectangle, nor how
its accepted (E_1) cancellation is represented after multiplication by
(\Theta_\beta).  This is the first unresolved seam.  It cannot be replaced
by merely declaring the full Round-24 unmasked residue controlled.

No exact physical mask-convolved (\chi_4) kernel is derived here because
that requires the full integrand and the complementary transition pieces,
which are not contained in the statement-only data.

## 5. Required control tests and outcomes

**Support and degeneracy.**  For the (psi(y))-only enlargement,
(T>2B_0) forces (H_\pm=0).  For the actual partition, both summands in
(26.2) are compactly supported, but their supports may overlap, separate,
or degenerate as (Im z) varies.  The exact product rule remains valid in
all cases.  The second derivative term cannot be discarded even when the
first transition edge is the one under study.  Outcome: the finite identity
passes; the one-mask identification with the accepted partition fails.

**Exact versus near resonance.**  Equation (26.1) is algebraic and does not
distinguish exact from near physical resonance.  Smoothing convolves the
pure sine kernel but supplies no bound by itself.  Outcome: no resonance
estimate, cancellation claim, or unsigned extension is licensed.

Actual profiles, floors, equality conventions, and the top star remain
inside (\mathcal F) on every term of (26.1); none is replaced by an
unsigned or adversarial profile.

## 6. Dependencies and exact artifacts used

- `protocol.md`
- `state/active_campaign.yml`
- `rounds/codex-managed/m9-m1-vector-hankel-kernel/synthesis.md`
- `rounds/codex-managed/m9-m1-diagonal-transition-exhaustion/synthesis.md`
- `rounds/codex-managed/m9-m1-r1-arithmetic-residue/synthesis.md`
- `rounds/codex-managed/m9-m1-partial-functional-equation-transitions/synthesis.md`
- `rounds/codex-managed/m9-m1-beta-transition-connector/briefs/blind_beta_connector_identity.md`

No other Round-26 report, proof graph, proof draft, numerical experiment,
or external source was used.

## 7. Recommended state effect

**Promote**, after independent seam agreement, only the finite
Cauchy--Green identity (26.1), its Wirtinger sign, rectangle orientation,
horizontal-side convention, and the two-edge derivative (26.2).

**Revise** the proposed beta reduction to use the true partition, to
reconcile the masked (A=0) share through an exact complementary
recombination, and to expose the artificial (M=1), (\rho=0)/(E_1)
ledger before any residue closure is claimed.

**Retain open** the physical kernel, its normalized
(O_\varepsilon(X^\varepsilon)) estimate, outside-height limits, and the
full transition operator.

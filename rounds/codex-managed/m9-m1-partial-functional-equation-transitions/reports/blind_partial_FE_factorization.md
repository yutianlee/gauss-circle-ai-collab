## 1. Result

Let \(z=u+v\), \(s=\sigma+it\), and
\[
 \alpha=t+\frac{\Im z}{2},\qquad \beta=t-\frac{\Im z}{2}.
\]
In the unreflected completion \(\Lambda_z(s)\), zeta has height
\(\alpha\) and \(L(\,\cdot\,,\chi _4)\) has height \(\beta\). The terminal
vector kernel contains \(\Lambda_{-z}(s)\), so there the assignments swap:
the reflected zeta factor has height \(\beta\), while the reflected
\(L(\,\cdot\,,\chi _4)\) factor has height \(\alpha\). On the
\(\beta\)-bounded trace, exact reversal of only the zeta functional equation
leaves a character-high mixed factor. On the \(\alpha\)-bounded trace,
exact reversal of only the character functional equation leaves a
zeta-high mixed factor. The two resulting finite formulas are (8) and (9)
below. They are exact factorizations, but neither one by itself proves a
bound or permits an outside-height limit.

## 2. Exact statement and hypotheses

Put
\[
 A_\zeta(r)=\pi^{-r/2}\Gamma(r/2),\qquad
 A_4(r)=\left(\frac4\pi\right)^{(r+1)/2}\Gamma((r+1)/2),
\]
and \(\Lambda_\zeta=A_\zeta\zeta\),
\(\Lambda_4=A_4L(\,\cdot\,,\chi _4)\). The primitive odd character
\(\chi _4\) has root number \(+1\), so both completed factors satisfy
\(\Lambda(r)=\Lambda(1-r)\). Thus
\[
 \Lambda_z(w):=\Lambda_\zeta(w+z/2)\Lambda_4(w-z/2)
 =\Lambda_{-z}(1-w).                                                   \tag{4}
\]

Take upward finite segments \(u\in\Gamma_{a,U}\),
\(v\in\Gamma_{b,V}\), \(s\in\Gamma_{c',S}\), where
\[
 a,b>0,\quad a/2+b<1/4,\quad
 1+(a+b)/2<c'<3/2,\quad S>(U+V)/2.                                    \tag{5}
\]
The last upper bound licenses the accepted \(M=1\) removal of renormalized
radial sides. Retain exactly
\[
 \mathcal A_j(u,v)=\widehat W_j(u)\widehat\phi(v)
 \left(\frac{D_j}{2\sqrt X}\right)^u(H_j+1)^v,                         \tag{6}
\]
with the actual finite scale set, integer floors, interior profiles, and
one-sided top profile. No finite-\(U\) top transform is replaced by its
physical half-star.

Let \(\Theta_\chi(\alpha,\beta)\) and
\(\Theta_\zeta(\alpha,\beta)\) be the exact chosen transition masks,
supported respectively where \(\beta\) is bounded and \(\alpha\) is large,
and where \(\alpha\) is bounded and \(\beta\) is large. Sharp indicators or
bounded masks are both allowed; no contour deformation is performed after
inserting them. Write
\[
 \rho=\frac14-s-\frac v2,\qquad
 R_{1,v}(1-s)=-\frac{\pi i\sqrt X}{\rho}
 \int_1^{N_X}x^{\rho-1/2}e(\sqrt{Xx})\,dx.                             \tag{7}
\]

## 3. Proof or derivation

The exact quotient splits as
\[
 K_z(1-s)=X_\zeta(s,z)X_4(s,z),
\]
where
\[
 X_\zeta=\pi^{1/2-s+z/2}
 \frac{\Gamma((s-z/2)/2)}{\Gamma((1-s+z/2)/2)},
\]
\[
 X_4=\left(\frac4\pi\right)^{s+z/2-1/2}
 \frac{\Gamma((1+s+z/2)/2)}{\Gamma((2-s-z/2)/2)}.
\]
Indeed, with \(F_{-z}(s)=\zeta(s-z/2)L(s+z/2,\chi _4)\),
\[
 X_\zeta\zeta(s-z/2)=\zeta(1-s+z/2),\qquad
 X_4L(s+z/2,\chi _4)=L(1-s-z/2,\chi _4).
\]
The imaginary parts of \(s-z/2\) and \(s+z/2\) are respectively
\(\beta\) and \(\alpha\).

For the \(\beta\)-bounded trace, (4) is used only on the bounded zeta
factor. At completion level the mixed product is
\[
 A_\zeta(1-s+z/2)^{-1}A_4(1-s-z/2)^{-1}
 \Lambda_\zeta(1-s+z/2)\Lambda_4(s+z/2).
\]
This displays the bounded gamma factor exactly; simplifying it gives
\(\zeta(1-s+z/2)X_4L(s+z/2,\chi _4)\). Since
\(\Re(s+z/2)>1\), absolute expansion of only the high factor yields
\[
 \boxed{\begin{aligned}
 \mathfrak T_\chi^{U,V,S}
 ={}&\sum_j\sum_{q\ge1}\frac{\chi _4(q)}{(2\pi i)^3}
 \int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}\int_{\Gamma_{c',S}}
 \Theta_\chi(\alpha,\beta)\mathcal A_j(u,v)R_{1,v}(1-s)\\
 &\quad\times X_4(s,z)\zeta(1-s+z/2)q^{-s-z/2}
 \,ds\,dv\,du .
 \end{aligned}}                                                        \tag{8}
\]

For the \(\alpha\)-bounded trace the corresponding completed product is
\[
 A_\zeta(1-s+z/2)^{-1}A_4(1-s-z/2)^{-1}
 \Lambda_\zeta(s-z/2)\Lambda_4(1-s-z/2).
\]
The bounded character gamma factor is again retained exactly before its
exact uncompletion. Since \(\Re(s-z/2)>1\), this gives
\[
 \boxed{\begin{aligned}
 \mathfrak T_\zeta^{U,V,S}
 ={}&\sum_j\sum_{h\ge1}\frac1{(2\pi i)^3}
 \int_{\Gamma_{a,U}}\int_{\Gamma_{b,V}}\int_{\Gamma_{c',S}}
 \Theta_\zeta(\alpha,\beta)\mathcal A_j(u,v)R_{1,v}(1-s)\\
 &\quad\times X_\zeta(s,z)L(1-s-z/2,\chi _4)h^{-s+z/2}
 \,ds\,dv\,du .
 \end{aligned}}                                                        \tag{9}
\]
Both series converge absolutely and locally uniformly on the finite boxes.
Restoring the physical normalization contributes
\[
 -\frac4\pi X^{1/4}\Re\{e(1/8)(\mathfrak T_\chi+\mathfrak T_\zeta)\}. \tag{10}
\]

Pole and side ledger: the sole uncancelled radial arithmetic pole is
\(s=z/2\), equivalently the zeta pole; it lies on \(\beta=0\). Its recombined
\(R_1\) residue is the already separated Round-24 term and is not included
again in (8). The apparent poles of the gamma numerators are cancelled by
the appropriate zeta or odd-character trivial zeros; \(s=1+z/2\) is also
cancelled in \(X_\zeta\zeta(s-z/2)\). The artificial \(M=1\) pole
\(s=1/4-v/2\) has opposite \(E_1,R_1\) residues and may not be counted from
(7) alone. The accepted endpoint term \(E_1\), recombined arithmetic
residue, and renormalized radial sides remain outside (8)--(9).

All vertical contours are upward. Before accepted radial-side removal, the
upper radial side is \(\lambda+iS\to c+iS\) and the lower is
\(c-iS\to\lambda-iS\). If an outside \(u\)- or \(v\)-line is shifted left,
the exact finite formula is left vertical plus residues plus upper
left-to-right side minus lower left-to-right side. Consequently the
\(u=0\) hard-top residue, the \(v=0\) height residue, and the joint corner
must be retained with positive Cauchy sign (and with \(z=v,u,0\),
respectively); their finite outside sides are not deleted. Interior scales
have no hard-top residue. The same actual profiles and floors in (6) occur
in every such term.

## 4. First doubtful or unproved step

The first unproved step is any uniform estimate of (8) or (9) as the
outside heights tend to infinity. Exact partial factorization neither
controls the high gamma quotient nor supplies cancellation in the coupled
\(u,v,s\) integral. In particular, the character in (8) does not by itself
license the fixed-profile period-four Abel bound before the physical
outside limits, while (9) has unsigned high coefficients. No bound follows
from these identities alone.

## 5. Required control test and outcome

Multiplying the mixed factors back gives exactly
\(K_z(1-s)F_{-z}(s)\), so both branch and root-number controls pass. A
coefficient control distinguishes the branches: the character-high
coefficients are
\(\chi _4(q)q^{-s-z/2}\), hence the coefficient at \(q=2\) is zero and that
at \(q=3\) is \(-3^{-s-z/2}\); the zeta-high coefficients are
\(h^{-s+z/2}\), hence the corresponding \(h=2,3\) coefficients are both
nonzero with positive arithmetic sign. Thus the character cannot be moved
to the zeta-high branch, and an unsigned analogue of (8) loses its only
period-four arithmetic structure. Outcome: exact algebra validated; target
estimate unproved.

## 6. Dependencies and exact artifacts used

Used only `protocol.md`, the relevant nodes of
`state/proof_obligations.yml`, `state/active_campaign.yml`, the Round-19,
Round-20, Round-21, and Round-24 syntheses specified in the brief, and
`rounds/codex-managed/m9-m1-partial-functional-equation-transitions/briefs/blind_partial_FE_factorization.md`.

## 7. Recommended state effect

**Promote** the exact completed-factor identification, quotient
factorization, mixed finite formulas (8)--(9), coefficient placement, and
pole/side ledger. **Retain** the partial-functional-equation transition
obligation as open: neither trace has a target-sized estimate or a justified
outside-height limit.

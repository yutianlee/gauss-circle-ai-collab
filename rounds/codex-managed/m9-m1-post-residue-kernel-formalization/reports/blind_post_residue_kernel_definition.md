# Blind post-residue kernel definition

## 1. Result

**No-go result.** The accepted identities define a standalone pointwise scalar profile only *before* radial functional-equation reflection:
\[
P_{T,X}(h,q)=\phi\!\left(\frac h{H_0+1}\right)
\left\{\frac1{2\pi i}\int_{a-iT}^{a+iT}\widehat W_+(u)
A_0(h,q)^u\,du\right\}
+\sum_{j=1}^J\phi\!\left(\frac h{H_j+1}\right)W(A_j(h,q)^{-1}),
\]
where \(D_j=2^{-j}\lfloor\sqrt X\rfloor\), \(H_j=\lfloor D_jX^{-1/4}\rfloor\),
\[
A_j(h,q)=\frac{D_j}{2\sqrt X}\sqrt{\frac qh},\qquad
\phi(t)=\Phi(t)\mathbf1_{0<t<1}.
\]
The top inverse has the star/half value at \(A_0=1\). After the Round-16 radial functional equation and residue subtraction, however, the surviving object is not specified by the accepted record as a scalar \(\mathcal H_{T,X}(h,q)\): the quotient \(K_z(1-s)\), transformed radial weight \(G_v(1-s)\), terminal line, and horizontal sides couple \(s\) with \(z=u+v\). Scalar separation is therefore **UNPROVED**, and so is its pointwise \(O(\log X)\) bound.

## 2. Exact statement and hypotheses

Take \(a,b>0\), preferably \(a=b=1/\log(2X)\); truncate the top \(u\)-line symmetrically at \(|\Im u|\le T\). Height inversion is the full absolutely convergent line
\[
\phi(h/(H_j+1))=\frac1{2\pi i}\int_{(b)}
\widehat\phi(v)((H_j+1)/h)^v\,dv,
\]
with the exact floor and no height half-weight. Interior spatial inversions use the full line and rapidly decreasing \(\widehat W\). The top uses
\[
\widehat W_+(u)=\frac1u+\widehat W_{+,r}(u),\quad
\widehat W_{+,r}(u)=-\frac1u\int_0^1W'(t)t^u\,dt,
\]
and symmetric inversion gives \(1/2\) at \(A_0=1\).

## 3. Proof or derivation

Termwise inversion before reflection gives exactly
\[
P_{T,X}(h,q)=\phi_0(h)\{\mathscr P_T(A_0)+\mathscr R_T(A_0)\}
+\sum_{j=1}^J\phi_j(h)W(A_j^{-1}),
\]
where
\[
\mathscr P_T(A)=\frac1{2\pi i}\int_{a-iT}^{a+iT}\frac{A^u}{u}\,du,
\quad
\mathscr R_T(A)=\frac1{2\pi i}\int_{a-iT}^{a+iT}\widehat W_{+,r}(u)A^u\,du.
\]
This lists the scale sum, floor, \(\Phi\), smooth remainder, symmetric truncation, and endpoint star.

Round 16 instead applies
\[
G_v(s)F_z(s)\mapsto G_v(1-s)K_z(1-s)F_{-z}(s),\qquad z=u+v,
\]
on finite radial rectangles. Subtracting the arithmetic pole, \(v=0\) height pole, \(u=0\) Perron pole, and any auxiliary radial endpoint half-residue does not factor the remainder: \(K_{u+v}(1-s)\) and \(G_v(1-s)\) remain joint multipliers. Nor does the accepted synthesis specify the radial contour abscissa, rectangle heights, horizontal-side limiting rule, or an inverse transform converting this joint multiplier into coefficients indexed by one \((h,q)\). Thus the schematic Round-16 \(\mathcal H\) cannot be reconstructed term by term from the accepted data.

## 4. First doubtful or unproved step

The first unsupported step is replacing the post-functional-equation triple contour and its finite horizontal sides by
\(\sum_{hq}\chi_4(q)(hq)^{-3/4}e(\sqrt{Xhq})\mathcal H_{T,X}(h,q)\)
with a scalar \(\mathcal H\) independent of the open radial correlation.

## 5. Required control test and outcome

Control: set \(K_z(1-s)=1\) and suppress radial reflection. The exact scalar \(P_{T,X}\) above returns, including the top half-weight. Restore the genuine gamma quotient: its dependence on \(s\) and \(u+v\) prevents the same factorization. **Outcome: scalar post-FE separation fails the available-definition test.**

## 6. Dependencies and exact artifacts used

Only the seven brief-authorized artifacts were used: protocol, proof graph, active campaign, Round-15 blind derivation, Round-16 synthesis, Round-17 synthesis, and this task brief. No analytic Round-18 claimant report or external source was read.

## 7. Recommended state effect

Retain M9-M1-high-2adic-kernel-pointwise-bound as open and the high-\(2\)-adic tail as conditional. Revise M9-M1-maximal-angular-sign-kernel: distinguish the pre-FE scalar profile \(P_{T,X}\) from the post-FE joint \((s,u,v)\) operator. A promotable scalar kernel requires an explicit inverse radial transform plus uniform treatment of terminal and horizontal contours; otherwise the pointwise hypothesis is not well-formed.

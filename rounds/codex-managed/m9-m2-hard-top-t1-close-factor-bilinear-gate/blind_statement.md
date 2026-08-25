# Statement-only packet: hard-TOP (t=1) close-factor scalar

This packet is self-contained for independent derivation. Do not consult
the proof graph, strategy files, other Round-162 artifacts, or prior-round
reports.

Let (J=\sqrt X), (y=\lfloor J\rfloor),
(q_X=X/y^2), and
(H=\lfloor yX^{-1/4}\rfloor). Let (1\ll L\ll H\) be a half-open
polynomial block. Retain the named literal cutoff and profile factors
(\eta_L,Phi,W), their hard support entries and exits, floors, endpoint
values, and zero extension; do not infer a nonzero lower buffer from their
upper bounds.

Define

\[
\begin{aligned}
\mathcal S_{L,1}=
\sum_{\substack{d_1d_2\asymp L^2\\
d_1,d_2\ {
m squarefree},\ (d_1,d_2)=1\\
d_1\ {
m odd},\ d_2\le d_1\le4d_2}}
&\chi_4(d_1)
\left(\frac{L^2}{d_1d_2}\right)^{3/4}
\eta_L(d_1)\Phi\!\left(\frac{d_1}{H+1}\right)\\
&\times W\!\left(\sqrt{\frac{q_Xd_1}{4d_2}}\right)
e(J\sqrt{d_1d_2}),
\end{aligned}
\tag{162.BL1}
\]

where (e(z)=e^{2\pi iz}). The even-product branch is retained through
(d_2). Both variables have length (\asymp L) on the displayed cone.
The desired uniform estimate is

\[
 |\mathcal S_{L,1}|\ll_\varepsilon L^{3/2}X^\varepsilon.
\tag{162.BL2}
\]

Independently determine whether character-preserving Poisson,
differencing, a bilinear theorem, or another self-contained method proves
(162.BL2), a complete signed subsector, or only an exact obstruction.
You must derive and charge:

- the (\chi_4) additive decomposition;
- the Hessian and every stationary or degenerate direction;
- one- and two-variable dual ranges and phases;
- squarefree and coprime openings and rescaled supports;
- hard cone, profile, endpoint, nonstationary, and zero-extension pieces;
- the full (L,J,H,X) powers and the missing factor relative to the
  (L^2) positive capacity; and
- the distinction between a method obstruction and a physical lower
  bound.

Your report must contain exactly the repository's seven substantive
sections: result; exact statement and hypotheses; proof or derivation;
first doubtful or unproved step; control tests and outcomes; dependencies
and artifacts used; and recommended state effect.

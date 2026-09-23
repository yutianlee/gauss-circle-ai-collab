# Isolated Round-196 statement

Fix one literal hard-M1 \(t=1\) packet with odd
\[
 U=\mathfrak m q,\qquad q>Q,\qquad U>4Q,\qquad (v,U)=1,
\]
and retain both orientations and signs under one outer real part.  The
physical mask is imposed before every spectral operation:
\[
 P_2=\mathbf1_{\{|d-gm|\le D_L\}}
     \mathbf1_{\{|d'-gm'|>D_L\}},
 \qquad D_L=\lceil\sqrt L\rceil.
\]
Only the exact packet region
\[
 \kappa<D_L,\qquad
 \min(Y,D_L)>Q\mathfrak m\kappa
\]
is in scope.  The target is
\[
 |\mathscr R_{{\rm core},{\rm fix}}^\sigma(P_2W)|
 \ll Q\mathfrak m\kappa uX^\varepsilon.
\]

In the plus chart,
\[
 2h=v\eta+U\delta-\kappa(U^2-v^2),\qquad
 x=\kappa v+\eta=\kappa U+2S.
\]
In the minus chart,
\[
 2h=U\eta-v\delta+\kappa(U^2-v^2),\qquad
 x=\kappa v+\delta=\kappa U+2S.
\]
The anchor mode is
\[
 e(\epsilon_\omega a\bar v_qh/q),\qquad
 \epsilon_+=1,\quad\epsilon_-=-1,
\]
and its exact-conductor coefficient is
\[
 c_q(a)=\frac{2}{q\{1+e(-a/q)\}}.
\]

Derive from these data, without importing earlier conclusions:

1. the exact on-shell reduction of
   \((-1)^S e(\epsilon_\omega a\bar v_qh/q)\) in both orientations;
2. its primitive additive modulus and step \(x\mapsto x+2\) multiplier;
3. the exact multiplier identity involving \(c_q(a)\);
4. the literal step-two difference or commutator identity actually needed
   to turn that algebra into the fixed-packet target;
5. every diagonal, collision, endpoint, carry, birth/death, mask,
   squarefree/coprimality, phase, Fejer, and zero-extension term which
   survives if that difference is opened; and
6. either a valid full target theorem, a target-safe strict sector with one
   exact complement, or the first rigorous self-return/no-go.

The full \(T=0\) branch and every strict \(T\ge1\) Farey-core condition stay
in scope.  Do not replace the actual coefficient sequence by a consecutive
interval, arbitrary bounded array, or separately normed orientation.
Primitivity of a carrier is not by itself a saving.  Computation, if any,
is diagnostic-only.

The report must contain exactly the repository's seven required sections:
result; exact statement and hypotheses; proof or derivation; first doubtful
or unproved step; required controls and outcomes; dependencies and exact
artifacts used; recommended state effect.

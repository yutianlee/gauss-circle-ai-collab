# Conductor Round-199 exact-identity and review control

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Starting graph SHA-256:
  63fa05e3a4d1493bc37bdd956453a4d3eefbb9dca6fadcbf8b7a68e32ade36b5
- Allocation: 100 percent analytical/algebraic
- Numerical theorem evidence: none

## Exact conductor reproduction

For

\[
 d=ACx,\quad m=BEu,\quad d'=ABy,\quad m'=CEv,
\]

the whole lower, upper and simultaneous swaps on \(B=1,C=1,E=1\)
reverse the lower defect, upper defect and both defects, respectively.
For one odd block \(q>1\), they give

\[
 V_B=(Ax,qu,Aqy,v),\quad
 V_E=(Ax,qu,Av,qy),\quad
 V_C=(Aqu,x,Av,qy),
\]

all with gcd \(A\) and defects

\[
 A|x-qu|,\qquad A|qy-v|.
\]

With \(p=\chi_4(qxu)\), \(t=\chi_4(qyv)\), the actual incidence is
\(1,t,tp\). The fourth endpoint product has allocation

\[
 V_A=(Aqu,x,Aqy,v),\qquad (Aqu,Aqy)=Aq,
\]

and relative sign \(p\). Direct multiplication reproduces

\[
\begin{aligned}
 &u_0\overline{\ell_0}
 +t u_1\overline{\ell_0}
 +tp u_1\overline{\ell_1}
 +p u_0\overline{\ell_1}\\
 &\hspace{20mm}
 =(u_0+t u_1)\overline{(\ell_0+p\ell_1)}.
\end{aligned}
\]

Hence \(p=-1\) leaves \(+u_0\overline{\ell_1}\) when \(V_A\) is
masked away. This is a structural coefficient statement only.

At \(V_A\),

\[
 |d-(d,d')m|=Aq|u-x|>D_L
\]

for all sufficiently large live shells, from
\(A|x-qu|\le D_L\), \(q\ge3\), and \(qu\gg L\). Under the
authoritative Round-193 definition

\[
 P_1=\mathbf1_{|d-(d,d')m|>D_L},
\]

this is exactly an unproved \(P_1\) corner; no upper-far statement is
required or made.

The separate partial-block moves have the three masks

\[
\begin{aligned}
 p_{01}&=\mathbf1_{g|\kappa a-hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{11}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|c-\kappa he|>D_L},\\
 p_{10}&=\mathbf1_{g|a-\kappa hb|\le D_L}
          \mathbf1_{g|\kappa c-he|>D_L}.
\end{aligned}
\]

They are not the whole-allocation triangle and are not generally equal.
Their transported-mask commutators are retained as an independent
failure control.

## Operator and power control

The \(P_2\) and three-piece masks are physical and pre-spectral. The
whole allocation cell is formed before the later linear cap/open
projector. In the plus chart \(\kappa=C\); in the minus chart
\(\kappa=B\). The triangle moves the plus inward gcd as \(1,1,q\) and
the minus inward gcd as \(q,1,1\), so no fixed-packet or
single-orientation cancellation is claimed.

Both orientations, both \(T\)-branches, all endpoints, phases, selectors,
commutators, carries, births/deaths, cells, crossings, Fourier copies and
zero extensions remain inside one outer real part. The positive packet
deficit

\[
 \frac{\min(Y,D_L)}{H_B\mathfrak m\kappa}>1
\]

and outer capacity \(D_LL^2X^\varepsilon\) remain. Neither is a lower
bound.

## Final reviewed artifact hashes

- discovery report:
  FD20236FF18F06A5E226BC86B4D1567BF4DFBB52A64CE825F1599A215F83CB04;
- hostile report:
  06F35DA18E28429889E6348A0018646C26DDA263F441BFD3154FD5B26C354885;
- corrected statement-only report:
  C62156FFB0AE3611A482055DBB1EA651E1FE02B532DAE2BBC8F234282C71F378;
- conductor reconciliation:
  AB733A0249B23F8895AB9A214B322F48CB405FFF73CF63ECFAEE76E15670A7EE;
- repaired candidate:
  D4F4FEEA48BB27BEFFF9613521B304DE1D319424138FC70E0802B4444F244E6A;
- repaired durable kernel:
  D8BCFAF33B02DB1FD306CEA926EEB57603D1F96C8FA80300B62B2BC8F6A65993;
- allocation/incidence post-repair verification:
  856C9F6112962820B3E39C0E4E600CB0A8921311EAA39E99CF002E504E8AB700;
- power/operator/owner post-repair verification:
  3FFDE6A915C2BBF82AE9E30723F28637796243C73D49F0094DFD561C8B52257C;
- blind post-unmask post-repair verification:
  8FCF215032573B9D518CCF1BF2ACF613F0448AB400A76520557DC75C14B4712B.

All three final seam verdicts are PASS. The initial REPAIR reviews remain
preserved as evidence of the corrections. No theorem, target-safe sector,
parent, bridge, global estimate, or exponent is promoted by this control.


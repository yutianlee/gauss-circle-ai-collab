# Blind rederivation of the full two-adic orbit convolution

## 1. Result

Put \(L=2^{\nu-1}\), and let \(\rho_j\) denote the packet's local reindexing of the row \(\mathcal R_x(\theta)\) along \(x\equiv1+2j\pmod {2^\nu}\).  The ordered four-residue orbit is

\[
 Q_j=\bigl(1+2j,\,1+2(j-a),\,1+2(j-v),\,1+2(j-v-c)\bigr)
       \pmod {2^\nu},
\]

and has exactly \(L\) elements.  With the two pair sequences in the packet, its literal four-row weighted cyclic sum is

\[
 \begin{aligned}
 S(a,c,v)
   &=\sum_{j\bmod L}w_jF_j\overline{G_{j-v}}\\
   &=\sum_{j\bmod L}e_{2^\nu}\!\left(u(1+2j)+K\Phi(1+2j)\right)
      \rho_j\overline{\rho_{j-a}}\overline{\rho_{j-v}}\rho_{j-v-c}.
 \end{aligned}
\]

For the nonunitary length-\(L\) DFT fixed below, the exact three-factor convolution is

\[
 \boxed{
 S(a,c,v)=\frac1{L^2}
 \sum_{\substack{r,s,t\bmod L\\r+s-t=0}}
 \widehat w(r)\widehat F(s)\overline{\widehat G(t)}e_L(tv).}
\]

This identity, the orbit length, the conditional period/support statements below, and the coefficient-free Cauchy bound are the exact survivors of the supplied data.  No actual character, lower period, spectral alignment, owner coefficient, or downstream cancellation follows without the omitted literal data.

## 2. Exact statement and hypotheses

All indices and frequencies in this report lie in \(\mathbb Z/L\mathbb Z\), and

\[
 \widehat H(r):=\sum_{j\bmod L}H_j e_L(-rj),
 \qquad
 H_j=\frac1L\sum_{r\bmod L}\widehat H(r)e_L(rj).
\]

The hypotheses used are exactly \(M=2^\nu N\), \(\nu\ge2\), \(N\) odd, \(A=2a\), \(B_2=2c\), \(V=2v\), and the packet's assertion that the displayed local rows and phase form well-defined length-\(L\) sequences.  The normalization \(M^{-1}\) is already inside each \(\rho_j\); it creates no additional factor of \(L\).

Writing \((\tau_vG)_j=G_{j-v}\), define the exact sesquilinear frequency channel

\[
 C_r(v):=\widehat{F\,\overline{\tau_vG}}(-r)
 =\frac1L\sum_{s\bmod L}
     \widehat F(s)\overline{\widehat G(r+s)}e_L((r+s)v).
\]

Then an equivalent exact form is

\[
 S(a,c,v)=\frac1L\sum_{r\bmod L}\widehat w(r)C_r(v).
\]

If \(\widehat\rho\) is the DFT of the local row sequence, the pair transforms are

\[
 \widehat F(s)=\frac1L\sum_{p\bmod L}
  \widehat\rho(p+s)\overline{\widehat\rho(p)}e_L(pa),
 \qquad
 \widehat G(t)=\frac1L\sum_{q\bmod L}
  \widehat\rho(q+t)\overline{\widehat\rho(q)}e_L(qc).
\]

Consequently the completely expanded four-row formula, including every \(L\)-factor, is

\[
 \boxed{
 S(a,c,v)=\frac1{L^4}
 \sum_{\substack{r,\alpha,\beta,\gamma,\delta\bmod L\\
                   r+\alpha-\beta-\gamma+\delta=0}}
 \widehat w(r)\widehat\rho(\alpha)\overline{\widehat\rho(\beta)}
 \overline{\widehat\rho(\gamma)}\widehat\rho(\delta)
 e_L\!\left(\beta a-\delta c+(\gamma-\delta)v\right).}
\]

## 3. Proof or derivation, including the case classification

The map \(j\mapsto1+2j\) is a bijection from \(\mathbb Z/L\mathbb Z\) to the odd residues modulo \(2^\nu\): two parameters have the same image exactly when \(2(j-j')\equiv0\pmod {2^\nu}\), equivalently \(j-j'\equiv0\pmod L\).  Subtracting \(A,V,V+B_2\) gives the other three displayed components of \(Q_j\).  The first component alone shows that the ordered orbit cannot close earlier, so its length remains \(L\), including repeated-shift or other degenerate choices of \(a,c,v\).

Insert DFT inversion for \(w_j,F_j,\overline{G_{j-v}}\).  The conjugated shifted factor contributes \(e_L(tv)\overline{\widehat G(t)}\), and

\[
 \sum_{j\bmod L}e_L((r+s-t)j)
 =L\,\mathbf 1_{r+s-t=0}.
\]

Three inverse transforms contribute \(L^{-3}\), while orthogonality returns one \(L\), giving precisely \(L^{-2}\).  Applying the same product calculation to \(F\) and \(G\) gives their two \(L^{-1}\) formulas and hence the fully expanded factor \(L^{-4}\).

The cases requested in the packet are exact only in the following conditional sense.

- **Single-character and constant cases.**  One has \(w_j=w_0e_L(qj)\) for some \(q\) if and only if the phase increments obey

  \[
  2u+K\bigl(\Phi(1+2(j+1))-\Phi(1+2j)\bigr)
       \equiv2q\pmod {2^\nu}
  \]

  for every \(j\).  Then \(\widehat w(r)=Lw_0\mathbf1_{r=q}\) and

  \[
  S(a,c,v)=\frac{w_0}{L}\sum_{t\bmod L}
       \widehat F(t-q)\overline{\widehat G(t)}e_L(tv).
  \]

  The constant case is the trivial character \(q=0\).  It is not licensed merely by the phrase “global \(u=0\) coefficient,” because the \(K\Phi\) increments remain and the owner predicate is absent.

- **Lower-period case.**  For a divisor \(T\mid L\), \(w\) has period \(T\) exactly when

  \[
  2uT+K\bigl(\Phi(1+2(j+T))-\Phi(1+2j)\bigr)
       \equiv0\pmod {2^\nu}
  \]

  for every \(j\).  In that event

  \[
  \operatorname{supp}\widehat w\subseteq
     \{mL/T:0\le m<T\},
  \qquad
  \widehat w(mL/T)=\frac LT\sum_{j=0}^{T-1}w_j e_T(-mj),
  \]

  and therefore

  \[
  S=\frac1{L^2}\sum_{m=0}^{T-1}\widehat w(mL/T)
       \sum_{\substack{s,t\bmod L\\mL/T+s-t=0}}
       \widehat F(s)\overline{\widehat G(t)}e_L(tv).
  \]

  Fundamental period \(T\) does not force every one of these \(T\) allowed coefficients to be nonzero.

- **Aligned case.**  Let \(W=\operatorname{supp}\widehat w\), \(P=\operatorname{supp}\widehat F\), and \(Q=\operatorname{supp}\widehat G\).  A necessary support alignment is a triple \((r,s,t)\in W\times P\times Q\) with \(r+s-t=0\).  If no such triple exists, then \(S=0\) exactly.  The exact channel-level alignment is \(\widehat w(r)C_r(v)\ne0\).  Nonempty support alignment alone does not imply \(S\ne0\), because the sum defining \(C_r(v)\), and then the sum over \(r\), may cancel.  If exactly one triple survives, its contribution is exactly \(L^{-2}\widehat w(r)\widehat F(s)\overline{\widehat G(t)}e_L(tv)\).

- **Generic case.**  With no increment or owner information, \(W\) may be all of \(\mathbb Z/L\mathbb Z\), so the full constrained convolution is irreducible.  Since \(|w_j|=1\), the weakest coefficient-free estimate is

  \[
  |S|\le \|F\|_2\|G\|_2
  =\frac1L
    \left(\sum_s|\widehat F(s)|^2\right)^{1/2}
    \left(\sum_t|\widehat G(t)|^2\right)^{1/2}.
  \]

Finally, mod-\(8\) data cannot normally determine the full phase.  Translation by four in \(j\), which preserves \(x\pmod8\), has ratio

\[
 \frac{w_{j+4}}{w_j}
 =e_{2^\nu}\!\left(8u+K(\Phi(1+2j+8)-\Phi(1+2j))\right),
\]

and mod-\(8\) information does not force this ratio to be one.  More generally, replacing \(\Phi\) by \(\Phi+8Q\) leaves all reductions modulo \(8\) unchanged but multiplies the weight by

\[
 e_{2^\nu}(8KQ)=e_{2^{\nu-3}}(KQ),
\]

which can be nontrivial for \(\nu\ge4\).  For \(\nu=2,3\), reduction modulo \(8\) does determine a phase modulo \(2^\nu\); this endpoint exception does not extend to the full family \(\nu\ge2\).

## 4. First doubtful or unproved step

There is no doubtful algebraic step in the parametric orbit and DFT identities.  The first unavailable inference is the identification of the actual weight spectrum: the packet supplies neither the literal owner predicate selecting the relevant mask and its \((u,K,\Phi)\) data nor the values of \(\Phi(1+2j)\pmod {2^\nu}\) on the whole orbit.  Thus one cannot decide whether the actual weight is constant, a character, lower-period, aligned, or generic, and one cannot attach a global coefficient or multiplicity.  The statement packet did not display the coupling operator between the two pair sequences; the conductor's seam comparison has now resolved that ambiguity in favor of the canonical sesquilinear coupling \(F_j\overline{G_{j-v}}\), which is used throughout this corrected report.

## 5. Required control test and outcome

The factor-and-shift control is exact rather than numerical.  Take

\[
 w_j=C e_L(r_0j),\qquad F_j=e_L(s_0j),\qquad G_j=e_L(t_0j).
\]

Direct summation gives \(S=CL e_L(t_0v)\) when \(r_0+s_0-t_0=0\), and \(S=0\) otherwise.  In the DFT formula the three transforms are \(CL,L,L\) at their respective frequencies, so \(L^{-2}(CL)(L)(L)e_L(t_0v)\) gives exactly the same answer.  This checks the \(L^{-2}\) normalization, the conjugation, and the sign of the translation factor.  The constant degeneracy \(r_0=s_0=t_0=0\) returns \(CL\), not \(C\) or \(CL^2\).

For the mod-\(8\) control, let \(\nu\ge4\), \(u=0\), \(K=1\), and compare

\[
 \Phi_0(1+2j)=0,
 \qquad
 \Phi_1(1+2j)=8j\pmod {2^\nu}.
\]

They have identical mod-\(8\) data, but \(w^{(0)}_j=1\) while
\(w^{(1)}_j=e_{2^\nu}(8j)=e_L(4j)\).  Their DFT supports are respectively \(\{0\}\) and \(\{4\}\).  Thus the proposed coarse-to-full-phase inference fails by an explicit symbolic control, while the conditional DFT formulas remain invariant.  These controls also cover the relevant `support-and-degeneracy` and `coefficient-adversary` requirements without using numerics.

## 6. Dependencies and exact artifacts used

The derivation used only:

- `problems/gauss_circle.md`;
- `state/control_models.md`;
- `rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/blind_statement.md`;
- `rounds/codex-managed/m9-m1-full-two-adic-orbit-convolution/briefs/blind_full_two_adic_orbit_rederivation.md`.

No proof graph, active-state file, earlier Round-101 derivation, sibling report, validation matrix, or synthesis file was read or used.

The sole additional datum used in this correction was the conductor's seam-resolution instruction that the canonical physical coupling is \(F_j\overline{G_{j-v}}\); no additional artifact was opened.

## 7. Recommended state effect

**Promote, after a seam check,** the length-\(L\) ordered-orbit lemma and the two boxed parametric DFT identities, including the character/period support implications.  **Retain conditionally** every case label until the full \(\Phi\)-table and literal owner predicate are supplied.  **Reject** any claim that mod-\(8\) phase data alone determine the full \(2^\nu\) weight for \(\nu\ge4\), and make no downstream theorem change from this blind report.

# 1. Result.

The exact finite Abel decomposition has opposite orientations on the two
signed blocks.  If

\[
 I=\{n\in\mathbb Z:V<n\leq 2V\}=[a,b]\cap\mathbb Z,
 \qquad \alpha=-\frac{i(1+i)}{2Nq},
\]

then the positive block uses the prefix
\(P_j(v)=\sum_{s=a}^{j}K(-v^2,-s;c)\), whereas the negative block uses
the suffix
\(S_j(v)=\sum_{s=j}^{-a}K(-v^2,-s;c)\).  The moving cells are, with the
stated closed lower endpoints,

\[
 C_j^+(x)={\bf1}_{[j+1,j+2)}(x)F_j(x),\qquad
 C_j^-(x)={\bf1}_{[-j,-j+1)}(x)F_j(x).
\]

On the physical integer lattice they are respectively the single
coordinates \(x=j+1\) and \(x=-j\).  There are also two indispensable
outer Abel terms: the row \(j=b\), cut off at \(x=b+1\), and the row
\(j=-b\), cut off at \(x=b\).

With the unnormalised \(q\)-Fourier convention specified below and the
full half-period inverse identity in its character-quotient
normalisation, the two full-frequency moving-cell traces are exactly

\[
 \mathcal C_+^{\rm all}
 =\sum_{k=a+1}^{b}F_{k-1}(k)
   \sum_{s=a}^{k-1}{\bf1}_{N\mid k^2-s}
      \chi _4\!\left(\frac{k^2-s}{N}\right),                                      \tag{1.1}
\]

\[
 \mathcal C_-^{\rm all}
 =\sum_{k=a}^{b-1}F_{-k}(k)
   \sum_{s=-k}^{-a}{\bf1}_{N\mid k^2-s}
      \chi _4\!\left(\frac{k^2-s}{N}\right).                                      \tag{1.2}
\]

The endpoint congruences govern only \(s=k-1\) in (1.1) and
\(s=-k\) in (1.2).  The strict ranges \(a\le s\le k-2\) and
\(-k+1\le s\le-a\) survive.  Hence endpoint roots do **not** control
the whole moving-cell trace.  The outer Abel terms survive as well.
The hypotheses supplied for \(F_j\) give only absolute-capacity bounds
for these sums and furnish no cancellation theorem for the strict
survivors.  Thus the requested full trace estimate cannot be certified
from the statement alone; the rigorous outcome is this exact
decomposition and a no-go for an endpoint-root-only proof.

# 2. Exact statement and hypotheses.

Write \(e_m(t)=e^{2\pi i t/m}\), and extend \(\chi _4\) by zero off the
odd integers.  The physical/Fourier convention used in this report is

\[
 \widehat G(h)=\sum_{x\in\mathbb Z}G(x)e_q(-hx),
 \qquad e_q(-2dvx)=e_c(-2vx),\qquad c=q/d.                         \tag{2.1}
\]

The sum is harmless for a zero-extended profile and automatically
periodises if its support crosses a \(q\)-boundary.  Under (2.1), the
full half-period inverse identity needed below is

\[
 \begin{aligned}
 &\alpha\sum_{\substack{d\mid N\\d\ \mathrm{odd}}}
 \chi _4(d)d\sqrt{c_d}\sum_{v\bmod H_d}
 \widehat G(2dv)K(-v^2,-s;c_d)\\
 &\hspace{25mm}=
 \sum_{x\in\mathbb Z}G(x)\,
 {\bf1}_{N\mid x^2-s}\chi _4\!\left(\frac{x^2-s}{N}\right),
 \qquad c_d=\frac{q}{d},\quad H_d=\frac{c_d}{2}.                  \tag{2.2}
 \end{aligned}
\]

Thus the physical kernel is

\[
 \Xi_N(x,s):={\bf1}_{N\mid x^2-s}
              \chi _4\!\left(\frac{x^2-s}{N}\right).            \tag{2.3}
\]

Formula (2.2) fixes the external scalar seam: since \(q=4N\),

\[
 \alpha=-\frac{i(1+i)}{2Nq}=-\frac{2i(1+i)}{q^2}.                 \tag{2.4}
\]

No normalising factor \(q^{-1}\) occurs in (2.1).  If the intended
definition of \(\widehat G\) contains such a factor, every physical
formula in this report acquires the corresponding compensating power
of \(q\); this is not a cosmetic change.

For the profile, define merely as an identity

\[
 A_j(x):=F_j(x)e\!\left(-\sqrt{x^2-j}+x\right),\qquad
 F_j(x)=A_j(x)e\!\left(\sqrt{x^2-j}-x\right).                    \tag{2.5}
\]

Here \(A_j\) retains, without alteration, every zero extension, BV
piece, transition, half-open convention, and outer endpoint present in
the given \(F_j\).  In particular, it is not assumed to be a function
of the quotient \((x^2-s)/N\).  Put

\[
 \eta\ll_\varepsilon M^{-3/4}X^\varepsilon,qquad
 S\ll_\varepsilon KX^\varepsilon,qquad L=|I|\le V+1.            \tag{2.6}
\]

All exact identities below hold for arbitrary \(N\), every odd
\(d\mid N\), both members of every complementary interior pair, and
both signs.  The estimates use only (2.6), except where a standard
Kloosterman bound is explicitly stated as an additional hypothesis.

# 3. Proof or derivation.

For fixed \(d,v\), abbreviate
\(T_s=K(-v^2,-s;c)\).  Finite summation by parts gives, on the positive
block,

\[
 \sum_{j=a}^{b}\widehat B_j(2dv)T_j
 =\widehat B_b(2dv)P_b(v)
  +\sum_{j=a}^{b-1}\bigl(\widehat B_j(2dv)-
                  \widehat B_{j+1}(2dv)\bigr)P_j(v),              \tag{3.1}
\]

\[
 P_j(v)=\sum_{s=a}^{j}T_s.                                       \tag{3.2}
\]

The pointwise difference, with no endpoint discarded, is

\[
 B_j-B_{j+1}
 ={\bf1}_{x\ge j+2}(F_j-F_{j+1})
  +{\bf1}_{[j+1,j+2)}F_j.                                       \tag{3.3}
\]

For the negative block let \(j_0=-b\) and \(u=-a\).  Reverse Abel
summation gives

\[
 \sum_{j=j_0}^{u}\widehat B_j(2dv)T_j
 =\widehat B_{j_0}(2dv)S_{j_0}(v)
  +\sum_{j=j_0+1}^{u}\bigl(\widehat B_j(2dv)-
                  \widehat B_{j-1}(2dv)\bigr)S_j(v),              \tag{3.4}
\]

\[
 S_j(v)=\sum_{s=j}^{u}T_s,                                       \tag{3.5}
\]

and

\[
 B_j-B_{j-1}
 ={\bf1}_{x\ge -j+1}(F_j-F_{j-1})
  +{\bf1}_{[-j,-j+1)}F_j.                                      \tag{3.6}
\]

Equations (3.1)--(3.6) prove the prefix/suffix directions and show why
the lower endpoint in each moving cell is included.  Applying the
linear identity (2.2) to each selected \(s\) gives the complete
physical decomposition

\[
 \begin{aligned}
 \mathcal E_+^{\rm all}
 &=\sum_{x\ge b+1}F_b(x)\sum_{s=a}^{b}\Xi_N(x,s),\\
 \mathcal R_+^{\rm all}
 &=\sum_{j=a}^{b-1}\sum_{x\ge j+2}(F_j(x)-F_{j+1}(x))
                       \sum_{s=a}^{j}\Xi_N(x,s),\\
 \mathcal C_+^{\rm all}
 &=\sum_{j=a}^{b-1}F_j(j+1)\sum_{s=a}^{j}\Xi_N(j+1,s),           \tag{3.7}
 \end{aligned}
\]

and

\[
 \begin{aligned}
 \mathcal E_-^{\rm all}
 &=\sum_{x\ge b}F_{-b}(x)\sum_{s=-b}^{-a}\Xi_N(x,s),\\
 \mathcal R_-^{\rm all}
 &=\sum_{j=-b+1}^{-a}\sum_{x\ge -j+1}(F_j(x)-F_{j-1}(x))
                       \sum_{s=j}^{-a}\Xi_N(x,s),\\
 \mathcal C_-^{\rm all}
 &=\sum_{j=-b+1}^{-a}F_j(-j)\sum_{s=j}^{-a}\Xi_N(-j,s).          \tag{3.8}
 \end{aligned}
\]

Every \(x\)-sum in (3.7)--(3.8) is also restricted by the exact
zero-extended support of the displayed profile.  In particular, the
two outer terms are not moving cells and cannot be deleted by a test
of the moving endpoint congruence.

Putting \(k=j+1\) in (3.7), and \(k=-j\) in (3.8), proves (1.1)--(1.2).
The strict survivors, with all inequalities exposed, are

\[
 \begin{aligned}
 \mathcal S_+^{\rm all}
 &=\sum_{k=a+2}^{b}F_{k-1}(k)
   \sum_{s=a}^{k-2}{\bf1}_{N\mid k^2-s}
       \chi _4\!\left(\frac{k^2-s}{N}\right)\\
 &=\sum_{k=a+2}^{b}A_{k-1}(k)
   e\!\left(\sqrt{k^2-k+1}-k\right)
   \sum_{\substack{\ell\in\mathbb Z\\a\le k^2-N\ell\le k-2}}
       \chi _4(\ell),                                           \tag{3.9}
 \end{aligned}
\]

\[
 \begin{aligned}
 \mathcal S_-^{\rm all}
 &=\sum_{k=a+1}^{b-1}F_{-k}(k)
   \sum_{s=-k+1}^{-a}{\bf1}_{N\mid k^2-s}
       \chi _4\!\left(\frac{k^2-s}{N}\right)\\
 &=\sum_{k=a+1}^{b-1}A_{-k}(k)
   e\!\left(\sqrt{k^2+k}-k\right)
   \sum_{\substack{\ell\in\mathbb Z\\-k+1\le k^2-N\ell\le-a}}
       \chi _4(\ell).                                           \tag{3.10}
 \end{aligned}
\]

In (3.9)--(3.10), \(\ell=(k^2-s)/N\) is the character quotient.  The
coefficient multiplying it is the boundary sample \(F_{k-1}(k)\) or
\(F_{-k}(k)\), not a weight that may be renamed as a function of
\(\ell\).  The exact diagonal pieces omitted from (3.9)--(3.10) are

\[
 \sum_{k=a+1}^{b}F_{k-1}(k)
 {\bf1}_{N\mid k^2-k+1}\chi _4\!\left(\frac{k^2-k+1}{N}\right),  \tag{3.11}
\]

\[
 \sum_{k=a}^{b-1}F_{-k}(k)
 {\bf1}_{N\mid k^2+k}\chi _4\!\left(\frac{k^2+k}{N}\right).    \tag{3.12}
\]

The negative-row phase in (3.10) is
\(e(\sqrt{k^2+k}-k)\); it follows directly from
\(j=-k,x=k\).  Thus (3.9)--(3.12) retain the two signs and their
different endpoint phases.

For completeness, the special-frequency subtraction can be done
before any estimate.  For each \(d\), let \(w_0=0\) and
\(w_*=H/2=c/4\).  Its exact physical kernel contributions are

\[
 \Theta_{d,0}(x,s)=\alpha\chi _4(d)d\sqrt c\,K(0,-s;c),           \tag{3.13}
\]

\[
 \Theta_{d,*}(x,s)=\alpha\chi _4(d)d\sqrt c\,(-1)^x
                   K(-c^2/16,-s;c).                              \tag{3.14}
\]

Consequently every formula (3.7)--(3.12) for the interior row is
obtained by replacing \(\Xi_N\) with
\(\Xi_N-\sum_d(\Theta_{d,0}+\Theta_{d,*})\).  This is a direct
subtraction for the Abel piece itself, not a transfer of a theorem for
a whole row.

If \(K\) is the standard (unnormalised) Kloosterman sum, then

\[
 |K(-w^2,-s;c)|\le \tau(c)c^{1/2}(g_w,s)^{1/2},\qquad
 g_w=(w^2,c),                                                     \tag{3.15}
\]

and, for an interval \(J\) of length at most \(L\),

\[
 \sum_{s\in J}(g,s)^{1/2}
 \le \tau(g)(L+\sqrt g).                                        \tag{3.16}
\]

Each selected \(s\) occurs in at most \(L\) moving cells.  Using
\(dc=q\) in the external scalar therefore gives, separately for
\(w=0,c/4\),

\[
 |\mathcal C^{(w)}_{d,+}|+|\mathcal C^{(w)}_{d,-}|
 \ll \frac{\eta L}{N}\tau(c)\tau(g_w)(L+\sqrt{g_w}),             \tag{3.17}
\]

where

\[
 g_0=c,\qquad
 g_*=(c^2/16,c)=n(n,4),\qquad n=N/d.                              \tag{3.18}
\]

The two outer endpoint profiles have at most \(S\) physical
coordinates, so their corresponding separate costs are

\[
 |\mathcal E^{(w)}_{d,+}|+|\mathcal E^{(w)}_{d,-}|
 \ll \frac{\eta S}{N}\tau(c)\tau(g_w)(L+\sqrt{g_w}).             \tag{3.19}
\]

Summing (3.17)--(3.19) over odd \(d\mid N\), and using
\(\sqrt{g_w}\le\sqrt c=2\sqrt{N/d}\), yields the transparent
capacity bounds

\[
 \mathcal C^{(w)}
 \ll_\varepsilon M^{-3/4}(NX)^\varepsilon
 \left(\frac{L^2\tau_o(N)}{N}
       +\frac{L\sigma^{(o)}_{-1/2}(N)}{\sqrt N}\right),          \tag{3.20}
\]

\[
 \mathcal E^{(w)}
 \ll_\varepsilon M^{-1/4}(NX)^\varepsilon
 \left(\frac{L\tau_o(N)}{\sqrt N}
       +\sigma^{(o)}_{-1/2}(N)\right).                           \tag{3.21}
\]

Here \(\tau_o(N)\) counts odd divisors and
\(\sigma^{(o)}_{-1/2}(N)=\sum_{d\mid N,\ d\ \mathrm{odd}}d^{-1/2}\).
These are upper capacities, not signed cancellation.  If (3.15) is
not among the intended hypotheses, the elementary bound \(|K|\le c\)
still gives the rigorous but weaker cell cost
\(\ll \eta L^2N^{-1}\sum_{d\mid N,\,d\ \mathrm{odd}}c_d^{1/2}\),
and the analogous outer cost with \(L^2\) replaced by \(SL\).

It remains to classify the two endpoint congruences.  For
\(f_+(j)=j^2+j+1\):

* modulo \(2^e\) there is no root for any \(e\ge1\);
* modulo \(3\) the unique root is \(j\equiv1\), while there is no
  root modulo \(3^e\) for \(e\ge2\), since
  \(f_+(1+3t)=3+9t+9t^2\not\equiv0\pmod9\);
* for \(p\ne2,3\), roots exist exactly when \(p\equiv1\pmod3\).
  They are the two nontrivial cube roots of unity modulo \(p\), are
  simple because \(2j+1\not\equiv0\pmod p\), and each has a unique
  lift modulo every \(p^e\).

Thus \(f_+(j)\equiv0\pmod N\) is solvable precisely when \(N\) is
odd, \(v_3(N)\le1\), and every prime \(p\ne3\) dividing \(N\)
satisfies \(p\equiv1\pmod3\).  For \(N>1\) it then has
\(2^{\omega(N/3^{v_3(N)})}\) roots.

For \(f_-(j)=j(j-1)\), coprimality of consecutive integers shows that
the roots modulo every prime power \(p^e\), including powers of two,
are exactly \(0\) and \(1\).  CRT therefore gives all idempotents:
there are \(2^{\omega(N)}\) roots modulo \(N>1\), not merely the two
global classes \(0,1\) when \(N\) is composite.

Finally, these classifications concern only (3.11)--(3.12).  A strict
positive control is obtained by taking \(s=k-2\) and
\(N=k^2-k+2\): then \(N\mid k^2-s\), while
\(k^2-(k-1)=N-1\).  A strict negative control takes \(s=-k+1\) and
\(N=k^2+k-1\): then \(N\mid k^2-s\), while
\(k^2-(-k)=N+1\).  Hence a strict selected coordinate can be resonant
when the corresponding endpoint is not.

# 4. First doubtful or unproved step.

The first unproved seam is the exact normalisation of (2.2).  The blind
statement does not define \(\widehat G\), does not define the
Kloosterman/theta sum denoted by \(K\), and says only that a full
half-period inverse identity is available, without stating its sign or
normalising powers.  The scalar check

\[
 {\bf1}_{N\mid t}\chi _4(t/N)
 =-\frac{2i}{q}\sum_{r\bmod q}\chi _4(r)e_q(rt),
 \qquad q=4N,                                                     \tag{4.1}
\]

together with one unnormalised Fourier inversion and the usual
\((1+i)\sqrt c\) quadratic Gauss factor produces exactly
\(-2i(1+i)/q^2=\alpha\), so (2.2) is the natural and externally
consistent normalisation.  Nevertheless, matching the remaining
Gauss multiplier to the particular object called \(K\) cannot be
certified without its definition or the stated inverse identity.

Even granting (2.2), no numerical target bound for the trace is stated,
and no hypothesis relates the arbitrary boundary samples
\(F_{k-1}(k),F_{-k}(k)\) to the quotient \(\ell\).  Therefore (3.9) and
(3.10) cannot be improved beyond capacity by the supplied data.  This
is the first mathematical obstruction after the normalisation seam.

# 5. Required control tests and outcomes.

1. **One- and two-row Abel controls — pass.**  Substituting a one-row
   interval in (3.1) or (3.4) leaves exactly the stated outer term.
   For two rows, expanding the right sides cancels the intermediate
   partial sum and recovers both original summands.  Evaluating
   (3.3) at \(x=j+1\), \(x=j+2\), and outside both cutoffs gives
   respectively \(F_j\), \(F_j-F_{j+1}\), and zero; (3.6) behaves
   analogously.

2. **Strict endpoint inequalities — pass.**  Positive cells have
   \(k\in[a+1,b]\), selected \(s\in[a,k-1]\), and strict survivor
   \(s\le k-2\), which is empty at \(k=a+1\).  Negative cells have
   \(k\in[a,b-1]\), selected \(s\in[-k,-a]\), and strict survivor
   \(s\ge-k+1\), which is empty at \(k=a\).  The omitted rows are
   exactly the separate outer rows \(b\) and \(-b\).

3. **Prime-power and CRT controls — pass.**  Direct reduction modulo
   \(2\), modulo \(3\), and modulo \(9\) gives the exceptional cases
   for \(j^2+j+1\); the cube-root argument and Hensel lifting give all
   other odd prime powers.  Coprimality of \(j,j-1\) gives both roots
   modulo every prime power for \(j^2-j\), and CRT gives all mixed
   idempotents.

4. **Strict-survivor adversarial controls — fail for the proposed
   endpoint-root mechanism.**  The two constructions at the end of
   Section 3 have a strict resonant \(s\) and a nonresonant endpoint.
   They can be placed inside a nonempty strict block by taking \(k\)
   large and choosing \(V\) with \(a+2\le k\le b\) (positive) or
   \(a+1\le k\le b-1\) (negative).  Because the statement permits
   arbitrary bounded complex profiles, one may support the relevant
   boundary sample and set the others to zero.  No signed cancellation
   then remains to be inferred.

5. **Support localisation — no comparability conclusion.**  A
   nonzero cell trace says only that the relevant physical support
   contains \(k\asymp V\).  Its span is at most \(O(KX^\varepsilon)\),
   and the hypotheses already give \(V\le K\), but neither the support
   location nor a lower bound for its span is given.  Thus trace
   support does not force \(V\asymp K\).  In particular it supplies no
   cancellation in the character quotient sum.

6. **Zero/Nyquist and complementary representatives — pass.**  The
   factors in (3.13)--(3.14) are respectively \(1\) and \((-1)^x\).
   Equations (3.17)--(3.21) estimate the two Abel pieces directly.
   The full sum contains both \(v\) and \(H-v\); neither is discarded
   or identified before summation.  Removing \(0,H/2\) therefore
   leaves both representatives of each ordinary pair.

7. **Edge case \(c=4\) — pass.**  Here \(H=2\) and
   \(\mathcal V_d^\circ=(\mathbb Z/2\mathbb Z)\setminus\{0,1\}) is
   empty.  This case occurs only for \(d=N\), hence only when that
   divisor is odd.  Its interior trace is exactly zero, while its full
   trace is exactly the sum of the separately displayed zero and
   Nyquist traces; no generic paired-interior estimate may count it.

8. **Absolute capacity — pass, but not a target proof.**  From
   (1.1)--(1.2), each fixed \(k\) selects at most
   \(1+L/N\) values of \(s\).  Hence the full moving-cell trace has
   absolute capacity \(O(\eta L(1+L/N))\) per sign.  This is a count,
   not cancellation in \(\chi _4\), and the special-frequency and
   outer capacities must still be subtracted as in Section 3.

# 6. Dependencies and exact artifacts used.

The only repository artifacts read were:

* `protocol.md`;
* `rounds/codex-managed/m9-m1-lower-cone-t1-d1-paired-interior-cell-trace-gate/blind_statement.md`.

No proof graph, campaign strategy, claimant seed, task brief, sibling
report, previous Round-158 artifact, proof draft, synthesis, or shared
state file was inspected.  The algebraic dependencies are finite Abel
summation, CRT, the elementary prime-power analysis written out above,
and the character selector (4.1).  Bounds (3.17)--(3.21) additionally
depend on the standard unnormalised Kloosterman interpretation and its
Weil bound (3.15); if that interpretation is not the intended one,
only the explicitly stated trivial-bound fallback should be retained.

# 7. Recommended state effect.

**Retain/revise, but do not promote the full trace target.**  Retain as
candidate lemmas the exact prefix/suffix Abel identities, the two
moving-cell and two outer-endpoint formulas, the literal strict
survivor formulas (3.9)--(3.10), the special-frequency subtraction, the
\(c=4\) empty-interior control, and the complete prime-power root
classification.  Reject the claim that the roots of
\(j^2+j+1\) and \(j^2-j\) control the whole trace.  Before any stronger
state change, supply and audit the precise Fourier/Kloosterman
definitions and (2.2), state the desired trace right-hand side, and
prove a new estimate for the signed quotient sums in (3.9)--(3.10) and
for the outer terms.  A whole-row zero or Nyquist theorem is not a
substitute for those piece-specific estimates.

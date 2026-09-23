# Round 197 blind four-corner commutator rederivation

## 1. Result

**Result: exact algebraic classification, followed by a rigorous route no-go at the first literal-support commutator.**

Write

\[
 A=\alpha m,\qquad B=\beta m',\qquad N=gA,\qquad N+r=gB.
\]

The three displayed cross-coprimality assumptions are exactly the three
extra gcd conditions needed, in addition to \((\alpha,\beta)=1\), for
all four recomputed gcds to be \(g\).  They also imply, using the parity
conditions in the statement, that every divisor occurring at a corner
is odd.  The two allocation inequalities defining \(P_2\) are invariant
under both swaps.  The algebraic swaps are commuting involutions; in the
sector \(s_0=s_1=-1\) their orbit is automatically free.

If

\[
 w=\chi _4(\alpha\beta),
\]

then the character weights at \((00),(10),(01),(11)\) are

\[
 w,\quad ws_0,\quad ws_1,\quad ws_0s_1.
\]

Consequently the actual character-weighted orbit in the sector
\(s_0=s_1=-1\) is **\(w\) times** the alternating rectangle.  It is the
displayed alternating rectangle itself only after either retaining and
factoring out this common sign or imposing \(\chi _4(\alpha\beta)=1\).
The sign \(w\) is not forced by the hypotheses.  Also,

\[
 s_0=s_1\iff r\equiv0\pmod4,
 \qquad
 s_0\ne s_1\iff r\equiv2\pmod4.
\]

In particular, \(s_0=s_1=-1\) implies \(4\mid r\), but \(4\mid r\)
also permits \(s_0=s_1=1\).

For the actual zero-extended endpoint coefficients, the alternating
rectangle factors exactly as stated.  There is no algebraic
commutator in this factorization.  The commutators first appear when one
tries to replace the actual lower endpoint difference by the difference
of its certified smooth factor.  A literal-support exit contributes an
undifferenced endpoint coefficient, and a BV or discrete-field change
contributes its own exact commutator.  Neither is controlled by
pointwise \(C^1\) regularity of the smooth factor.

Thus the intended ledger is correct on a lower-swap-stable common cell
after all nonsmooth commutators are separately controlled:

\[
 \frac{D_L}{L}\,(D_LL^2)=D_L^2L\le 4L^2\qquad(L\ge1).
\]

It does not cover the complement.  On the first lower support exit the
only available envelope remains \(D_LL^2X^\varepsilon\), too large by a
factor comparable with \(D_L\).  The supplied hypotheses neither prove
that this exit is empty nor bound its aggregate by \(O(L^2X^\varepsilon)\).
Therefore a whole-sector \(O(L^2X^\varepsilon)\) conclusion does not
follow from the isolated statement.  This is a no-go for the proposed
smooth-displacement route, not a claim that the actual endpoint theorem
is false.

## 2. Exact statement and hypotheses

For a corner \((i,j)\in\{0,1\}^2\), let the lower factor pair be

\[
 (a_i,\bar a_i)=
 \begin{cases}
 (\alpha,m),&i=0,\\
 (m,\alpha),&i=1,
 \end{cases}
\]

and the upper factor pair be

\[
 (b_j,\bar b_j)=
 \begin{cases}
 (\beta,m'),&j=0,\\
 (m',\beta),&j=1.
 \end{cases}
\]

The corner has divisors \((ga_i,gb_j)\) and complementary factors
\((\bar a_i,\bar b_j)\).  The following assertions use only the physical
and candidate hypotheses in the isolated statement.

1. The four recomputed gcds are

   \[
   \begin{array}{c|cc}
     &j=0&j=1\\ \hline
   i=0&g(\alpha,\beta)&g(\alpha,m')\\
   i=1&g(m,\beta)&g(m,m').
   \end{array}
   \]

   Hence, because \((\alpha,\beta)=1\), all four equal \(g\) if and
   only if

   \[
   (m,\beta)=(\alpha,m')=(m,m')=1.
   \]

2. Subject to these gcd conditions, the two maps are commuting
   involutions on normalized factorization tuples.  The orbit has four
   distinct corners if and only if \(\alpha\ne m\) and \(\beta\ne m'\).
   The second inequality follows from the strict upper \(P_2\)
   inequality.  In the sector \(s_0=-1\), the first follows because
   \(\alpha=m\) would give
   \(s_0=\chi _4(\alpha^2)=1\).  Thus the \((-1,-1)\) sector is a free
   algebraic four-corner orbit.

3. Let \(\mathsf I_L(x)\) denote the conjunction of every literal
   lower-endpoint support and zero-extension predicate for
   \(\lambda_{N,\sigma}(gx)\), and define \(\mathsf I_U(y)\) analogously
   for \(\lambda_{N+r,\sigma}(gy)\).  An original physical corner has
   \(\mathsf I_L(\alpha)=\mathsf I_U(\beta)=1\).  After the arithmetic
   conditions above, all four corners are in the complete literal
   endpoint source if and only if

   \[
   \mathsf I_L(m)=\mathsf I_U(m')=1.
   \]

   This support closure is an additional condition; it is not a
   consequence of the gcds or of \(P_2\).  Among original physical
   corners its exact disjoint support complement is

   \[
   \boxed{
   \{\mathsf I_L(m)=0\}
   \ \dot\cup\
   \{\mathsf I_L(m)=1,\ \mathsf I_U(m')=0\}.}
   \]

   Any genuinely joint literal predicate not already included in the
   two endpoint indicators would have to be intersected at all four
   corners as a further closure condition; no formula for such a
   predicate was supplied.

4. The strict lower-interior sector needed by the displacement argument
   is smaller still: both lower endpoints must be in literal support,
   must lie in one certified smooth cell, and every nonsmooth lower
   field must either agree at the two endpoints or be charged by a
   separate estimate.  Fixing any order of the literal fields gives an
   exact disjoint complement by assigning a tuple to its first failed
   item in that order.  One admissible order is: arithmetic/gcd and
   parity; opposing-source and \(P_2\); shell; strict cone; squarefree;
   literal coprimality; residual selector; profile; floor; star;
   half-weight; hard sample; crossing; endpoint mask; zero extension;
   common-cell membership; normalized BV field; and the remaining
   discrete fields.  The arithmetic and \(P_2\) exits are empty under
   the hypotheses proved above; none of the later exits is shown empty
   by the isolated statement.

If the three cross gcd assumptions were not imposed, their exact
disjoint arithmetic complement (after \((\alpha,\beta)=1\)) could, for
example, be recorded in the first-failure order

\[
\begin{aligned}
 \mathcal E_{10}&=\{(m,\beta)>1\},\\
 \mathcal E_{01}&=\{(m,\beta)=1,\ (\alpha,m')>1\},\\
 \mathcal E_{11}&=\{(m,\beta)=(\alpha,m')=1,\ (m,m')>1\}.
\end{aligned}
\]

## 3. Proof or derivation

### 3.1 Arithmetic, parity, allocation, and the action

The gcd table follows immediately from

\[
 (gx,gy)=g(x,y).
\]

It proves both necessity and sufficiency of the three cross conditions.
Moreover, the four cross coprimalities

\[
 (\alpha,\beta)=(m,\beta)=(\alpha,m')=(m,m')=1
\]

give \((A,B)=1\).  Since \(d,d'\) are odd, \(g,\alpha,\beta\) are odd.
Because

\[
 r=g(B-A)
\]

is even and \(g\) is odd, \(B-A\) is even.  Hence \(m,m'\) have the
same parity.  Their gcd is one, so they cannot both be even; both are
odd.  Thus \(gm\) and \(gm'\), as well as the original two divisors,
are odd.

At every corner the lower and upper allocation distances are

\[
 |ga_i-g\bar a_i|=g|\alpha-m|=|g\alpha-gm|
\]

and

\[
 |gb_j-g\bar b_j|=g|\beta-m'|=|g\beta-gm'|.
\]

Therefore the displayed opposing close/far allocation \(P_2\) is
exactly invariant.  The products are also invariant:

\[
 (ga_i)\bar a_i=g\alpha m=N,
 \qquad
 (gb_j)\bar b_j=g\beta m'=N+r.
\]

After gcd recomputation, \(\tau _0\) interchanges
\((\alpha,m)\), \(\tau _1\) interchanges \((\beta,m')\), and the two
operations act on disjoint pairs.  Hence

\[
 \tau _0^2=\tau _1^2=1,
 \qquad
 \tau _0\tau _1=\tau _1\tau _0.
\]

These identities prove an ambient algebraic action.  They do not prove
that the literal nonzero source is invariant; that is precisely the
support condition in Section 2.

### 3.2 Complete character table and the residue of \(r\)

Multiplicativity of \(\chi _4\) on odd numbers and
\(\chi _4(g)^2=1\) give

\[
\begin{array}{c|c|c}
 (i,j)&\chi _4(gb_j)\chi _4(ga_i)&\text{relative to }w\\ \hline
 (0,0)&\chi _4(\alpha\beta)&1\\
 (1,0)&\chi _4(m\beta)&s_0\\
 (0,1)&\chi _4(\alpha m')&s_1\\
 (1,1)&\chi _4(mm')&s_0s_1.
\end{array}
\]

Thus the four sign sectors, in corner order \((00),(10),(01),(11)\),
are

\[
\begin{array}{c|c}
 (s_0,s_1)&w^{-1}(w_{00},w_{10},w_{01},w_{11})\\ \hline
 (+,+)&(1,1,1,1)\\
 (-,+)&(1,-1,1,-1)\\
 (+,-)&(1,1,-1,-1)\\
 (-,-)&(1,-1,-1,1).
\end{array}
\]

Because \(A,B\) are odd, \(s_0\) and \(s_1\) record their respective
residue classes \(1\) or \(3\pmod4\).  Equal signs mean
\(B-A\equiv0\pmod4\); unequal signs mean
\(B-A\equiv2\pmod4\).  Multiplication by the odd number \(g\) preserves
this dichotomy, proving the stated equivalences for \(r\).

In the \((-,-)\) sector the character orbit sum is

\[
 w\{F_{00}-F_{10}-F_{01}+F_{11}\}.
\]

The common sign is genuinely undetermined.  For example, with
\(g=1,L=4,D_L=2\):

\[
 (\alpha,m,\beta,m')=(3,1,7,1)
\]

satisfies the arithmetic conditions, \(P_2\), and \(s_0=s_1=-1\), and
has \(w=1\).  In contrast,

\[
 (\alpha,m,\beta,m')=(5,3,19,1)
\]

has the same properties, with \(r=4\), but
\(w=\chi _4(95)=-1\).  Hence the unqualified claim that the actual
weighted sum equals, rather than equals \(w\) times, the alternating
rectangle is false.

### 3.3 Exact mixed endpoint factorization

Set

\[
 U_0=\lambda_{N+r,\sigma}(g\beta),\quad
 U_1=\lambda_{N+r,\sigma}(gm'),\quad
 L_0=\lambda_{N,\sigma}(g\alpha),\quad
 L_1=\lambda_{N,\sigma}(gm).
\]

These are the actual endpoint coefficients, including all their literal
predicates and their zero extensions.  Direct expansion gives

\[
\begin{aligned}
 F_{00}-F_{10}-F_{01}+F_{11}
   &=U_0\overline{L_0}-U_0\overline{L_1}
     -U_1\overline{L_0}+U_1\overline{L_1}\\
   &=(U_0-U_1)\,\overline{(L_0-L_1)}.
\end{aligned}
\]

This identity remains exact when one or more endpoint coefficients is
zero.  No commutator is needed here.  More generally the full character
sum factors as

\[
 w\,(U_0+s_1U_1)\,\overline{(L_0+s_0L_1)}.
\]

The Fejer factor and the square-root phase in the physical statement
depend only on \(N,N+r,r,\sigma\), all of which are invariant.  They are
therefore one common scalar multiplying the orbit identity; no
cornerwise phase conjugation is produced by either swap.

### 3.4 Where the commutators actually occur

Let \(I_i\in\{0,1\}\) be the complete lower literal support indicator at
the endpoint defining \(L_i\), and write \(L_i=I_i\widetilde L_i\), where
\(\widetilde L_i\) denotes the corresponding literal interior value.
Then the following is an exact identity:

\[
\boxed{
 L_0-L_1
 =I_0I_1(\widetilde L_0-\widetilde L_1)
  +I_0(1-I_1)\widetilde L_0
  -(1-I_0)I_1\widetilde L_1.}
\]

The last two terms are the positive and negative literal-support/
zero-extension boundary commutators.  In the physical base sector
\(I_0=1\), the first possible exit \(I_1=0\) leaves simply

\[
 L_0-L_1=L_0,
\]

with no displacement factor.

On a common literal smooth cell, split the interior coefficient into its
certified smooth factor and its actual remaining factor,

\[
 \widetilde L_i=C_iQ_i.
\]

Here \(Q_i\) retains the normalized BV field and all discrete literal
fields.  A second exact identity is

\[
 \boxed{
 \widetilde L_0-\widetilde L_1
 =Q_0(C_0-C_1)+C_1(Q_0-Q_1).}
\]

The first term is the smooth displacement.  The second is the BV/
selector/arithmetic commutator.  If the literal remainder is a product
\(Q=\prod_{k=1}^Jq_k\), it can be charged field by field through the
exact telescoping formula

\[
 Q_0-Q_1
 =\sum_{k=1}^J
   (q_{k,0}-q_{k,1})
   \prod_{\ell<k}q_{\ell,0}
   \prod_{\ell>k}q_{\ell,1}.
\]

Thus shell/support, strict-cone, squarefree, coprimality, residual
selector, profile, floor, star, half-weight, hard-sample, crossing,
endpoint mask, zero-extension, normalized BV, and every other discrete
field each has a named term.  Equivalently, choosing the first field
that changes makes their boundary sets disjoint.  No one of these terms
is bounded by the \(C^1\) estimate for \(C\).

The arithmetic hypotheses alone demonstrably do not force typical
literal support predicates to be swap-invariant.  For instance,

\[
 g=1,\quad L=36,\quad D_L=6,\quad
 (\alpha,m,\beta,m')=(3,9,31,1)
\]

satisfies every displayed gcd condition, the \((-,-)\) character
conditions, \(r=4\), and both \(P_2\) inequalities.  The two lower
divisors are \(3\) and \(9\).  Therefore, if the listed squarefree
literal predicate tests the divisor at this interface, it passes at the
original endpoint and fails at the swapped endpoint.  This example is
not asserted to pass the undisclosed full literal support; it proves the
narrow point that arithmetic and allocation alone cannot establish
support closure.

### 3.5 The exact power ledger and its boundary failure

The displacement is

\[
 \delta=|g\alpha-gm|\le D_L.
\]

If on the strict common-cell piece one has the quantitative derivative
certificate

\[
 \sup |C'|\ll_\varepsilon L^{-1}X^\varepsilon,
\]

if the remaining common factor is bounded at the required scale, and if
the BV/discrete commutator has been separately removed or estimated,
then the mean value theorem yields

\[
 |L_0-L_1|\ll_\varepsilon
 \frac{D_L}{L}X^\varepsilon.
\]

After the usual harmless rescaling of \(\varepsilon\), applying this
gain to the available positive envelope gives

\[
 \frac{D_L}{L}\,D_LL^2X^\varepsilon
 =D_L^2L X^\varepsilon
 \le4L^2X^\varepsilon,
\]

because \(D_L=\lceil\sqrt L\rceil\le2\sqrt L\) for \(L\ge1\).

On a lower support exit, however, the exact orbit contribution is

\[
 w\,(U_0-U_1)\overline{L_0}
\]

when \(I_0=1,I_1=0\).  On an interior discrete or BV change it instead
contains

\[
 w\,(U_0-U_1)\overline{C_1(Q_0-Q_1)}.
\]

Neither term has the factor \(D_L/L\).  The stated positive envelope
then gives only \(D_LL^2X^\varepsilon\).  Closing the target requires a
new theorem that either proves these sets empty or bounds the aggregate
of every such commutator by \(O(L^2X^\varepsilon)\).  No such theorem is
among the isolated hypotheses.  Pointwise \(C^1\) by itself is also
insufficient to produce the scale \(L^{-1}\); the displayed derivative
bound must be part of the certificate and was not quantified in the
isolated statement.

## 4. First doubtful or unproved step

The first target-relevant unproved step is the assertion that the lower
swap \(g\alpha\leftrightarrow gm\) stays in the complete literal support
and in the same literal smooth cell with every nonsmooth field either
unchanged or separately summable.  In the notation above, the very first
uncontrolled term is

\[
 \mathcal B_{L,+}
 =I_0(1-I_1)\widetilde L_0.
\]

It is an actual endpoint coefficient, not an arbitrary bounded-array
surrogate, and it receives no small displacement factor.  Even after
one proves \(I_1=1\), the next unproved step is control of
\(C_1(Q_0-Q_1)\), followed by a quantitative
\(\|C'\|_\infty\ll L^{-1}X^\varepsilon\) certificate.  Hence the
four-corner algebra does not by itself establish the requested outer
scale.

## 5. Required control test and outcome

1. **Single-swap shadow — conditional pass and identification of the
   minimal useful action.**  In the sector \(s_0=-1\), at either fixed
   upper endpoint,

   \[
   w_{0j}F_{0j}+w_{1j}F_{1j}
   =w_{0j}U_j\overline{(L_0-L_1)}.
   \]

   Thus a lower \(\tau _0\)-pair alone supplies the desired lower
   difference.  It passes only with consistent zero extension and with
   the lower support/BV/discrete commutators charged.  Full upper
   four-corner closure is not needed for this particular gain; lower
   closure is the essential seam.

2. **Simultaneous-swap-only shadow — fail.**  In the \((-,-)\) sector
   the weights at \((00)\) and \((11)\) are both \(w\), so the diagonal
   pair is \(w(F_{00}+F_{11})\), not a difference.  The other diagonal
   similarly has equal signs.  The simultaneous involution alone cannot
   create the rectangle.

3. **Unsigned shadow — fail.**  Erasing \(\chi _4\) gives

   \[
   F_{00}+F_{10}+F_{01}+F_{11}
   =(U_0+U_1)\overline{(L_0+L_1)},
   \]

   so there is no lower displacement gain.

4. **Character-erased shadow — fail.**  This is algebraically the same
   plus-plus expression as the unsigned shadow.  Therefore the argument
   genuinely uses the \(\chi _4\) sector and does not prove an unsigned
   or adversarial bounded-array analogue.  Even with the correct
   characters, an arbitrary oscillatory array need not have a small
   endpoint difference; the actual coefficient regularity and boundary
   estimates remain indispensable.

5. **Phase-conjugated shadow — physical common phase passes; a
   cornerwise-conjugated shadow fails.**  A global replacement of the
   common physical phase by its conjugate merely changes the common
   scalar.  If instead the off-diagonal corners are assigned
   \(\overline p\) while the diagonal corners are assigned \(p\), the
   signed coefficient matrix has determinant

   \[
   p^2-\overline p^{,2},
   \]

   which is nonzero generically, so it is not a rank-one mixed
   difference.  The physical swaps do not cause this defect because
   \(N,N+r,r,\sigma\) and hence the phase are common at all four
   corners.

6. **Missing-corner shadow — fail unless the missing value is the actual
   endpoint zero extension.**  Deleting a nonzero \(F_{11}\) changes the
   alternating rectangle by \(-F_{11}\) and destroys the factorization.
   If \(F_{11}=0\) because an endpoint coefficient is literally zero,
   the four-term algebraic identity still passes.  Nevertheless the
   physical nonzero source is not a genuine four-corner orbit, and a
   missing lower row produces the undifferenced boundary coefficient
   displayed above.

7. **Zero-extension shadow — algebraic pass, analytic boundary fail.**
   Consistent endpoint zero extension preserves the exact rectangle
   identity because it is an identity of the four actual complex
   endpoint values.  It does not make a \(1\)-to-\(0\) support jump
   \(O(D_L/L)\).  Zero extension therefore repairs bookkeeping, not the
   power ledger.

No spectral-core relocation was made in this derivation.  It stays with
the physical correlation, fixed orientation, and fixed frequency sign,
so it invokes none of the additional restoration claims listed for a
spectral-core proof.

## 6. Dependencies and exact artifacts used

Only the following two files were read or used:

1. `protocol.md`.
2. `rounds/codex-managed/m9-m1-t1-p2-four-corner-allocation-commutator-gate/blind_statement.md`.

No proof graph, campaign manifest, strategy, previous round, source
card, sibling report, plan, brief, review, control, candidate, kernel,
synthesis, or other artifact was inspected.

## 7. Recommended state effect

**Revise.**  Retain the recomputed-gcd classification, parity and
\(P_2\) invariance, complete character table (including the common sign
\(w\)), exact mixed endpoint factorization, and the conditional
\(D_L/L\) ledger.  Reject promotion of a whole-sector
\(O(L^2X^\varepsilon)\) estimate from this mechanism until there is a
separate lower-swap support/cell closure theorem or an
\(O(L^2X^\varepsilon)\) aggregate estimate for each named
support/BV/discrete commutator.  Make no state change beyond this
route-specific obstruction and no promotion to any larger allocation,
endpoint, bridge, or exponent claim.

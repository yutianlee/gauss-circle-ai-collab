# Independent cross-gcd allocation/incidence seam review

- Campaign: m9-m1-t1-p2-cross-gcd-cellular-boundary-gate
- Round: 199
- Role: independent algebra and incidence seam reviewer
- Numerical theorem evidence: none

## 1. Result

The factorization, the three whole-allocation maps, their invariant
canonical domains, preservation of \(P_2\), the actual \(\chi _4\)
quotients, the triangle/rectangle expansion, and the forced role of
\(V_A\) are algebraically correct. The large-shell argument does put
\(V_A\) in the authoritative first-failure mask
\(P_1=\mathbf 1_{|d-gm|>D_L}\).

One sentence is overstrong: immediately after (199.K8), the candidate
calls the maps involutions on their displayed **live** domains. The
conditions \(B=1\) and \(C=1\) are sufficient for preservation of the
recomputed gcd, but not by themselves for preservation of the physical
odd-denominator domain. They define involutions on the canonical total
zero-extended allocation domain. A live-to-live statement needs the
additional parity/support restrictions recorded in Section 4 below.
This is a statement repair; it does not affect the odd \(B\)-\(E\)-\(C\)
triangle or the mechanism-scoped self-return.

## 2. Exact factorization and hypotheses

On a live term, both \(N=dm\) and \(N+r=d'm'\) are squarefree. A prime
of \((N,N+r)\) occurs in exactly one of the four pairs

\[
 (d,d'),\quad(m,d'),\quad(d,m'),\quad(m,m').
\]

Consequently

\[
 A=G_{00},\quad B=G_{10},\quad C=G_{01},\quad E=G_{11}
\]

are pairwise coprime, and removal of these common-prime states gives the
unique factorization

\[
 d=ACx,\qquad m=BEu,\qquad d'=ABy,\qquad m'=CEv,
\]

with \(A,B,C,E,x,u,y,v\) pairwise coprime. In particular \(A=g\),
\(B=(m,\beta)\), and

\[
 d-gm=A(Cx-BEu),\qquad d'-gm'=A(By-CEv).
\]

Thus (199.K6)--(199.K7) are exact. No prime-density or nonvanishing
claim is used.

## 3. Whole-allocation maps, inverse domains, and \(P_2\)

Writing canonical factor data in the order
\((A,B,C,E,x,u,y,v)\), the three maps in (199.K8) act as follows:

\[
\begin{array}{c|c|c}
\text{map and domain}&\text{canonical image data}&\text{defects}\\ \hline
\tau_L,\ B=1&(A,1,E,C,u,x,y,v)&(\Delta_L,\Delta_U)\mapsto(-\Delta_L,\Delta_U)\\
\tau_U,\ C=1&(A,E,1,B,x,u,v,y)&(\Delta_L,\Delta_U)\mapsto(\Delta_L,-\Delta_U)\\
\tau_S,\ E=1&(A,C,B,1,u,x,v,y)&(\Delta_L,\Delta_U)\mapsto(-\Delta_L,-\Delta_U).
\end{array}
\]

Here \(\Delta_L=d-Am\) and \(\Delta_U=d'-Am'\). The image again has
respectively \(B'=1,C'=1,E'=1\); applying the same map to the image
returns the source. These are the exact inverse domains. Products
\(N,N+r\) and the recomputed gcd \(A\) are preserved. Since \(P_2\)
uses only \(|\Delta_L|\le D_L\) and \(|\Delta_U|>D_L\), all three maps
preserve \(P_2\).

For the block \(q>1\), the vertices

\[
 V_B=(Ax,qu,Aqy,v),\quad V_E=(Ax,qu,Av,qy),\quad
 V_C=(Aqu,x,Av,qy)
\]

are therefore the lawful whole-allocation orbit
\(V_B\overset{\tau_U}{\longrightarrow}V_E
\overset{\tau_L}{\longrightarrow}V_C
\overset{\tau_S}{\longrightarrow}V_B\), with the common defects
\(A|x-qu|\) and \(A|qy-v|\). These swaps exchange whole complementary
allocations (and hence also exchange residual factors); they are not the
blind report's moves of only one prime block while the residual factors
are frozen.

## 4. First overstrong statement and exact repair

Because \(d,d'\) are odd and \(r\) is even, \(m\) and \(m'\) have the
same parity. Under \(\tau_L\), the new lower divisor is \(Am\), so the
map is physical live-to-live only when \(m\) is odd. Under \(\tau_U\),
the new upper divisor is \(Am'\), so it is live-to-live only when \(m'\)
is odd. The simultaneous map requires both; on its canonical domain
\(E=1\), equal parity already forces both to be odd. If “live” includes
all literal support predicates rather than only denominator parity, each
domain must further be intersected with the transported live preimage;
otherwise the correct setting is the total zero extension.

This is a real distinction. For an even squarefree source one may have
\(B=C=1\) and \(E=2\); then the lower and upper maps retain gcd \(A\) but
send an odd physical denominator to an even, zero-extended one. Hence
\(B=1\) or \(C=1\) alone is not an exact live-bijection hypothesis.

The repair is to replace the sentence after (199.K8) by:

> Each map is an involution on its displayed canonical total
> zero-extended allocation domain. It is a bijection on the physical
> live-to-live subdomain after imposing \(m\) odd for \(\tau_L\), \(m'\)
> odd for \(\tau_U\), and both odd for \(\tau_S\), together with the
> transported literal support conditions.

Then add that the triangle (199.K9) lies in this parity-safe subdomain:
its cross-gcd state is the odd block \(q\), and equal parity together
with \(E=1\) (at \(V_B,V_C\)) or \(E=q\) (at \(V_E\)) forces \(m,m'\)
odd. Thus this repair does not alter the triangle calculation.

The partial-block vertices (199.K21) are a separate construction. Their
three masks are exactly the three displayed, generally unequal Boolean
expressions, so their transported-mask differences in (199.K22) are
real. They must not be used as the inverse cells of the whole swaps.

## 5. Actual character incidence and endpoint algebra

All denominators on the lawful triangle are odd. If \(c_\bullet\) is
the actual factor \(\chi_4(d)\chi_4(d')\), then, relative to \(V_B\),

\[
 c_E=t\,c_B,\qquad c_C=tp\,c_B,\qquad c_A=p\,c_B,
\]

where

\[
 p=\chi_4(qxu),\qquad t=\chi_4(qyv).
\]

Therefore the actual edge quotients along
\(V_B\to V_E\to V_C\to V_B\) are \(t,p,tp\), with product \(1\).
In particular the simultaneous quotient is \(+1\) when \(p=t=-1\).
This verifies (199.K12) and excludes an assigned alternating sign.

With the endpoint notation (199.K13), the three lawful vertices give

\[
 \Sigma_{BEC}=u_0\overline{\ell_0}
 +t u_1\overline{\ell_0}+tp u_1\overline{\ell_1}.
\]

The only missing product of
\(\{u_0,u_1\}\times\{\ell_0,\ell_1\}\) is
\(u_0\overline{\ell_1}\). Fixing that lower divisor and upper divisor,
while preserving \(N,N+r\), forces uniquely

\[
 V_A=(Aqu,x,Aqy,v).
\]

Its recomputed gcd is \(Aq\), and its relative character is \(p\).
Direct expansion gives exactly

\[
 \Sigma_{BEC}+p\,u_0\overline{\ell_1}
 =(u_0+t u_1)\overline{\ell_0+p\ell_1}.
\]

For \(p=-1\), omission of \(V_A\) consequently leaves
\(+u_0\overline{\ell_1}\) with structural coefficient one. This is a
coefficient identity only and asserts neither nonvanishing nor lower
mass. The constant-endpoint augmentation \(1+t+tp\) is also never zero.

## 6. \(V_A\) owner and controls

Let \(qu\ge cL\) be the fixed live-shell lower bound. From
\(A|x-qu|\le D_L\) and \(q\ge3\),

\[
\begin{aligned}
 |x-u|
 &\ge (q-1)u-|x-qu|\\
 &=\left(1-\frac1q\right)qu-|x-qu|\\
 &\ge \frac23cL-\frac{D_L}{A}.
\end{aligned}
\]

For all sufficiently large live shells this is at least \(cL/3\).
At \(V_A\), the current gcd is \(Aq\), so

\[
 |d-(d,d')m|=Aq|u-x|>D_L.
\]

Thus \(V_A\in P_1\) for large live shells; bounded shells retain the
accepted absolute treatment. This proves only the authoritative
lower-first-failure predicate. It does **not** prove that the upper
coordinate at \(V_A\) is far: \(A|qy-v|>D_L\) does not imply
\(Aq|y-v|>D_L\). Accordingly the blind packet's phrase “two-far mask
\(P_1\)” must not be imported literally. The candidate's wording
“lower-far owner” is the correct one and should be accompanied by the
explicit definition of \(P_1\).

Control outcomes: cross-gcd factorization PASS; whole-map algebra and
canonical inverses PASS; physical live-domain wording REPAIR;
\(P_2\)-preservation PASS; actual \(\chi_4\) incidence PASS;
triangle/rectangle algebra PASS; uniqueness of \(V_A\) PASS; large-shell
\(P_1\) ownership PASS with the lower-far terminology above; distinction
from partial-block moves PASS.

## 7. Dependencies and state recommendation

Dependencies used: protocol.md, the authoritative definition of
\(P_1,P_2\) in state/proof_obligations.yml,
state/active_campaign.yml, the Round-199 statement-only packet, the
conductor reconciliation, and the formal candidate. No external source,
numerical evidence, kernel edit, or graph mutation is used.

Recommended state effect: revise the candidate wording only; retain the
mechanism-scoped self-return and make no theorem or exponent promotion.
Exact required repairs are (i) replace the live-domain claim after
(199.K8) by the total-zero-extended/invariant-domain statement plus the
parity and transported-support restrictions, (ii) state explicitly that
the lawful \(q\)-triangle satisfies those restrictions, and (iii) define
\(P_1\) as the lower-first-failure mask and disclaim any upper-far claim.

**REPAIR**

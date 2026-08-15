# Local reflection eigenspaces and the maximal angular kernel

## 1. Result

There is an exact coefficient-level reflection law, but the ramified prime
\(2\) is a translation of the angular coordinate rather than a reflection
eigenvalue. If \(n=2^k m\), \(m\) odd, and
\(\epsilon_m=\chi _4(m)\), then

\[
 a_{-z}(n)=\epsilon_m2^{kz}a_z(n).
\]

Consequently the odd part is a genuine \(\epsilon_m\)-eigenvector, while at
height \(z=it\) the \(2\)-part rotates, without shrinking, the two global
reflection eigenspaces. In the exact physical maximal kernel the arithmetic
coefficient selects precisely the matching reflection component of the
profile; the opposite component is identically invisible. This projection
has norm one, so it gives no cancellation by itself.

There are two genuine but limited gains. First, the reflection-odd mode has
zero joint \((u,v)=(0,0)\) residue. It does **not** cancel either the top
\(1/u\) pole or the height \(1/v\) pole away from their intersection. Second,
the entire non-vacuous tail
\(2^{v_2(n)}\ge 2X^{1/8}\) of the maximal kernel is
\(O_\varepsilon(X^\varepsilon)\) absolutely. The smallest surviving kernel
therefore has \(0\le v_2(n)<\lceil\log _2(2X^{1/8})\rceil\), with the two odd
reflection sectors still coupled outside the absolute value.

## 2. Exact statement and hypotheses

Use the accepted coefficient

\[
 a_z(n)=\sum_{hq=n}\chi _4(q)(q/h)^{z/2}
\]

and the post-residue Round-16 maximal sum, with \(N_X=\lfloor16\sqrt X\rfloor\),

\[
 \mathfrak M_T(X)=\sum_{hq\le N_X}\chi _4(q)(hq)^{-3/4}
 e(\sqrt{Xhq})\,\mathcal H_{T,X}(h,q).
\]

Here \(\mathcal H\) is exactly the actual scale sum, with height floors,
\(\Phi\), endpoint stars, smooth remainders, and the symmetrically truncated
Perron sign kernel. No profile is replaced or completed.

Write \(h=2^kr\), with \(r,q\) odd, \(m=rq\), and define

\[
 \mathcal H^{[\epsilon]}_{T,k}(r,q)=\frac12\{\mathcal H_{T,X}(2^kr,q)
 +\epsilon\mathcal H_{T,X}(2^kq,r)\}.
\]

Then the exact eigenspace insertion is

\[
 \mathfrak M_T(X)=\sum_{k\ge0}2^{-3k/4}
 \sum_{\substack{m\le N_X/2^k\\m\ {\rm odd}}}m^{-3/4}e(\sqrt{2^kXm})
 \sum_{rq=m}\chi _4(q)\mathcal H^{[\chi _4(m)]}_{T,k}(r,q). \tag{E}
\]

## 3. Proof or derivation

Multiplicativity gives, for an odd prime \(p\),

\[
 a_z(p^j)=p^{-jz/2}\sum_{\nu=0}^j(\chi _4(p)p^z)^\nu,
 \qquad a_z(2^k)=2^{-kz/2}.
\]

Reversing \(\nu\mapsto j-\nu\) proves
\(a_{-z}(p^j)=\chi _4(p)^j a_z(p^j)\). Hence, for \(n=2^km\),

\[
 a_z(n)=2^{-kz/2}a_z(m),\qquad
 a_{-z}(n)=2^{kz/2}\epsilon_m a_z(m).
\]

Thus \(a_z^\pm=(a_z\pm a_{-z})/2\) satisfy

\[
 a_z^\pm(2^km)=\frac{a_z(m)}2
 (2^{-kz/2}\pm\epsilon_m2^{kz/2}). \tag{1}
\]

For \(z=it\), (1) is a cosine/sine rotation and

\[
 |a_{it}^+(2^km)|^2+|a_{it}^-(2^km)|^2=|a_{it}(m)|^2.
\]

At \(k=0\), odd \(m\equiv1\pmod4\) is purely even and odd
\(m\equiv3\pmod4\) purely odd. Also

\[
 a_0(n)=\prod_{p\equiv1(4)}(v_p(n)+1)
 \prod_{p\equiv3(4)}\mathbf1_{2\mid v_p(n)}=r_2(n)/4.
\]

So the odd reflection mode has zero joint mode, while the even mode retains
the full Hardy return.

For (E), let \(S=\sum_{rq=m}\chi _4(q)\mathcal H(2^kr,q)\). After swapping
\(r,q\),
\(\sum\chi _4(q)\mathcal H(2^kq,r)=\epsilon_m S\); hence inserting
\(\mathcal H^{[\epsilon_m]}\) returns \(S\), and the opposite projection gives
zero.

The prime \(2\) worsens the missing-profile seam. The two Perron arguments
are

\[
 A_D(2^kr,q)=\frac D{2\sqrt X}2^{-k/2}\sqrt{q/r},\quad
 A_D(2^kq,r)=\frac D{2\sqrt X}2^{-k/2}\sqrt{r/q}.
\]

Making the second the inverse of the first requires
\(D'=2^k4X/D\ge2^k4\sqrt X\), outside every actual scale. Thus the matching
projection reconstructs the original capacity; it supplies no partner.

Nor do antisymmetric modes cancel the poles. With
\(F_z^-(s)=(F_z(s)-F_{-z}(s))/2\), nonzero \(z\) gives distinct poles at
\(1-z/2\) and \(1+z/2\), with residues
\(\tfrac12L(1-z,\chi _4)\) and \(-\tfrac12L(1+z,\chi _4)\). Near the double
Mellin origin, \(a^-_{u+v}=O(u+v)\), while
\(\widehat W_+(u)\widehat\phi(v)=(uv)^{-1}+O(u^{-1}+v^{-1})\). The product is
\(O((u+v)/(uv))\): the joint residue vanishes, but both axial poles remain.
Already \(a_z(3)=3^{-z/2}-3^{z/2}\) shows the \(1/u\) pole survives when
\(v\ne0\).

Finally, each truncated Perron sign factor is uniformly bounded (a sine
integral), smooth remainders have bounded Mellin \(L^1\)-norm, and there are
\(O(\log X)\) scales. Hence
\(\sup_T|\mathcal H_{T,X}(h,q)|\ll\log X\). For any \(K\),

\[
 \sup_T|\mathfrak M_T^{k\ge K}|
 \ll (\log X)\sum_{k\ge K}2^{-3k/4}
 \sum_{rq\le N_X/2^k}(rq)^{-3/4}
 \ll N_X^{1/4}2^{-K}(\log X)^2.
\]

Taking \(K=\lceil\log _2(2X^{1/8})\rceil\) proves the claimed target-sized
tail. This range is arithmetically nonempty well below \(k\asymp
(1/4)\log_2X\).

## 4. First doubtful or unproved step

No cancellation estimate is proved for the low-\(2\)-adic sum in (E). The
first missing step is a maximal, outside-absolute correlation for its matching
profile projections. Splitting the \(\epsilon=\pm1\) sums and bounding them
separately would be a stronger, unjustified target.

## 5. Required control test and outcome

Exact symbolic controls pass: \(n=5\) is reflection-even;
\(n=3\) is reflection-odd and nonzero off \(z=0\); and
\(a_{-z}(6)=-2^za_z(6)\), exposing the ramified rotation. The scale equation
returns \(D'=4X/D\) at \(k=0\) and \(D'=8X/D\) at \(k=1\). No numerical test
was used.

## 6. Dependencies and exact artifacts used

Only protocol.md, state/proof_obligations.yml,
rounds/codex-managed/m9-m1-angular-mellin-separation/synthesis.md,
rounds/codex-managed/m9-m1-reflected-mode-correlation/synthesis.md, and
state/failure_ledger.md were used. No external theorem or web source was
invoked.

## 7. Recommended state effect

Promote the prime-power reflection law, (E), the vanishing joint odd residue,
and the high-\(2\)-adic absolute tail bound. Retain the low-\(2\)-adic maximal
kernel below as open:

\[
 \boxed{\sup_T\left|\sum_{0\le k<K_X}2^{-3k/4}
 \sum_{\substack{m\le N_X/2^k\\m\ {\rm odd}}}m^{-3/4}e(\sqrt{2^kXm})
 \sum_{rq=m}\chi _4(q)\mathcal H^{[\chi _4(m)]}_{T,k}(r,q)\right|
 \ll_\varepsilon X^\varepsilon.}
\]

Reject claims that reflection eigenspaces cancel the separate Mellin poles or
reduce capacity merely by orthogonality. GAR, blockwise M9-M1, M9, and the
Gauss target remain open.

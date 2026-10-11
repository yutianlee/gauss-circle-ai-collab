# Isolated Round208 statement packet

Read only protocol.md and this packet. No graph, campaign, strategy,
predecessor reports, siblings or web. Write only reports/blind_moment_hierarchy.md
under this campaign. Seven numbered protocol sections are mandatory.

Let theta be a fixed number in(1/4,1/3), beta=2theta-1/2, q=136/13.
Let T>=2, X=T^2, I=[T/sqrt(2),sqrt(3)T], J=[X/2,3X].
Assume the inclusive discrepancy P(x) has monotone counting function
P(x)+pi*x, satisfies O(x^theta+epsilon), and
P(R^2)=R^(1/2)H_T(R)/pi+O(T^(1/2+epsilon)) on I.
The complete series has a smooth dyadic decomposition, singleton and
rapid tails. Its blocks H_N, N=T^alpha, satisfy
measure{|H_N|>V} << T^epsilon(V^-2+T V^-q), V>=1,
and |H_N|<<T^epsilon min(N^(1/4),T^beta,(T/N)^(1/2))
in the range1<=N<=T. For N>=T assume rapid weighted bounds adequate to
make every fixed p moment O(T^(1+epsilon)); singleton is bounded.
There are O(log T) active blocks. Thus no power loss in fixed-p summation.

For the middle blocks assume a proved bridge H_N(R)=R^-1/2 Z_N(R^2)
plus errors whose complete p-moment is O(T^(1+epsilon)) for each fixed p.
Set h=2sqrt(x)/sqrt(N), H=T/sqrt(N), and K_(2k)(N)=integral_J|Z_N(x)|^(2k)dx.

Independently derive (do not assume proposed formulas):
(a) the moment and pointwise consequence of a radius moment T^(1+delta_p);
(b) the largest exponent a for which every block with the displayed
supremum<=T^a is safe for that radius target, when p>q and delta_p>=0;
(c) the corresponding low and high safe bands, including empty/overlap
cases and beta;
(d) for integer k with2k<=p, the sufficient complete K_(2k) threshold,
and the current certificate using variance integral_I|H_N|^2<<T N^-1/2
and the displayed supremum;
(e) which dependence of delta_p on arbitrarily large fixed p proves
the full quarter bound, and why one fixed-p success or merely proving
Gaussian K6 cannot by itself establish arbitrarily high moments;
(f) compare a hypothetical K_(2k)<<X H^k hierarchy for all fixed k with
one fixed k, retaining all complements and real endpoints.
Controls: recover p=12,delta=4/25 and k=3 explicitly; check a constant
or single narrow peak for unjustified extrapolation. No numeric theorem
certification. State first unproved arithmetic input precisely.

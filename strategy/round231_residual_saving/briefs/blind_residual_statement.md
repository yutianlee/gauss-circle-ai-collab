# Isolated arithmetic residual control

Statement-only task; 2026-10-11. Read ONLY protocol.md and this file, plus the task message. No graph, sibling, research history or web. Provenance graph identifier a50642edf65a3000056cd1443996a32193eb7bf3477b789314be49b843e25f0b.

Let chi4 be the real primitive character modulo4, r2(n)=4 sum_(d|n)chi4(d), x>1 real, z=x^(1/20), and for n in (x,x+H] define

    rsharp_x(n)=4 sum_(z<=d<z²,d|n)chi4(d)(log n-2log z)/log z
                +4 sum_(d<z,d|n)[chi4(d)+chi4(n/d)],
    v_x(n)=r2(n)-rsharp_x(n).

Investigate how large a uniform power saving in

    |sum_(x<n<=x+H)v_x(n)e(P(n))| <= C H x^(-kappa)

can possibly be, for all real x sufficiently large, all fixed-degree real polynomial P (including constant and linear), and H in [x^(1/3+epsilon0),x^(1-epsilon0)] for fixed epsilon0=1/25. Give a rigorous quantitative restriction if one exists, or explain the first gap. Controls should use ACTUAL coefficients and real endpoints. You may choose a legal H, starts x along a sequence and polynomial phases to falsify an overly strong uniform saving. If removing only a scalar mean would repair your obstruction, test that claim separately using linear phases, with exact arithmetic proof if feasible.

Elementary facts allowed: A(y)=sum_(n<=y)r2(n)=pi y+O(sqrt(y)+1); chi4 has bounded partial sums; divisor identity; finite geometric sums. You may derive exact norm counts in residue classes from the lattice if useful. Do not assume a uniform bound or source theorem. This is an isolated question about the displayed residual; no claim about physical circle moments is requested. Seven protocol sections, exact proof, first gap, controls and narrow state recommendation. Write ONLY reports/blind_residual_control.md in this packet and return SHA256; stop. Budget15min, >=95% analysis.

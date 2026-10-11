# Round216 isolated same-round collective-class seam

This is a bounded statement-only rederivation assigned after the original
blind_radical_cutoff report is finalized. Until this derivation is frozen,
read only protocol.md, this packet and your own original isolated packet
and report. No claimant, conductor ledger, graph, strategy or siblings.
Write only reviews/isolated_distinct_class_rederivation.md; seven numbered
protocol sections, exact inputs, controls and state scope; stop afterward.
Metadata graph hash:4f6f990b276b15b24c791870864c945a4a9921b0acdd7dcc734a2b5d3f007c71.

For realT>=2 set Q=floor(T^(2/5)). Let w>=0 be a fixed smooth radius
window of compact support comparable toT after writingw(R/T). Let
f_d(R) be real functions indexed by integersd>Q (a subset is permitted),
with |f_d(R)|<=A_d, sum_d A_d finite for eachT. For fixedh=2,...,12
assume, for everyepsilon>0 with the corresponding fixed constants,

    sum_(d>Q) A_d^h <<_epsilon Q^(1-3h/4+epsilon).

Put Z(R)=sum_d f_d(R). Suppose a fixedbeta satisfies1/8<beta<13/100
and, for each integer0<=r<=10,

    integral w(R/T)|Z(R)|^r dR
          <<_epsilon T^epsilon [T+T^(max(r-2,0)beta)].

All these hypotheses are granted abstractly; infer no arithmetic origin.
Define the ordered distinct-class sum

    E12(R)=sum_(d1,...,d12 pairwise distinct) product_(j=1)^12 f_dj(R).

Independently derive a finite algebraic identity comparingZ^12 withE12
which retains collective signed cancellations among repeated labels.
Use it to bound integral w(R/T)|Z(R)^12-E12(R)|dR, with an explicit
complete exponent inT, all feasible class partitions, all infinite-sum
passages and endpoint/logarithmic losses. Compare with target29/25.

Determine precisely when an upper or absolute bound on the real signed
integral ofE12 transfers to the twelfth moment ofZ and conversely.
Do not treatE12 as pointwise nonnegative or as a torus expectation.
Test the formula when the index family has fewer than twelve members,
and when all f_d coincide or vanish. A termwise absolute expansion of
the original repeated-label part is a different estimate; explain the
distinction. No source, numerical experiment, source expansion or
successor work is authorized by this packet.

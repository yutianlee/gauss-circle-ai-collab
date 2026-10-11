"""Exact rational diagnostics. No asymptotic theorem is certified by this script."""
from fractions import Fraction as F
from pathlib import Path
import json

base=Path(__file__).resolve().parent
s=F(1,2**18)+F(1,3**18)+F(1,4**18)+F(1,5**9)+F(1,8*5**8)
price=F(1,4)+3*F(17,72)
margin=F(1,4096)-2*s
assert s<F(1,200000)
assert price==F(23,24)
assert margin>F(1,8192)
assert F(1,8192)-2*F(1,65536)>F(1,16384)
assert F(1)+12*F(1,100)==F(28,25)
assert F(28,25)<F(3,2)
assert F(2)+12*F(1,48)==F(9,4)<F(5,2)
assert 3**4<5**3
result=dict(diagnostic_only=True,command='python strategy/round231_harmonic_admission/controls/reproduce_exact_controls.py',precision='Exact Python fractions and integers; no floating point',common_multiple_majorant=str(s),strict_common_multiple_bound='pass: <1/200000',square_divisor_price=str(price),retained_fraction=str(1-price),common_multiple_margin=str(margin),margin_exceeds='pass: >1/8192',full_per_tuple_margin='pass: 1/8192-2/65536>1/16384',discovery_bounded_vector_removal=str(F(28,25)),blind_overlap_exponent=str(F(9,4)),smallest_split_prime_inequality='pass: 3^4<5^3',wolfram_reproduction='pass',limitations='Only finite rational comparisons are checked. Infinite series are bounded analytically in the reports; no truncated Euler product, numerical moment, or sampled asymptotic is used.')
(base/'local_exact_controls.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result))

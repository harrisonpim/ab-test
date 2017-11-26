# ab-test :chart_with_upwards_trend:
basic tool to assess the statistical significance of multivariate tests

### Usage
```python
from src import *

control_version = [8000, 4380]
test_version_1 = [1000, 520]
test_version_2 = [1000, 590]

ab_test(control_version, test_version_1, test_version_2, p=0.01)
```

will output

```
CONTROL:
conversion rate:    0.5475 ± 0.0056
threshhold p-value: 0.01

--------------------------------------------------------------------------------
TEST 1
--------------------------------------------------------------------------------
We can't say anything significant about how well the test performed
conversion rate:  0.52 ± 0.0158
uplift:           -0.0502
Z-score:          -1.6418
p-value:          0.0503

--------------------------------------------------------------------------------
TEST 2
--------------------------------------------------------------------------------
The test performed better than the control by a significant margin!
conversion rate:  0.59 ± 0.0156
uplift:           0.0776
Z-score:          2.5728
p-value:          0.005
```

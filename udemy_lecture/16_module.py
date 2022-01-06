import test_module1
# 다시 import는 안됨
import test_module1
import test_module2

test_module2.test2_f1()
test_module2.test2_f2()

# 모듈내의 요소가 특정 모듈에만 존재하면 생략가능
#from test_module3 import test3_f1
#from test_module3 import test3_f2
from test_module3 import test3_f1, test3_f2

# 비추천, 혹시라도 중복되면....
#from test_module3 import *

test3_f1()
test3_f2()

# 별칭 가능
import test_module4 as t4
t4.test4_f1()
t4.test4_f2()
# 16_package.py

import package1.test_module5

package1.test_module5.test5_f1()
package1.test_module5.test5_f2()

# 패키지명 생략
from package2 import test_module6

test_module6.test6_f1()
test_module6.test6_f2()

from package3.test_module7 import test7_f1, test7_f2
test7_f1()
test7_f2()

# 패키지 내의 모든 모듈 사용
# 지정된 패키지내의 __init__.py 파일에 명시된 모듈들만 import
from package4 import *

test_module8.test8_f1()
test_module8.test8_f2()
test_module9.test9_f1()
test_module9.test9_f2()

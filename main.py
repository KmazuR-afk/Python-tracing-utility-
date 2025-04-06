from test_funs import fun_1,fun_2,fun_3
from profiler import Profiler, show_results

profiler = Profiler()
profiler.enable(["test_funs.fun_1","test_funs.fun_2"])

for i in range(5):
    fun_1()
    fun_2()
    fun_3(i)
print('\n','-'*6,'Before adding fun_3','-'*6)
show_results(profiler.get_results())

profiler.add_func("test_funs.fun_3")

for i in range(5):
    fun_1()
    fun_2()
    fun_3(i)
print('\n','-'*6,'After adding fun_3','-'*6)
profiler.disable()

show_results(profiler.get_results())

for i in range(5):
    fun_1()
    fun_2()
    fun_3(i)
print('-'*6,'After profiler.disable() fun_3','-'*6)
show_results(profiler.get_results())

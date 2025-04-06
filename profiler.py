import sys,time

class Profiler:
    def __init__(self):
        self.enabled = False
        self.funcs = set()
        self.res = {}

    def trace_call(self,frame,event,arg):
        if event != 'call':
            return
        f_name = frame.f_code.co_name
        mod_name = frame.f_globals['__name__']
        full_name = f"{mod_name}.{f_name}"
        if f"{mod_name}.{f_name}" not in self.funcs:
            return
        start = time.perf_counter()

        def trace_returns(f,e,a,t_func=full_name):
            if e == 'return':
                duration = time.perf_counter() - start
                self.res.setdefault(t_func, []).append(duration)
            return trace_returns

        return trace_returns

    def enable(self,f_names):
        self.enabled = True
        self.funcs.update(f_names)
        sys.settrace(self.trace_call)

    def disable(self):
        sys.settrace(None)
        self.enabled = False

    def add_func(self,f_name):
        self.funcs.add(f_name)
        if self.enabled:
            sys.setprofile(self.trace_call)

    def get_results(self):
        return {
            fun: {
                'count': len(times),
                'average time': sum(times)/len(times) if times else 0,
                'total time': sum(times)
            }
            for fun, times in self.res.items()
        }

def show_results(results):
    print(f"{'Function':40} | {'Calls':^7} | {'Avg Time (s)':^15} | {'Total Time (s)':^15}")
    print("-" * 85)
    for func, data in results.items():
        print(f"{func:40} | {data['count']:^7} | {data['average time']:^15.6f} | {data['total time']:^15.6f}")
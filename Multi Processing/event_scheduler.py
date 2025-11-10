import sched, time

s = sched.scheduler(time.time, time.sleep)

def print_task(val ='default'):
    print("From print_task", time.time(), val)


def print_some_tasks():
    print(time.time())

    s.enter(delay=2, priority=0, action=print_task)
    s.enter(delay=1, priority=1, action=print_task, argument=("positional",))
    s.enter(delay=1, priority=2, action=print_task, kwargs={'val' : "keyword"})

    s.run()

    print(time.time())


print_some_tasks()

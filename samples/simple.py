import ray
ray.init()

@ray.remote(num_cpus=2)
def f(x):
    print("started executing task!")
    @ray.remote(num_cpus=2)
    def g(x):
        return x * x
    y = x * x#ray.get(g.remote(x))
    print("finished executing task!")
    return y

futures = [f.remote(i) for i in range(64)]
print(ray.get(futures))
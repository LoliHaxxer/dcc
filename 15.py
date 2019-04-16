import random
def rangen(num):
    for x in range(num):
        yield x
def rantom(sample_generator):
    sample_count = 0
    selected_sample = None
    for sample in sample_generator:
        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample
    return selected_sample
input(rantom(rangen(5_000_000)))
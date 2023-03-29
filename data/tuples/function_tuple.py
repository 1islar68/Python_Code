def likelihood():
    likelihoods = (50, 38, 27, 99, 4)
    return likelihoods

def run():
    value1 = min(likelihood())
    value2 = max(likelihood())
    print(f"Minimum likelihood of falling: {value1}%\nMaximum likelihood of falling: {value2}%")

run()
def observed():
    observations = []
    for i in range(5):
        add_observe = input("Pleasure enter an observation:")
        observations.append(add_observe)
    return observations

def remove_observations(observation_list = []):
    while True:
        opt = input(print("Do you wish to remove an observation (yes/no)?"))
        if opt.upper() == "YES":
            remove = input("What observation do you wish to remove?")
            observation_list.remove(remove)
        elif opt.upper() == "NO":
            break
    return observation_list

def run():
    observe = observed()
    remove_observations(observe)
    obser = set()
    for observation in observe:
        data = (observation, observe.count(observation))
        obser.add(data)
    sorted(obser)
    for data in obser:
        print(f"{data[0]} observed {data[1]} times")

run()
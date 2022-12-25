file = open("test_day19.txt", "r")
lines = file.readlines() 
blueprints = []
maxtime = 8
best_geodes = dict()
def simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time):
        if time not in best_geodes:
            best_geodes[time] = geode
        best_geodes[time] = max(best_geodes[time], geode)

        if maxtime == time: 
            return geode  

        ore += ore_robots
        clay += clay_robots
        obsidian += obsidian_robots
        geode += geode_robots
        print("Time", time, ore, clay, obsidian, geode) 
        
        time += 1 
        maxscore = 0
 
        if ore >= blueprint[4] and obsidian >= blueprint[5]:
            geode_robots += 1
            ore -= blueprint[4]
            obsidian -= blueprint[5]
            geode -= 1
            #print("Time", time, "Geode", geode_robots)
            score = simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
            maxscore = max(score, maxscore)
        else:
            if ore >= blueprint[2] and clay >= blueprint[3]:
                obsidian_robots += 1
                ore -= blueprint[2]
                clay -= blueprint[3]
                obsidian -= 1
                #print("Time", time, "Obsidian", obsidian_robots) 
                score = simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
                maxscore = max(score, maxscore)
                
            if blueprint[1] <= ore:
                clay_robots += 1
                ore -= blueprint[1]
                clay -= 1
                #print("Time", time, "Clay", clay_robots) 
                score = simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
                maxscore = max(score, maxscore)
                
            if blueprint[0] <= ore and blueprint[1] > blueprint[0]:
                ore_robots += 1
                ore -= blueprint[0]
                ore -= 1
                #print("Time", time, "Ore", ore_robots) 
                score = simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
                maxscore = max(score, maxscore)

        score = simulate_blueprint(blueprint, ore, clay, obsidian, geode, ore_robots, clay_robots, obsidian_robots, geode_robots, time)
        maxscore = max(score, maxscore)
        return maxscore
 
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    lines[i] = lines[i].replace("Blueprint ", "")
    lines[i] = lines[i].replace(": Each ore robot costs", "")
    lines[i] = lines[i].replace("ore. Each clay robot costs ", "")
    lines[i] = lines[i].replace("ore. Each obsidian robot costs ", "")
    lines[i] = lines[i].replace("ore and ", "")
    lines[i] = lines[i].replace(" clay. Each geode robot costs", "") 
    lines[i] = lines[i].replace(" obsidian.", "")  
    lines[i] = lines[i].split(" ") 
    num = int(lines[i][0])
    ore_ore = int(lines[i][1])
    clay_ore = int(lines[i][2])
    obsidian_ore = int(lines[i][3])
    obsidian_clay = int(lines[i][4])
    geode_ore = int(lines[i][5])
    geode_obsidan = int(lines[i][6])
    blueprints.append([ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidan])

for blueprint in blueprints:  
    print(blueprint)
    print(simulate_blueprint(blueprint, 0, 0, 0, 0, 1, 0, 0, 0, 1))

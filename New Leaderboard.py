# List of all available upgrades
all_upgrades = [
	#Unlocks.Plant,
    Unlocks.Carrots,
    Unlocks.Pumpkins,
    Unlocks.Trees,
    Unlocks.Sunflowers,
    Unlocks.Cactus,
    Unlocks.Dinosaurs,	
    Unlocks.Expand,
	Unlocks.Fertilizer,
	Unlocks.Mazes,
	Unlocks.Watering,
	Unlocks.Speed,
	
	Unlocks.Leaderboard
    # Add more unlocks here
]

def hay():
        for i in world_range():
            goto(i)
            if can_harvest():
                harvest()
    
def wood():
    for i in world_range():
        goto(i)

    if can_harvest():
        harvest()
	#Check for water, wood checks
    water()

    x, y = conv_xy(i)
    if x % 2 == y % 2:
        if get_entity_type() != Entities.Tree:
            plant(Entities.Tree)
    else:
        if get_entity_type() != Entities.Bush:
            plant(Entities.Bush)

    goto(i)

    if can_harvest():
        harvest()

    water()

    x, y = conv_xy(i)
    if x % 2 == y % 2:
        if get_entity_type() != Entities.Tree:
            plant(Entities.Tree)
    else:
        if get_entity_type() != Entities.Bush:
            plant(Entities.Bush)
    
def carrot():
    for i in world_range():
        goto(i)
    
        if can_harvest():
            harvest()
    
        water()
    
        if get_entity_type() != Entities.Carrots:
            plant(Entities.Carrots)
    
def pumpkin():
    queue = list(world_range())
    
    while len(queue) > 0:
        next = queue.pop(0)
        goto(next)
        if get_entity_type() != Entities.Pumpkin:
            if not plant(Entities.Pumpkin):
                return False
            water()
            queue.append(next)
        elif not can_harvest():
            queue.append(next)
    
    while not can_harvest():
        pass
    harvest()
    
    return True
    
def power():
    petal_coords = dict()
    
    for i in world_range():
        goto(i)
    
        if get_entity_type() != Entities.Sunflower and not plant(Entities.Sunflower):
            return False
    
        petals = measure()
    
        if petals not in petal_coords:
            petal_coords[petals] = list()
    
        petal_coords[petals].append(i)
    
    req = controller[Items.Power][required_amt]
    while num_items(Items.Power) < req:
        l = list()
        for k in petal_coords:
            l.append(k)
        quick_print(l)
        p = max(petal_coords)
        i = petal_coords[p].pop()
        if len(petal_coords[p]) == 0:
            petal_coords.pop(p)
        goto(i)
    
        while not can_harvest():
            fertilize()
        harvest()
   
        if not plant(Entities.Sunflower):
            return False
    
        petals = measure()
        if petals not in petal_coords:
            petal_coords[petals] = list()
        petal_coords[petals].append(i)
    
def cactus():
    cacti_sort()


# Dictionary mapping plant functions to required unlocks
plant_unlocks = {
    hay: [],
    wood: [Unlocks.Trees],
    carrot: [Unlocks.Carrots],
    pumpkin: [Unlocks.Pumpkins],
    power: [Unlocks.Sunflowers],
    cactus: [Unlocks.Cactus],
    dinosaurs: [Unlocks.Dinosaurs]
}


# List to store unlocked upgrades
current_upgrades = []

# List of plants and their corresponding functions

plants = [
    {
        'entity': Entities.Grass,
        'function': hay,
        'cost': get_cost(Unlocks.Grass),
        'seed_cost': None,  # Grass doesn't have a seed
        'max_upgrades': 15,
        'current_upgrades': 2
    },
    {
        'entity': Entities.Bush,
        'function': wood,
        'cost': None,
        'seed_cost': None,  # Bushes don't have a seed
        'max_upgrades': 15,
        'current_upgrades': 1
    },
    {
        'entity': Entities.Carrots,
        'function': carrot,
        'cost': get_cost(Unlocks.Carrots),
        'seed_cost': get_cost(Items.Carrot_Seed),
        'max_upgrades': 15,
        'current_upgrades': 0
    },
    {
        'entity': Entities.Tree,
        'function': wood,
        'cost': get_cost(Unlocks.Trees),
        'seed_cost': None,  # Trees don't have a seed
        'max_upgrades': 15,
        'current_upgrades': 0
    },
    {
        'entity': Entities.Pumpkin,
        'function': pumpkin,
        'cost': get_cost(Unlocks.Pumpkins),
        'seed_cost': get_cost(Items.Pumpkin_Seed),
        'max_upgrades': 15,
        'current_upgrades': 0
    },
    {
        'entity': Entities.Sunflower,
        'function': power,
        'cost': get_cost(Unlocks.Sunflowers),
        'seed_cost': get_cost(Items.Sunflower_Seed),
        'max_upgrades': 15,
        'current_upgrades': 0
    },
    {
        'entity': Entities.Cactus,
        'function': cactus,
        'cost': get_cost(Unlocks.Cactus),
        'seed_cost': get_cost(Items.Cactus_Seed),
        'max_upgrades': 15,
        'current_upgrades': 0
    },
    {
        'entity': Entities.Dinosaur,
        'function': dinosaurs,
        'cost': get_cost(Unlocks.Dinosaurs),
        'seed_cost': get_cost(Items.Egg),
        'max_upgrades': 15,
        'current_upgrades': 0
    }
]

current_items = {
	    Items.Hay: num_items(Items.Hay),
	    Items.Wood: num_items(Items.Wood),
	    Items.Carrot: num_items(Items.Carrot),
	    Items.Pumpkin: num_items(Items.Pumpkin),
	    Items.Gold: num_items(Items.Gold),
	    Items.Power: num_items(Items.Power),
	    Items.Cactus: num_items(Items.Cactus),
	    Items.Bones: num_items(Items.Bones),
	    # Add more items here
	}

upgrade_costs = {
    #Unlocks.Plant: get_cost(Unlocks.Plant),
    Unlocks.Carrots: get_cost(Unlocks.Carrots),
    Unlocks.Pumpkins: get_cost(Unlocks.Pumpkins),
    Unlocks.Trees: get_cost(Unlocks.Trees),
    Unlocks.Sunflowers: get_cost(Unlocks.Sunflowers),
    Unlocks.Cactus: get_cost(Unlocks.Cactus),
    Unlocks.Dinosaurs: get_cost(Unlocks.Dinosaurs),
    Unlocks.Expand: get_cost(Unlocks.Expand),
    Unlocks.Fertilizer: get_cost(Unlocks.Fertilizer),
    Unlocks.Mazes: get_cost(Unlocks.Mazes),
    Unlocks.Watering: get_cost(Unlocks.Watering),
    Unlocks.Speed: get_cost(Unlocks.Speed),
    Unlocks.Leaderboard: get_cost(Unlocks.Leaderboard)
}

# List of current items
def get_item_counts():
	current_items = {
	    Items.Hay: num_items(Items.Hay),
	    Items.Wood: num_items(Items.Wood),
	    Items.Carrot: num_items(Items.Carrot),
	    Items.Pumpkin: num_items(Items.Pumpkin),
	    Items.Gold: num_items(Items.Gold),
	    Items.Power: num_items(Items.Power),
	    Items.Cactus: num_items(Items.Cactus),
	    Items.Bones: num_items(Items.Bones),
	    # Add more items here
	}
	return current_items
	
def unlock_upgrades():
    quick_print("Unlocking upgrades...")
    current_items = get_item_counts()
    upgrades_to_remove = []

    for upgrade in all_upgrades:
        quick_print("Upgrades: \n\n")
        quick_print(all_upgrades)
        if upgrade not in current_upgrades:
            #cost = plants[plant['cost']]
            #print(cost)
            #quick_print(cost)
            #cost = upgrade_costs[upgrade]
            cost = get_cost(upgrade)
            quick_print(cost)
            if cost == None:
                quick_print("Unlocking")
                quick_print(upgrade)
                quick_print(cost)
                quick_print("Cost ^")
                unlock(upgrade)
                current_upgrades.append(upgrade)
            else:
                can_unlock = True
                for item in cost:
                    if current_items[item] < cost[item]:
                        can_unlock = False
                        break
                    else:
                        quick_print("something here")
                        pass

                if can_unlock:
                    quick_print("Unlocking")
                    quick_print(upgrade)
                    unlock(upgrade)
                    current_upgrades.append(upgrade)
                    upgrades_to_remove.append(upgrade)
                    
                    for item in cost:
                        current_items[item] -= cost[item]
                else:
                    current_items = get_item_counts()
                    quick_print("Could not get upgrade")
    for upgrade in upgrades_to_remove:
        all_upgrades.remove(upgrade)
    if all_upgrades == []:
        return




def can_unlock(upgrade, current_items):
    quick_print(upgrade)
    quick_print("Upgrade above!!")
    cost = get_cost(upgrade)
    quick_print(cost)
    if cost == None:
        return True
    for item in cost:
        if current_items[item] < cost[item]:
            return False
    return True

#def gather_resources():
#    for plant in plants:
#		quick_print("Plants:")
#		quick_print(plant)
#       if plant['current_upgrades'] == 0:
#            pass
#        if plant['current_upgrades'] < plant['max_upgrades']:
#            if can_afford(plant['cost']):
#                plant['function']()
#                plant['current_upgrades'] += 1
#                update_current_items(plant['cost'])
#            else:
#                trade_for_resources(plant['cost'])

def gather_resources():
    quick_print("Gathering resources...")
    for upgrade in upgrade_costs:
        quick_print(upgrade)
        #if num_items> upgrade[1]


    for plant in plants:
        if plant['current_upgrades'] <= 0:
			
            pass
        else:
            quick_print("Processing plant:")
            quick_print(plant['entity'])
            quick_print(plant['current_upgrades'])
            if plant['current_upgrades'] <= plant['max_upgrades']:
                required_unlocks = plant_unlocks[plant['function']]
                unlocks_satisfied = True
	
                for unlock in required_unlocks:
                    if unlock not in current_upgrades:
                        quick_print(current_upgrades)
                        unlocks_satisfied = False
                        break
	
                if unlocks_satisfied:
                    quick_print("Required unlocks satisfied for")
                    quick_print(plant['entity'])
                    cost = plant['cost']
                    quick_print(cost)
                    if cost == None:
                        plant['function']()
                        quick_print("Cost equals None")
                        break
                    if can_afford(plant['cost']):
                        quick_print("Calling function for")
                        quick_print(plant['entity'])
                        #plant['function']()
                        #current_items = get_item_counts()
                        unlock_upgrades()
                        #can_unlock()
                        plant['current_upgrades'] += 1
                        quick_print(plants)
                        #update_current_items(plant['cost'])
                        plant['function']()
                    else:
                        quick_print("Trading for resources for")
                        quick_print(plant['entity'])
                        trade_for_resources(plant['seed_cost'])
                else:
                    quick_print("Required unlocks not satisfied for")
                    quick_print(plant['entity'])
                
         
       


def can_afford(cost):
    quick_print("Cost in can afford")
    quick_print(cost)
    if cost == None:
        return True
    for item in cost:
        quick_print(cost)
        current_items = get_item_counts()
        if current_items[item] < cost[item]:
            return False
    return True

def update_current_items(cost):
    if cost != None:
        for item in cost:
            current_items[item] -= cost[item]

def trade_for_resources(seed_cost):
    if seed_cost != None:
        for item in seed_cost:
            if current_items[item] < seed_cost[item]:
                trade_amount = seed_cost[item] - current_items[item]
                if trade(item, trade_amount):
                    current_items[item] += trade_amount
                else:
                    quick_print("Failed to trade for:")
                    quick_print(item)

def main():
    #unlock_upgrades()
	
    cost = get_cost(Unlocks.Speed)[Items.Hay] + get_cost(Unlocks.Expand)[Items.Hay]
    while num_items(Items.Hay) < cost:
        harvest()
    unlock(Unlocks.Speed)
    unlock(Unlocks.Expand)

    cost = get_cost(Unlocks.Plant)[Items.Hay]
    while num_items(Items.Hay) < cost:
        move(North)
        harvest()
    unlock(Unlocks.Plant)
    #goto(0, 0)
    clear()
    move(North)
    #quick_print_unlock()
    print_all_unlocks()
    while (num_items(Items.Wood) < 40):
        for i in world_range():
            goto(i)
            if can_harvest():
                harvest()
            if (num_items(Items.Hay) > 101):
                if get_entity_type() != Entities.Bush:
                     plant(Entities.Bush)

                #plant(Entities.Bush)
                #move(North)

                     if can_harvest():
                        harvest()
            unlock(Unlocks.Expand)
            unlock(Unlocks.Speed)
            unlock(Unlocks.Grass)

			
			 
	#unlock(Unlocks.Plant)
    move(North)    move(North)
    unlock_upgrades()
    while True:
        
        gathers()
        #unlock_upgrades()


timed_reset()

main()
timed_reset()
def GetUnlocksData():
	grass = [
		{Items.Hay: 100},
		{Items.Hay: 300},
		{Items.Hay: 450},
		{Items.Hay: 675},
		{Items.Hay: 1010},
		{Items.Hay: 1520},
		{Items.Hay: 2280},
		{Items.Hay: 3420},
		{Items.Hay: 5130},
		{Items.Hay: 7690},
		{Items.Hay: 11500},
		{Items.Hay: 17300}
	]

	speed = [
		{Items.Hay: 20},
		{Items.Wood: 10},
		{Items.Wood: 50, Items.Carrot: 100},
		{Items.Wood: 100, Items.Carrot: 200},
		{Items.Carrot: 350},
		{Items.Carrot: 500},
		{Items.Carrot: 800},
		{Items.Carrot: 1100},
		{Items.Carrot: 1400},
		{Items.Carrot: 1700},
		{Items.Carrot: 2100},
		{Items.Carrot: 2500},
		{Items.Power: 2000},
		{Items.Power: 2600},
		{Items.Power: 3380},
		{Items.Power: 4390},
		{Items.Power: 5710},
		{Items.Power: 7430},
		{Items.Power: 9650},
		{Items.Power: 12500}
	]

	trees = [
		{Items.Wood: 50, Items.Carrot: 200},
		{Items.Hay: 300},
		{Items.Hay: 480},
		{Items.Hay: 768},
		{Items.Hay: 1230},
		{Items.Hay: 1970},
		{Items.Hay: 3150},
		{Items.Hay: 5030},
		{Items.Hay: 8050},
		{Items.Hay: 12900},
		{Items.Hay: 20600},
		{Items.Hay: 33000}
	]

	carrots = [
		{Items.Wood: 100},
		{Items.Wood: 300},
		{Items.Wood: 480},
		{Items.Wood: 768},
		{Items.Wood: 1230},
		{Items.Wood: 1970},
		{Items.Wood: 3150},
		{Items.Wood: 5030},
		{Items.Wood: 8050},
		{Items.Wood: 12900},
		{Items.Wood: 20600},
		{Items.Wood: 33000}
	]

	expand = [
		{Items.Hay: 30},
		{Items.Wood: 20},
		{Items.Wood: 50, Items.Carrot: 50},
		{Items.Wood: 100, Items.Pumpkin: 200},
		{Items.Pumpkin: 500},
		{Items.Pumpkin: 1750},
		{Items.Pumpkin: 6120},
		{Items.Pumpkin: 21400},
		{Items.Pumpkin: 75000}
	]

	pumpkins = [
		{Items.Wood: 500, Items.Carrot: 1000},
		{Items.Carrot: 1200},
		{Items.Carrot: 1920},
		{Items.Carrot: 3070},
		{Items.Carrot: 4920},
		{Items.Carrot: 7860},
		{Items.Carrot: 12600},
		{Items.Carrot: 20100},
		{Items.Carrot: 32200},
		{Items.Carrot: 51500}
	]

	mazes = [
		{Items.Carrot: 2000, Items.Pumpkin: 3000},
		{Items.Pumpkin: 4000},
		{Items.Pumpkin: 8000},
		{Items.Pumpkin: 16000},
		{Items.Pumpkin: 32000}
	]
	
	sunflowers = [
		{Items.Carrot:500},
		{Items.Gold:1000},
		{Items.Gold:2000},
		{Items.Gold:4000},
		{Items.Gold:8000},
		{Items.Gold:16000}
	]

	cactus = [
		{Items.Gold:5000},
		{Items.Gold:10000},
		{Items.Gold:20000},
		{Items.Gold:40000}
	]

	dinosaurs = [
		{Items.Cactus:5000},
		{Items.Cactus:1000},
		{Items.Cactus:2000}
	]

	data = {
		Unlocks.Grass: grass,
		Unlocks.Speed: speed,
		Unlocks.Trees: trees,
		Unlocks.Carrots: carrots,
		Unlocks.Expand: expand,
		Unlocks.Pumpkins: pumpkins,
		Unlocks.Mazes : mazes,
		Unlocks.Sunflowers : sunflowers,
		Unlocks.Cactus : cactus,
		Unlocks.Dinosaurs : dinosaurs,

		Unlocks.Plant : [{Items.Hay:50}],
		Unlocks.Watering : [{Items.Carrot:100}],
		Unlocks.Multi_Trade : [{Items.Carrot:300}],
		Unlocks.Fertilizer : [{Items.Pumpkin:1000}],

		Unlocks.Polyculture : [{
			Items.Hay : 3000,
			Items.Wood :3000,
			Items.Carrot : 3000
		}],

		Unlocks.Leaderboard : [{Items.Bones:2000}]
	}

	return data

data = GetUnlocksData()
quick_print(data)
for upgrade in data:
	quick_print("Upgrade: ", upgrade)
	#quick_print(upgrade)
	#if upgrade == Unlocks.Plant:
	#	for mat in data[upgrade][0]:
	#		quick_print("Cost Plant:")
	#		quick_print(mat)
	#		cost = data[upgrade][0][mat]
	#		quick_print(cost)
			#quick_print(data[upgrade][mat][0])
    #for length in range(len(data[upgrade])):
    length = len(data[upgrade])
    length = length - 1
    if length < -1:
        quick_print("Length less than -1")
        for i in data[upgrade][0]:
            quick_print("Data[Upgrade][0][i]")
            quick_print(data[upgrade][0][i])
        #quick_print(
    quick_print("Length of:")
    quick_print(upgrade, length)
    for i in data[upgrade]: #[0]
        quick_print('Upgrade:', i, data[upgrade])
        #quick_print(i, data[upgrade][0][i], upgrade)
        #data[upgrade].pop(0)
		#data[upgrade][0].pop()
        quick_print(data)
    quick_print(data[upgrade][0])
    data.pop(data[upgrade][0])
	#quick_print(data[upgrade][0])
	#for cost in data[upgrade]:
		#quick_print(cost)
		
#unlocks = data	
#quick_print(unlocks[Unlocks.Grass]) # prints all unlocks for Grass
#quick_print(unlocks[Unlocks.Grass][0]) # print the first unlock for Grass
#for i in unlocks[Unlocks.Grass][0]:
#    quick_print(i, unlocks[Unlocks.Grass][0][i]) # prints the Entities and amount of the first unlock for Grass
#quick_print(data[0])
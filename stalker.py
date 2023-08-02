import textwrap		# used to format long sentences to fit
import os			# used to clear the screen
import time			# used to put pauses in
import pickle		# used to save and load games
import random		# used in the guard routine

def initialize_game():
	locations = load_locations()
	location = 35	# location 35 is the starting position
	holding = ['a copek', 'a copek', 'a copek', 'a strip of rag with a nut tied to it']
	return location, locations, holding

def introduction():
	os.system('clear')
	print()
	print("          ╔══════════════════════════════════════╗")
	print("          ║              STALKER                 ║")
	print("          ║                                      ║")
	print("          ║           A text adventure           ║")
	print("          ║                  by                  ║")
	print("          ║           Richard Tatschner          ║")
	print("          ║                                      ║")
	print("          ║           based on the book by       ║")
	print("          ║        Boris and Arcady Strugatsky   ║")
	print("          ║            and the film by           ║")
	print("          ║           Andrei Tarkovsky           ║")
	print("          ║                                      ║")
	print("          ╚══════════════════════════════════════╝")
	time.sleep(5)
	os.system('clear')
	print()
	wrap_description("This adventure is set in the very distant future. Many, many years ago, something landed a little way from the village you live in. This was called the visitation and the place where it landed became known as the zone. At first people went to visit, but none ever came back.")
	print()	
	wrap_description("Then the military sealed the whole area off and declared it out of bounds. After that practically everything stopped working properly. Nobody comes to the village anymore and the villagers are not allowed to leave.")
	print()
	wrap_description("It is rumoured that many treasures exist there but also many dangers and only the very cunning and careful ever get out alive. These people are called Stalkers.")
	print()
	print("You are Redrick, the stalker.")
	print()
	wrap_description("But it is also said that those who return come back altered somehow. Their children are weird and they have a hunted look in their eyes.")
	print()
	print("There is help available.\n")
	input("Press enter to begin your quest as Redrick.")
	
def load_locations():
	print("loading locations")
	locations = {0:{
		"full_description": "A sudden surge of water sweeps you off your feet and down a flooded passage at speed. Suddenly you drop down the vertical shaft of a very deep well. You tread water until you drown.",
		"short_description": "You are in a deep well.", 
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		1:{
		"full_description": "You are in a flooded tunnel. The water is now up to your waist. To the east you see light,		to the west you can hear rushing water.",
		"short_description": "You are in a flooded tunnel", "north": False, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		2:{
		"full_description": "You are in an east-west tunnel that slopes downwards to the west. A draught blows your hair awry. There is little light to the west but you can hear a murmuring sound.",
		"short_description": "You are in a sloping tunnel.", 
		"north": False, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		3:{
		"full_description": "You are at the entrance to a cave. Your seeker flew this way but you see no sign of it. There is water dripping from the ceiling.", "short_description": "You are at the entrance to a cave.", 
		"north": False, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		4:{
		"full_description": "You are at the end of a cave. A steel vault door bars your way to the east. It may have a lot of rust patches on it but it looks very strong. It has a small rusty keyhole in it.",
		"short_description": "You are at the end of the cave.",
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a rusty key"},
		5:{
		"full_description": "Behind you is the cave. Ahead of you is a steel tunnel. It is rotating at great speed. It appears to be lined with spikes and blades. You can see the rotating cogs that drive it.",
		"short_description": "You are in the meat grinder",
		"north": False, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a chain"},
		6:{
		"full_description": "Gingerly you step amongst the flailing spikes and you duck the razor knives. Then you stumble.... ...and very quickly you realise why you know this as the meat grinder!",
		"short_description": "You are in the meat grinder",
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		7:{
		"full_description": "You are walking slowly amongst spikes and knives. You think that you just heard one of the chain links snap. Now would be a good time to hurry.",
		"short_description": "You are in the meat grinder",
		"north": False, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		8:{
		"full_description": "You have strayed into a fire field. Too late you remember your blanket. Your skin starts peeling from you and your brain begins to boil.",
		"short_description": "You are in fire field",
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		9:{
		"full_description": "You have entered the old water works that served the village. All the machinery is rotten and rusted. A black wolf stands at the edge of a large puddle to the east.",
		"short_description": "You are at the water works",
		"north": False, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		10:{
		"full_description": "You walk into the puddle. Suddenly something snags your feet and drags you very quickly towards the center of the water which gets very deep. You are dragged under.",
		"short_description": "You are in a gravity well.",
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		11:{
		"full_description": "You are standing on a cross of planks. To the north is an opening, to the east is the lake, to the west is a large puddle and to the south is the marsh.",
		"short_description": "You are on planks across water", 
		"north": True, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a seeker"},
		12:{
		"full_description": "You are standing on the lake shore. The water is so calm that its surface is like a mirror. This is a good place to rest. Across the lake you can see the back wolf. He is looking back at you.",
		"short_description": "You are at the lake shore",
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": ['a knife'], "puzzle": "a seeker"},
		13:{
		"full_description": "You are in a large derelict room. It is raining heavily here although none of the other rooms are even wet. The floor is littered with rusted and broken weapons. Your quest is nearly at an end.",
		"short_description": "You are in the rain chamber",
		"north": False, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		14:{
		"full_description": "The room you have entered is bathed in a golden light emanating from a golden ball which hovers in the air in the middle of the room. The black wolf stands by the south door.",
		"short_description": "You are in the gold chamber.",
		"north": False, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": ['the gold ball'], "puzzle": "The golden ball"},
		15:{
		"full_description": "You are standing at the top of a steel stairway which leads south into water but emerges on the other side to a big steel platform.",
		"short_description": "You are in the water chamber",
		"north": True, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		16:{
		"full_description": "You are standing in a very bare field. The earth is blackened and hard as if baked. It is becoming very hot suddenly.",
		"short_description": "You are in a hot field",
		"north": True, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "an old thick blanket"},
		17:{
		"full_description": "You are in the old pump room. Water drips from the roof and the paint is peeling from the walls. The door to the south leads to the outside and a narrow passage runs to the east.",
		"short_description": "You are in the pump room",
		"north": True, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		18:{
		"full_description": "You are on a narrow walkway over some dark water. To the east is an exit. To the west is the pump room. Things are very dark to the north.",
		"short_description": "You are on a narrow walkway.",  
		"north": True, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		19:{
		"full_description": "You are in the marsh. A series of planks lie to the north. To the south you can see dry land, although there seem to be grave stones there.",
		"short_description": "You are in the marsh.", 
		"north": True, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": ['a pistol'], "puzzle": "a seeker"},
		20:{
		"full_description": "You approach the mansion door. This is the fastest way in for sure. Suddenly, spikes fly out of the door and impale you to the wall behind you. They quickly expand, tearing you into pieces......",
		"short_description": "You are at the mansion door",   
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		21:{
		"full_description": "You are in an office. There is a desk in the middle of the room. The floor boards are uneven and creak as you walk on then. The black wolf sits by the east door.",
		"short_description": "You are in an office", 
		"north": True, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['a phone which is ringing'], "puzzle": "a phone which is ringing"},
		22:{
		"full_description": "The wolf watches you pass. You step into a bright room. The floor moves beneath your feet. Suddenly, you plunge downwards at incredible speed. The descent seems endless, but it isn't......",
		"short_description": "You are in a well", 
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		23:{
		"full_description": "You are up to your chest in dirty water. The platform you are standing on does not feel that stable. Higher platforms are to the north and south.",
		"short_description": "You are in a flooded chamber",  
		"north": True, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		24:{
		"full_description": "You are walking across a large green field, which is littered with the wrecks of many tanks. Weeds are overgrowing them now.",
		"short_description": "You are in a field of tanks",   
		"north": True, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['a machine gun'], "puzzle": "a seeker"},
		25:{
		"full_description": "You are in a covered stores yard. From here you can see the rail embankment you came in on. The black wolf stands to the south and there are piles of old pipes to the east. The pump room lies to the north.",
		"short_description": "You are the stores yard", 
		"north": True, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		26:{
		"full_description": "You are amongst piles of old pipes. These were used all over the area to supply fresh water to the villages. There is an open shed to the south.",
		"short_description": "You are in the pipe room", 
		"north": False, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		27:{
		"full_description": "You have entered a graveyard. Many of the old grave stones have fallen over. You are now right next to the mansion. The front porch is to the east.",
		"short_description": "You are in a graveyard.", 
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a seeker"},
		28:{
		"full_description": "You are standing on the front porch of the mansion. The entrance is to the north. Oddly, there is a seeker stuck to the entrance by a shiny spike. The graveyard is to the west.",
		"short_description": "You are standing on the porch", 
		"north": True, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		29:{
		"full_description": "You are in a hallway. Dusty portraits line the walls. To the north is a smart white door, which is ajar. To the east is the opening to the room of dunes.",
		"short_description": "You are in a hallway", 
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		30:{
		"full_description": "You are standing in a very large room. It is filled with huge piles of sand that resemble dunes. To the north sits the black wolf. Your way west is barred by a large owl.",
		"short_description": "You are in the room of dunes",  
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "some dry seeds"},
		31:{
		"full_description": "You are standing on a raised steel platform, which leads north into water but emerges on the other side to a steel stairway.",
		"short_description": "You are on a steel platform",   
		"north": True, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		32:{
		"full_description": "You are standing by a rusted car. Inside you can see the skeletons of two people. Judging by their rotted clothes they were military men. The telegraph poles end here.",
		"short_description": "You are by a rusted car", 
		"north": True, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a seeker"},
		33:{
		"full_description": "You have entered a rogue gravity field. You feel yourself being thrown to the floor before you pass out. Your body is crushed out of existence. A small stain seeps into the dry earth.",
		"short_description": "You are in a gravity field",		
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		34:{
		"full_description": "You are in a store shed. There are shiny cobwebs in the corners. You had best stay clear of them. There are many items you can't identify and you know the dangers here.",
		"short_description": "You are in a store shed", 
		"north": True, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['a rusty key', 'two weird looking disks'], "puzzle": ""},
		35:{
		"full_description": "You are in a bar. The walls are stained black from fire damage and the floor is littered with  broken glass, spit and debris. The light can hardly penetrate the filthy windows.",
		"short_description": "You are in a dark dirty bar",   
		"north": False, "east": True, "south": False, "west": False, 
		"people": "a barman", "talk": "So, what's it to be, Red?", "washere": False, "items": [], "puzzle": "a copek"},
		36:{
		"full_description": "You are standing on the porch of a bar. Rust has formed on the iron roof above you, and water is dripping through the holes that have formed. The floorboards creak under your weight.",
		"short_description": "You are on the bar porch", 
		"north": False, "east": True, "south": True, "west": True, 
		"people": "Alexei", "talk": "So, Red, where's my empty?", "washere": False, "items": [], "puzzle": "an empty"},
		37:{
		"full_description": "You are standing on a wet road surrounded by tall disused buildings. Some have partly collapsed, others are boarded up. There is an acrid smell here.",
		"short_description": "You are standing on a wet road.",
		"north": False, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		38:{
		"full_description": "You have entered a very damp alley. The buildings on either side overhang and reduce the light. You can see shadows moving in your peripheral vision. But there is nothing there when you look.",
		"short_description": "You are in an alley", 
		"north": False, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		39:{
		"full_description": "You are outside your home. The top floor is unusable because part of the roof is missing. The windows are smudged and dirty and the door creaks in the breeze. There is a small face at the window.",
		"short_description": "You are outside your home.",		
		"north": False, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		40:{
		"full_description": "A long line of telegraph poles runs off in an easterly. You are not very sure which way to go. There is no sign of the black wolf. A steep ravine borders the quarry to the south.",
		"short_description": "You are by a telegraph pole",   
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a seeker"},
		41:{
		"full_description": "You are the end of a rail track. The land slopes down in all directions from here. To the north you can see a store yard. To the west you see a line of telegraph poles. The rails run eastwards.",
		"short_description": "You are at the rail end.", 
		"north": True, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		42:{
		"full_description": "You are on a high rail embankment. The sides are way to steep to descend. You know that there can be very dangerous gravity fields at the base of this embankment. The rails stretch to the eastern horizon.",
		"short_description": "You are on a rail embankment.", 
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		43:{
		"full_description": "You are in a small shed where a set of rail tracks end. The walls are intact and you can't be seen by the soldiers. Here there is a single seater rail cart. It looks very old and abused. The petrol tank is empty.",
		"short_description": "You are by a small rail cart",  
		"north": False, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a can of petrol"},
		44:{
		"full_description": "You have entered a burnt out house. The roof is missing and the rain is coming through. The timbers are blackened charcoal and wreckage litters the floor. There are puddles of water.",
		"short_description": "You are in a burnt out house",  
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['a rusty nail'], "puzzle": ""},
		45:{
		"full_description": "You have reached the center of what used to be a thriving village. You are at the main crossroad. The traffic lights have long since ceased working, but then there's no traffic here these days either.",
		"short_description": "You are at the crossroad", 
		"north": True, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		46:{
		"full_description": "You are at the gates of an old factory you used to work in before the visitation. It is dilapidated now. The gates are chained and padlocked. These look new. A sign reads 'ARMED GUARDS - KEEP OUT!'",
		"short_description": "You are at the gates of a factory",
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a bolt cutter"},
		47:{
		"full_description": "You are in your living room. What paint is left is peeling from the wall. There is a single table in the middle of the room with 3 chairs. A sink in the corner of the room next to a fire stove is dripping.",
		"short_description": "You are in your living room",   
		"north": False, "east": False, "south": True, "west": False, 
		"people": "Zania", "talk": "I've been stuck in this dump all bloody day. Fetch me Pupey, will you?", "washere": False, "items": [], "puzzle": "Pupey"},
		48:{
		"full_description": "You are at the edge of a steep ravine that borders a quarry. The old excavators litter the site. They are rusted. You can make out a skeleton in one of the cabs.",
		"short_description": "You are at the edge of a quarry",
		"north": False, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		49:{
		"full_description": "You are the bottom of a steep embankment. Nettle fields are to the east and what look like a quarry to the west. A very dead looking forest lies to the south.",
		"short_description": "You are at a steep embankment", 
		"north": True, "east": True, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		50:{
		"full_description": "You are at the edge of a nettle field. The nettles stand nearly ten feet high. The seed pods are as big as your fist. If only there were birds here. What a feast they would find. The seed pods are within your grasp.",
		"short_description": "You are in a nettle field", 
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "a rusty nail"},
		51:{
		"full_description": "You have made it to the supply hangar. The guards know you are here and a smattering of bullets hit the building. You know they will not enter since you are too close to the zone. Here is Alexei's jeep.",
		"short_description": "You are in the supply hangar.", 
		"north": False, "east": True, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": "car keys"},
		52:{
		"full_description": "You are in some narrow alley ways they run between the buildings. It's easy to get caught here. So speed is important.  At least the guards are unlikely to shoot you here.",
		"short_description": "You are in the alley ways", 
		"north": False, "east": False, "south": True, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		53:{
		"full_description": "You are standing outside an old shack. The door is missing and an old man sits on the porch in a rocking chair. He is smoking a pipe. It smells like he's burning leaves, which he probably is.",
		"short_description": "You are at Gremko's shack", 
		"north": True, "east": False, "south": False, "west": False, 
		"people": "Gremko", "talk": "I got what you asked for, Red. Do you have the money?", "washere": False, "items": [], "puzzle": "10 copeks"},
		54:{
		"full_description": "You are standing in the old factory car park. There are a few rusted cars here. None of them work. The puddles are mixed with leaked oil and form multi-coloured bands on a black background. It's colder now.",
		"short_description": "You are in the car park", 
		"north": True, "east": False, "south": True, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		55:{
		"full_description": "You are in your bedroom. There is one bed with many heavy blankets on. They are all very old. The window is cracked and is letting cold air in. To the south is your store room.",
		"short_description": "You are in your bedroom", 
		"north": True, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['Pupey'], "puzzle": ""},
		56:{
		"full_description": "You walk into a swamp of blue liquid. Too late you realise this is the witches brew. Your bones start to turn to jelly and you are quickly sucked under. A few bubbles surface.",
		"short_description": "You are in the swamp", 
		"north": False, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		57:{
		"full_description": "You are in the dead forest. The trees have been stripped of their bark and leaves. They look like white skeletons. To the west you can see a black wolf. His yellow eyes are watching you.",
		"short_description": "You are in the dead forest.",   
		"north": True, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		58:{
		"full_description": "You are in a small glade. The earth here is baked hard and it is very warm. The forest gets too dense from here. You can't work out where the heat source is.",
		"short_description": "You are in a small glade.", 
		"north": False, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": ['some dry seeds'], "puzzle": ""},
		59:{
		"full_description": "You are in some out buildings. There is no cover here and you can easily be seen. A window is clattering in the wind. You can hear the motorcycle engine of the guard. Be careful here.",
		"short_description": "You are in the out buildings",  
		"north": True, "east": True, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		60:{
		"full_description": "You are in the railway siding. There is little cover here and you'll have to be quick and quiet not to get caught here. At least the guards are unlikely to shoot you here.",
		"short_description": "You are in the railway siding.",
		"north": True, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		61:{
		"full_description": "You are in the factory yard. Piles of rusting pipework lie in heaps giving you cover from the guards. You know that if you make it to the jeep they won't follow you into the zone. They're far too afraid to risk it.",
		"short_description": "You are in the factory yard",   
		"north": False, "east": True, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		62:{
		"full_description": "You are in the old foundry. The furnaces are cold and the roof is missing. Rain runs down the walls. You can hear a motorcycle engine. You should be careful of the guards. They are more nervous than you.",
		"short_description": "You are in the foundry", 
		"north": True, "east": False, "south": False, "west": True, 
		"people": "", "talk": "", "washere": False, "items": [], "puzzle": ""},
		63:{
		"full_description": "You are in your store room. There are racks of clothing and old pieces of paper. The light is shining though a crack in ceiling where the roof above is missing. Water is trickling down the wall.",
		"short_description": "You are in your store room",		
		"north": True, "east": False, "south": False, "west": False, 
		"people": "", "talk": "", "washere": False, "items": ['a bolt cutter', 'two weird looking disks', '5 copeks', '10 copeks', 'an old thick blanket', 'a notebook']}}
	return locations

def wrap_description(full_description):
	wrapped_description = textwrap.wrap(full_description, width=80)
	for line in wrapped_description:
		print(line)
	return

def is_numeric(prompt, array):	# to ensure that input is numeric
	valid_input = False
	while not valid_input:
		try:
			print()
			#print(f"There are {len(array)} objects here.")
			user_input = int(input(prompt))
			if user_input < 1 or user_input > len(array):
				print("Keep to the numbers, eh?")
			else:
				valid_input = True
		except ValueError:
			print("Try a number rather than a letter.")
	print()
	return user_input

def areyousure():
	yes_or_no = ""
	while yes_or_no not in ('y', 'n', 'yes', 'no'):	
		yes_or_no = input("Are you sure? ")
	if yes_or_no in('y', 'yes'):
		return True
	else:
		return False

def describe_location(location, locations):
	os.system('clear')
	#print(f"\nLocation is {location}.\n")
	if locations[location]['washere'] == False:
		wrap_description(locations[location]['full_description'])
	else:
		print(locations[location]['short_description'])
	print()
	
	locations[location]['washere'] = True
	
	print("You can go ", end='')
	nowhere = True
	if locations[location]['north']:
		nowhere = False
		print("north, ", end='')
	if locations[location]['south']:
		nowhere = False
		print("south, ", end='')
	if locations[location]['east']:
		nowhere = False
		print("east, ", end='')
	if locations[location]['west']:
		nowhere = False
		print("west, ", end='')
	if nowhere:
		print("nowhere.", end='')
	print()
	print()
	
	
	
	if locations[location]['people'] != "":
			print(f"Here is {locations[location]['people']}\n")
	
	if len(locations[location]['items']) != 0:
		print("You find ", end = '')
		for item in locations[location]['items']:
			print(f"{item}{('.' if item == locations[location]['items'][-1] else ', ')}")
	
	return
		
def move_location(location, locations, option):
	invalid_move = True
	if option in ('n', 'north') and locations[location]['north']:
		location -= 8
		invalid_move = False
	elif option in ('s', 'south') and locations[location]['south']:
		location += 8
		invalid_move = False
	elif option in ('e', 'east') and locations[location]['east']:
		location += 1
		invalid_move = False
	elif option in ('w', 'west') and locations[location]['west']:
		location -= 1
		invalid_move = False
	if invalid_move:
		print("You can't go that way.")
		time.sleep(2)
	return location

def talk_to(location, locations):
	if locations[location]['people'] == "":
		print("Great Kruschev! I'm talking to myself")
	else:
		wrap_description(f"{locations[location]['people']} says: {locations[location]['talk']}")
	return
		
def pick_up_object(location, locations, holding):
	if len(locations[location]['items']) == 0:
		print("There is nothing here to pick up.")
	else:
		item_number = 1
		for item in locations[location]['items']:
			print(f"{item_number}. {item}")
			item_number += 1
		item_choice = is_numeric("What do want to pick up? ", locations[location]['items'])
		holding.append(locations[location]['items'][item_choice-1])
		print(f"You have picked up {locations[location]['items'][item_choice-1]}")
		del locations[location]['items'][item_choice-1]
	return

def drop_object(location, locations, holding):
	if len(holding) == 0:
		print("You've got nothing to drop.")
	else:
		item_number = 1
		for item in holding:
			print(f"{item_number}. {item}")
			item_number += 1
		item_choice = is_numeric("What do want to drop? ", holding)
		locations[location]['items'].append(holding[item_choice-1])
		print(f"You have dropped {holding[item_choice-1]}")
		del holding[item_choice-1]
	return

def inventory(holding):
	print("You are carrying:")
	if len(holding) == 0:
		print("nothing")
	else:
		for item in holding:
			print(item)
	return

def use_object(location, locations, holding):
	global DRINKS 			# for location 35 (the bar)
	global SUCCESS			# end of game indicator in location 47
	if len(holding) == 0:
		print("You've got nothing to use.")
	else:
		item_number = 1
		for item in holding:
			print(f"{item_number}. {item}")
			item_number += 1
		item_choice = is_numeric("What do want to use? ", holding)
		if holding[item_choice-1] != locations[location]['puzzle']:
			print("You can't use that here.")
		
		elif location == 4:
			wrap_description("You insert the key into the lock and to your complete surprise the door swings open.")
			locations[location]['full_description'] = locations[location]['full_description'].replace("It has a small rusty keyhole in it", "The door is open")
			locations[location]['east'] = True
			del holding[item_choice-1]
		
		elif location == 5:
			wrap_description("You throw the chain into the mechanism, which abruptly stops. You can hear it straining to break the chain. You have no idea how long it will last. Gingerly you step between the spikes and the razor knives and inch your way forward. All way you hear the engine straining against the chain")
			location = 7
			del holding[item_choice-1]
			
		elif location == 11:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north through a cave opening and out of sight")
			locations[4]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
		
		elif location == 12:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the west")
			locations[11]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
			
		elif location == 13:
			weapon_list = ["a machine gun", "a pistol", "a knife", "a bolt cutter"]
			weapons = []
			for item in weapon_list:
				if item in holding:
					weapons.append(item)
			if len(weapons) != 0:
				wrap_description(f"{weapons[0]} that you are carrying suddenly explodes tearing a large hole in your side. As you bounce off the wall you remember the warning in your notebook......")
				end_game()

		elif location == 14:		# the gold room
			os.system('clear')
			print("Your quest is nearing it's end.")
			print()
			print("You know the golden ball will grant you your innermost wish.")
			print("You only have one go at this.")
			print("So you clear your mind and wish for....")
			print()
			print("(1) I wish I had enough money to get my family away from here.")
			print("(2) I wish that Pupey would be cured of the zone illness.")
			print("(3) I wish the zone had never existed.")
			print()
			print("or (0) to decide later.")
			print()
	
			decide = ['0', '1', '2', '3']
			decision = is_numeric("So, what's it be,Red?", decide)
			if decide == 1:
				print()
				wrap_description("The gold ball starts to spin rapidly and you notice flecks of gold forming on the walls. Too late you realise that the ball is spewing out molten gold! The speed increases as does the molten gold. You feel a searing pain as a load hits you in the face. Then all goes black.")
				end_game()
			elif decide == 2:
				print()
				wrap_description("The gold ball starts to spin rapidly. Back home zania is amazed to see Pupey's body hair fall off her. Her back straightens and her eyes brighten. Pupey is being cured! You however, are now left to find your way out.")
				end_game()
			elif decide == 3:
				print()
				wrap_description("The gold ball starts to spin rapidly. There is a bright flash of light and suddenly you find yourself somewhere very familiar.")
				change_the_matrix(location, locations, holding)
				location = 35
			else:
				print()
				print("Okay, but don't loose the ball.")	
		
		elif location == 16:
			wrap_description("You throw the blanket round yourself as smoke starts to seep out of the ground. You run forward and can see fire billowing around you. Still you run in the direction of the seeker. Your blanket begins to smolder. Finally just as the blanket bursts into flames you turn a sharp right into the old water works. You throw the blanket to the ground where is turns into ash.")
			location = 9
			del holding[item_choice-1]
		
		elif location == 19:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north")
			locations[11]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
		
		elif location ==21:
			wrap_description( "Even though the phone is not connected to anything, you lift the receiver. You recognise the voice.")
			print()
			time.sleep(1)
			print("Red!")
			time.sleep(1)
			print("Purcupine? ...but you're dead.")
			time.sleep(1)
			print("Red, when you find the ball, be truthful with what you wish.")
			time.sleep(1)
			print("Purcupine, what do you mean?")
			time.sleep(1)
			print("Red....fzgl..owqih......ds...zzz.xx....x..z.z.z.z....")
			time.sleep(2)
			print()
			print("The line goes dead.")
			holding.append("a phone")
    
		elif location == 24:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north, then veers to the east and out of sight.")
			locations[9]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
		
		elif location == 27:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north.")
			locations[19]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
		
		elif location == 30:
			wrap_description("You throw the seeds toward the owl, which rise into the air to catch them, As they meet both disappear.")
			del holding[item_choice-1]
			locations[location]['full_description'] = locations[location]['full_description'].replace("Your way west is barred by a large owl.", "Your way west is clear")
			locations[location]['west'] = True
		
		elif location == 32:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north.")
			locations[24]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]

		elif location == 35:
			DRINKS += 1
			wrap_description("The barman pours you a drink from a dusty bottle into a dirty shot glass. You down it in one...")
			if DRINKS == 3:
				wrap_description("...and fall off your bar stool. You lie in the dirt until you sober up.")
			del holding[item_choice-1]
		
		elif location == 36:
			wrap_description("Alexei says 'It's beautiful! I hope you can get me another some time. You know you can place incredible weights on these and they won't budge a centimeter. Incredible. I guess you want to borrow the jeep again. Here are the keys.'")
			print("\nHe hands you a set of car keys.\n")
			print("Good luck!")
			holding.append('car keys')
			locations[location]['talk'] = "We'll have a drink together when you get back."
		
		elif location == 40:
			wrap_description("You throw the seeker into the air. As if grabbed by a strong wind it veers off to the north.")
			locations[32]['items'].append(holding[item_choice-1])
			del holding[item_choice-1]
		
		elif location == 43:
			wrap_description("You fill the tank with petrol and turn the starting handle of this rail cart. The engine fires up and you jump on. It  hugs along the rails, clickety clack, clickety clack. Slowly you notice that the air no longer contains any smell of any kind. The rain has stopped and you are now entering the zone. You sit on the little cart as it makes its way into the heart of the zone. Clickety clack, clickety clack. Nothing moves in the zone. There is no breeze.")
			print()
			wrap_description("Finally you reach the end of the line and you get off the cart. You reverse the engine and send it back along the the track to its shed. You are now in the zone. You know that you can never return the way you came. This is the way of the zone.")
			del holding[item_choice-1]
			location=41
		
		elif location == 46:
			wrap_description("One snip of the bolt cutters to the lock and the chain drops away. The gates swing open.")
			locations[location]['south'] = True
			locations[location]['full_description'] = locations[location]['full_description'].replace("The gates are chained and padlocked. These look new.", "The gates are open.")
			locations[location]['items'].append("a chain")
			locations[location]['items'].append("a broken padlock")
		
		elif location == 47:
			if not SUCCESS:
				wrap_description("You hand Pupey over to Zania. She picks up a small paper bag and says, I'll feed her at Galina's. She gets up and leaves the house with Pupey.")
				locations[location]['people'] = ""
				locations[55]['south'] = True
				locations[location]['north'] = True
				del holding[item_choice-1]
			else: # end of game
				wrap_description("You enter your living room, which is bright and airy. There is a large sofa. Zania is here. She's as beautiful as you remember her when you first met. Sitting next to her is a beautiful young girl. With complete surprise you recognise her as your daughter. She has long dark hair and a beautiful smile. She recognises you and rushes over to embrace you.")
				print("\nWell done! You have cured the curse of the zone.\n")
				close_game()				
    
		elif location == 50:
			wrap_description("You work at the seed pod with the old nail. It's hard going since the nail is blunt. Finally the pod breaks open and spills its moist seeds on the ground.")
			locations[location]['items'].append("some moist seeds")

		elif location == 51:
			wrap_description("You jump into the jeep and gun the engine into life. You drive the jeep at great speed out of the hangar and across the rain lines. The guards have spotted you and start shooting, but you manage to outdrive the hail of bullets. These guys really mean business. Finally you swerve through the barriers that mark the boundaries of the zone. The jeep starts coughing and spluttering. You know it won't work in the zone but you manage to steer it into a deserted out building. You also know that the guards will recover the jeep at some point and sell it back to Alexei.")
			location=43
			del holding[item_choice-1]
			locations[location]['full_description'] = "You walk back into the supply hangar and to your complete surprise, the guards appear to have returned Alexei's jeep here. You must have been wandering longer than you thought."
					
		elif location == 53:
			wrap_description("Gremko gets up and coughs. 'Wait a minute', he says and disappears inside the shack.")
			print("\nHe returns with a can of petrol which he gives you.\n")
			wrap_description("Take care old friend, remember what happened to Porcupine, come back alive, eh?")
			locations[location]['talk'] = "Stay away from the witch's brew, eh Redrick?"
			holding.append('a can of petrol')
			del holding[item_choice-1]
		
		else:
			print("Not coded yet, be patient.")
	return location, locations, holding
	
def guard_routine(location): 
	one_in_five = random.choice(range(1,5))
	#print(f"Chance of getting caught is {one_in_five}.")
	#time.sleep(2)
	if one_in_five == 3:
		print("A guard steps out in front of you and levels his rifle at you.\n")
		wrap_description( "Redrick Shuhart, he says, One of these days you're going to get shot. Come on. Come with me.")
		print("\nHe marches you at gun point to the factory gates.\n")
		print("Now sod off home to your freaky child and stay there, you renegade!\n")
		print("He disappears back across the car park.")
		location=46
		#print(f"Location should be {location}")
		#time.sleep(3)
	return location
	
	
	
def help_screen():
	print()
	print("Commands in this adventure")
	print()
	print("Moving about     n=north,    s=south,    w=west,     e=east")
	print("Handling items   p=pick up,  d=drop,     i=inventory ")
	print("Interacting      t=talk      g=give      u=use       x=examine object")
	print("Assistance       l=look,     m=map       h=help")
	print("File commands    save=save,  load=load")
	print("Quitting         q= quit,    new=restart game")
	print()
	print("Hint - it's well worth examining everything you pick up.")
	return
	
def save_game(location, locations, holding):
	global DRINKS
	global SUCCESS
	with open('data.pkl', 'wb') as file:
		pickle.dump(locations, file)
		pickle.dump(location, file)
		pickle.dump(holding, file)
		pickle.dump(DRINKS, file)
		pickle.dump(SUCCESS, file)
	print(f"Game saved at {locations[location]['short_description']}.")
	return

def load_game(location, locations, holding):
	global DRINKS
	global SUCCESS
	with open('data.pkl', 'rb') as file:
		locations = pickle.load(file)
		location = pickle.load(file)
		holding = pickle.load(file)
		DRINKS = pickle.load(file)
		SUCCESS = pickle.load(file)
	print(f"Game restored to {locations[location]['short_description']}.")
	return location, locations, holding

def restart_game():
	location, locations, holding = initialize_game()
	print("Game reset.")
	return location, locations, holding

def examine_object(holding):
	if len(holding) == 0:
		print("There is nothing here to examine.")
	else:
		item_number = 1
		for item in holding:
			print(f"{item_number}. {item}")
			item_number += 1
		item_choice = is_numeric("What do want to examine? ", holding)
		if holding[item_choice-1] in ('a copek', '5 copeks', '10 copeks'):
			print("A copek is a small coin")
		elif holding[item_choice-1] in ('a strip of rag with a nut tied to it', 'a seeker'):
			wrap_description("This tatty little device has saved your life many a time in the zone. It's just a strip of white rag with a heavy metal nut tied to one end. You call this a seeker.")
			holding[item_choice-1] = "a seeker"
		elif holding[item_choice-1] in ('two weird looking disks', 'an empty'):
			wrap_description("You brought this back the last time you went into the zone. It's weird. There are two disks about six inches apart with nothing between them. You can't press them together nor pull them apart. They look like the top and bottom of a can with the middle absent. You call this an 'empty'.")
			holding[item_choice-1] = "an empty"
		elif holding[item_choice-1] == 'Pupey':
			wrap_description("It breaks your heart every time you look at your daughter. She may be be fifteen years old but she has the body of a seven year old and she is covered with short thick hair which resembles fur. Her big brown eyes look up at you lovingly. She put her arms around your neck and says 'Papa'. This is the curse you brought back from the zone those many years ago.")
		elif holding[item_choice-1] == 'a bolt cutter':
			wrap_description("This is a heavy duty piece of kit. Ideal for cutting through bolts and sometimes even padlocks.")
		elif holding[item_choice-1] == 'a chain':
			wrap_description("This is a very thick and heavy chain. It looks like it would take a great deal to break this one.")
		elif holding[item_choice-1] == 'an old thick blanket':
			wrap_description("It's been impregnated with something that will keep you warm and dry. It might even protect you for a short time from fire. It doesn't smell too good, though.")
		elif holding[item_choice-1] == 'a notebook':
			print("This is a collection of notes you've made about the zone.\n")
			wrap_description("From the telegraph poles until you're through the meat grinder only follow the seeker.")
			print("\nDo not stray from the seeker, but remember that it won't work indoors.\n")
			print("Never carry anything sharp nor anything that is weaponlike.\n")
			wrap_description("Always pick some nettle seeds and leave them in the glade to dry. Use the ones I left there previously.")
			print()
			wrap_description("There is a dog in the zone. I don't know how he survives. He seems to know where danger is.")
			print()
			print("Don't take this into the zone.")
		elif holding[item_choice-1] == 'a rusty nail':
			print("it's a blunt rusty nail.")
		elif holding[item_choice-1] == 'a knife':
			print("It's a fine knife with a keen blade")
		elif holding[item_choice-1] == 'the gold ball':
			wrap_description("This is the fabled ball of wishes. It is said that it will grant your innermost wish, but only the pure of heart may use it.")
		elif holding[item_choice-1] in ('a pistol', 'a machine gun'):
			print("It is a fine gun. It is well oiled and clean and it is loaded.")	
		else:
			print("it is what it is")
	return holding

def draw_map(location, locations):
	print("Not coded yet, be patient.")
	return

def change_the_matrix(location, locations, holding):
	locations[35]['full_description'] = "You are in a bar. The walls are brightly coloured and a jaunty piece of folk music is playing on the juke box. There are many people sitting at tables drinking and eating."
	locations[35]['short_description'] = "You are in nice bright bar"
	locations[35]['north'] = False
	locations[35]['east'] = True
	locations[35]['south'] = False
	locations[35]['west'] = False
	locations[36]['full_description'] = "You are standing on the porch of a bar. Fresh flowers hang in baskets from the beams. The smell of fresh food wafts out of the doorway."
	locations[36]['short_description'] = "You are on the bar porch"
	locations[36]['north'] = False
	locations[36]['east'] = True
	locations[36]['south'] = True
	locations[36]['west'] = True
	locations[37]['full_description'] = "You are standing on the pavement of a busy road. There are tall office buildings on both sides of the with coffee bars and restaurants."
	locations[37]['short_description'] = "You are standing on a busy road"
	locations[37]['north'] = False
	locations[37]['east'] = True
	locations[37]['south'] = True
	locations[37]['west'] = True
	locations[38]['full_description'] = "You have entered a alley. There is a bustling market here with stalls selling fruit and vegetables. The place is full of people buying their groceries."
	locations[38]['short_description'] = "You are in an alley"
	locations[38]['north'] = False
	locations[38]['east'] = True
	locations[38]['south'] = False
	locations[38]['west'] = True
	locations[39]['full_description'] = "You are outside your home. A clean white picket fence surrounds a beautiful garden. There are flowers and a small pond with fish in it. The house windows are open to the sunshine."
	locations[39]['short_description'] = "You are outside your home."
	locations[39]['north'] = False
	locations[39]['east'] = False
	locations[39]['south'] = True
	locations[39]['west'] = True
	locations[44]['full_description'] = "You are standing outside of the town hall. The people are coming and going."
	locations[44]['short_description'] = "You are at the town hall"
	locations[44]['north'] = True
	locations[44]['east'] = True
	locations[44]['south'] = False
	locations[44]['west'] = False
	locations[45]['full_description'] = "You have reached the center of a thriving village. You are at the main crossroad. The traffic lights are working hard marshalling the busy traffic."
	locations[45]['short_description'] = "You are at the crossroad"
	locations[45]['north'] = True
	locations[45]['east'] = True
	locations[45]['south'] = True
	locations[45]['west'] = True
	locations[46]['full_description'] = "You are at the gates of a factory. The yards are full of goods and trucks are coming and going. You decide not to enter."
	locations[46]['short_description'] = "You are at the gates of a factory"
	locations[46]['north'] = False
	locations[46]['east'] = False
	locations[46]['south'] = False
	locations[46]['west'] = True
	locations[47]['full_description'] = "You are in your living room."
	locations[47]['short_description'] = "You are in your living room."
	locations[47]['north'] = False
	locations[47]['east'] = False
	locations[47]['south'] = False
	locations[47]['west'] = False
	locations[53]['full_description'] = "You are standing outside a small bungalow. A young man sits on the porch in a deck He is smoking a pipe. It smells like sweet vanilla."
	locations[53]['short_description'] = "You are at Gremko's house"
	locations[53]['north'] = True
	locations[53]['east'] = False
	locations[53]['south'] = False
	locations[53]['west'] = False
	
	locations[35]['talk'] = "You look beat, Red. Go home to your wife."
	locations[36]['talk'] = "Hi Red. Another great day, isn't it?"
	locations[53]['talk'] = "Hi Red, how's that gorgeous girl of yours?"
	
	for location_number in range(0, 63):
		locations[locations_number]['puzzle'] = ""
		locations[locations_number]['items'] = []
	holding = []
	return location, locations, holding
	
def close_game():
	input("Enter to finish.")
	raise SystemExit

def end_game():
	os.system('clear')
	time.sleep(3)
	print("Zania is bathing Pupey. She feels a change in the air.")
	print("Pupey looks at a floating soap bubble. She pops it and says,")
	print("\nPapa gone.\n")
	print("Zania starts to cry")
	print("\n\nYour quest has ended prematurely.\n")
	close_game()

def check_for_guards(location):
	if location in [59, 60, 61]:		# one in five chance of being returned to the gate
		location = guard_routine(location)
		#print(f"Location return is {location}")
		#input()
	return location

def check_for_traps(location):	
	if location in [0, 6, 8, 10, 20, 22, 33, 56]:		# places where you get scrambled
		end_game()
	return location

# Main routine 
location, locations, holding = initialize_game()
DRINKS = 0 # global count of number of drinks taken in the bar
SUCCESS = False # end of game indicator
#introduction()
option = ""
describe_location(location, locations)
while True:
	#describe_location(location, locations)
	location = check_for_guards(location)
	location = check_for_traps(location)
	
	option = input("\nWhat do want to do? ")
	print()
	if option in ('north', 'south', 'east', 'west', 'n', 's', 'e', 'w'):
		location = move_location(location, locations, option)
		describe_location(location, locations)
	elif option in ('talk', 't'):
		talk_to(location, locations)
	elif option in ('pick', 'p'):
		pick_up_object(location, locations, holding)
	elif option in ('drop', 'd'):
		drop_object(location, locations, holding)
	elif option in ('inventory', 'i'):
		inventory(holding)
	elif option in ('use', 'u', 'give', 'g'):
		use_object(location, locations, holding)
	elif option == "save":
		save_game(location, locations, holding)
	elif option == "load":
		location, locations, holding = load_game(location, locations, holding)
	elif option in ('examine', 'x'):
		holding = examine_object(holding)
	elif option in ('look', 'l'):
		locations[location]['washere'] = False
		describe_location(location, locations)
	elif option in ('help', 'h'):
		help_screen()
	elif option in ('map', 'm'):
		draw_map(location, locations)
	elif option == "new":
		location, locations, holding = restart_game()
	elif option in ('exit', 'quit', 'q'):
		leave_game = areyousure()
		if leave_game:
			close_game()
		else:
			option = ""
	else:
		print("This is not an option, yet.")

print("Exiting")


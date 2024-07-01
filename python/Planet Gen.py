import random


# list to store planet data in.
# 0 starport
# 1 world size
# 2 atmosphere
# 3 hydrographics
# 4 population
# 5 government
# 6 law level
# 7 tech level

#index = int(input("Enter the index of the planet you would like to retrieve "))
list_of_planets = []
planet = [0]
sub_sector = {}


total_die_roll = 0


################# dice
def roll_1_D_6():
    total_die_roll = random.randrange(1,6)
    #print (f'You rolled 1D6 and got {total_die_roll}')
    return total_die_roll


def roll_2_D_6():
    total_die_roll = random.randrange(2,12)
    #print (f'You rolled 2D6 and got {total_die_roll}')
    return total_die_roll






##### planet gen section
##### world gen
def gen_world_size():
    #world size is 2d6-2
    roll = roll_2_D_6()
    world_size = roll - 2
   
    print(f'World Size roll is {roll} - 2, total is {world_size}')
    planet.append(world_size)


##### atmosphere
def gen_atmosphere():
    #atmo = 2d6-7+ world size
    roll = roll_2_D_6()
    planet_size = planet[1]
    atmosphere = (roll - 7) + planet_size
    if atmosphere < 0:
        atmosphere = 0
    print(f'atmosphere roll: {roll} - 7 + {planet_size}')
    planet.append(atmosphere)
   
##### hydrographics
def gen_hydrographics():
    #hydro = 2d6 -7 + world size + atmo mod
    roll = roll_2_D_6()
    planet_size = planet[1]
    atmo = planet[1]
    mod = 0
    pre_atmo = (roll - 7) + planet_size
    if atmo <1 or (atmo >= 10 and atmo <= 12):
        mod = -4
    elif atmo == 15:
        mod = -2
    hydro = pre_atmo + mod
   
    if planet_size <= 1:
        hydro = 0
    if hydro < 0:
        hydro = 0
       
    print(f'Hydro roll : {roll} - 7 + {planet_size} + {mod}')
    planet.append(hydro)
   
##### world pop
def gen_world_pop():
    #gen by 2d6-2 modified by world size
    roll = roll_2_D_6()
    planet_size = planet[1]
    atmo = planet[2]
    hydro = planet[3]
    mod = 0
    world_pop = roll - 2 + mod
    if planet_size <= 2:
        mod -= 1
    if atmo >= 10:
        mod -= 2
    if atmo == 6:
        mod += 3
    elif atmo == 5 or atmo == 8:
        mod += 1
    if hydro == 0 and atmo <= 3:
        mod -= 2
    print(f'World Pop roll: {roll} - 2 + {mod} = {world_pop}')
    planet.append(world_pop)


##### primay starport
def gen_starport():
    #gen 2d6-7 + world pop
    roll = roll_2_D_6()
    world_pop = planet[4]
    starport = roll - 7 + world_pop
   
    if starport < 0:
        starport = 0
    print(f'Starport roll: {roll} - 7 + {world_pop} = {starport}')
    planet[0] = starport


##### world government
def gen_world_government():
    # gen 2d6-7 + world pop
    roll = roll_2_D_6()
    world_pop = planet[4]
    world_gov = roll - 7 + world_pop
   
    if world_gov < 0:
        world_gov = 0
    print(f'World Government roll: {roll} - 7 + {world_pop} = {world_gov}')
    planet.append(world_gov)
   
   
##### law level


def gen_law_level():
    #gen 2d6-7+ world_gov
    roll = roll_2_D_6()
    world_gov = planet[5]
    law_level = roll - 7 + world_gov
   
    if law_level < 0:
        law_level = 0
    print(f'Law level roll: {roll} - 7 + {world_gov} = {law_level}')
    planet.append(law_level)
   
##### Tech Level
def gen_tech_level():
    roll = roll_1_D_6()
    mod = 0
    starport = planet[0]
    size = planet[1]
    atmo = planet[2]
    hydro = planet[3]
    pop = planet[4]
    world_gov = planet[5]
    tech_level = roll + mod
    ## star port mod
    if starport == 10:
        mod += 6
    elif starport == 11:
        mod += 4
    elif starport == 12:
        mod += 2
    ## world size mod
    if size <= 1:
        mod += 2
    elif size == 2 or size == 3:
        mod += 1
    ### atmo mod
    if atmo <= 3:
        mod += 1
    elif atmo >= 10:
        mod += 1
    ### hydro mod
    if hydro == 0 or hydro == 9:
        mod += 1
    elif hydro == 10:
        mod += 2
    ### pop mod
    if pop >=1 and pop <=5 or pop == 9:
        mod += 1
    elif pop == 10:
        mod += 2
    elif pop == 11:
        mod += 3
    elif pop == 12:
        mod += 4  
    ### gov mod
    if world_gov == 0 or world_gov == 5:
        mod += 1
    elif world_gov ==7:
        mod += 2
    elif world_gov == 13 or world_gov == 14:
        mod -=2
    ### end of mod
   
    if tech_level <=4 and (hydro == 0 or hydro == 10,) and pop >=6:
        tech_level = 4
    if tech_level <=5 and (atmo == 4 or atmo == 7 or atmo ==9):
        tech_level = 5
    if tech_level <= 7 and (atmo <= 3 or atmo == 10 or atmo == 12):
        tech_level = 7
    if tech_level <= 7 and (atmo == 13 or atmo == 14) and hydro == 10:
        tech_level = 7
   
   
    print(f'Tech level roll: {roll} + {mod} = {tech_level}')
    planet.append(tech_level)
   
##### group all gen functions into one function
def gen_planet():
    global planet 
    planet = [0]
    gen_world_size()
    gen_atmosphere()
    gen_hydrographics()
    gen_world_pop()
    gen_starport()
    gen_world_government()
    gen_law_level()
    gen_tech_level()
    return planet












##### convert values to strings
def convert_to_psudo_hex():
    temp_planet = []
    for index, value in enumerate(planet):
        if index == 0:
            if value > 10:
                temp_planet.append('A')
            elif value >= 9 and value <=10:
                temp_planet.append('B')
            elif value >= 7 and value <=8:
                temp_planet.append('C')
            elif value >= 5 and value <=6:
                temp_planet.append('D')
            elif value >= 3 and value <=4:
                temp_planet.append('E')
            elif value >= 0 and value <=1:
                temp_planet.append('X')
        if value > 9 and index != 0:
            temp_planet.append(chr(value - 10 + ord('A')))
        elif index != 0:
            temp_planet.append(value)
    list_of_planets.append(temp_planet)
    print(f'\nPlanet code {planet}\nTemp Planet code {temp_planet}')
    planet.clear()
    return temp_planet
   

def gen_1_planet():
    gen_planet()
    convert_to_psudo_hex()



def gen_10_planets():
   x = False
   y = True
   for _ in range(1):
    if x == False:
        gen_planet()
        x = True
        y = False
    if y == False:
        print("Converting Code")
        convert_to_psudo_hex()
        x = False
        y = True
      



def get_planet_code():
    if 0<= index < len(list_of_planets):
        p = list_of_planets[index]
        print(f"Planet code: {index} is {p}")
    else:
        print("Invalid Index", len(p)-1)


def show_list_of_planets():
    for planet in list_of_planets:
        if len(planet) == 8:
            print(planet[0],planet[1],planet[2],planet[3],planet[4],planet[5],planet[6],"-",planet[7])


def gen_grid_coordinates():
    for x in range(1,9):
        for y in range (1,11):
            key = str(x)+ str('0')+str(y)
            sub_sector[key]=[]

def gen_sub_sector():
    # currently does not gen any planets or will gen to many planets
    for coordinate in sub_sector:
        planet_exist = 3
        roll = roll_1_D_6()
        print(roll)
        if roll > planet_exist:
            gen_1_planet()
            sub_sector[coordinate] = list_of_planets
            list_of_planets.clear
        else:
            print('No planet')

gen_grid_coordinates()
gen_sub_sector()
print(sub_sector)
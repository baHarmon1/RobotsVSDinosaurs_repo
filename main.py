from battlefield import Battlefield
battlefield = Battlefield()
battlefield.display_welcome()
battlefield.run_game()
battlefield.battle()
game_over = False
robot_winner = False
dinosaur_winner = False

while game_over == False:
    battlefield.robo_turn(battlefield.fleet.robots_list[0])
    if len(battlefield.herd.dinosaurs_list) <= 0:
        game_over = True
        robot_winner = True
        continue
    battlefield.dino_turn(battlefield.herd.dinosaurs_list[0])
    if len(battlefield.fleet.robots_list) <= 0:
        game_over = True
        dinosaur_winner = True
        continue

if robot_winner == True:
    print("Congratulations! Robots are victorious! 01010110 01101001 01100011 01110100 01101111 01110010 01111001 ")
elif dinosaur_winner == True:
    print("Retreat! The dinos are too strong!")

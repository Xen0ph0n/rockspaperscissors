#!/usr/bin/python
# Rocks, Paper, Scissors ! 
# Written and Designed by CJ Clark & Chris Clark
# No Licence or warranty expressed or implied, use however you wish!

import sys, random, argparse, time


def findweapon(weapon):

  if weapon == "s" or weapon == "scissors":
    print "\n[+] You Picked Scissors! ... sneaky!\n"
    return "Scissors"

  if weapon == "r" or weapon == "rock":
    print "\n[+] You Picked Rock! .. Hulk Smash!!\n"
    return "Rock"

  if weapon == "p" or weapon == "paper":
    print "\n[+] You Picked Paper! .. eeww gross!\n"
    return "Paper"

  else: 
    print "\n[-] Woah " + weapon + " is cheating!"
    print "[-] You need to pick: [R]ocks, [P]aper, or [S]cissor\n" 
    sys.exit(1) 

def computerweapon():

  weapons = ['Rock','Paper','Scissors']
  return random.choice(weapons)


def battle(p_weapon, c_weapon):

  if p_weapon == "Rock":
    if c_weapon == "Rock":
      winner = "Tie"
    if c_weapon == "Paper":
      winner = "Computer"
    if c_weapon == "Scissors":
      winner = "Player"

  if p_weapon == "Paper":
    if c_weapon == "Rock":
      winner = "Player"
    if c_weapon == "Paper":
      winner = "Tie"
    if c_weapon == "Scissors":
      winner = "Computer"

  if p_weapon == "Scissors":
    if c_weapon == "Rock":
      winner = "Computer"
    if c_weapon == "Paper":
      winner = "Player"
    if c_weapon == "Scissors":
      winner = "Tie"

  return winner


def main():

  weapon = raw_input("[+] Chose your Weapon Warrior!! [R]ocks, [P]aper, or [S]cissors \n[+] Pick now: ").lower()

#  opt=argparse.ArgumentParser(description="RPS! Try to beat the computer at Rocks Paper Scissors!")
#  opt.add_argument("RPS", help="Pick your weapon! [R]ocks, [P]aper, or [S]cissors")
#  options= opt.parse_args()
#  weapon = options.RPS.lower()
  
  player_weapon = findweapon(weapon)
  computer_weapon = computerweapon()

  time.sleep(2)

  print "[+] PREPARE FOR BATTLE!!!!\n"

  time.sleep(2)

  print "\n[+] The Terminator has chosen " + computer_weapon +"!"

  winner = battle(player_weapon, computer_weapon)

  time.sleep(2)

  if winner == "Tie":
    print "\n[+] You've TIED!! Weak! Play again!\n"

  else:
    print "\n[+] All Hail!! The great " + winner + " is Victorious!!!\n"

if __name__ == '__main__':
    main()

import argparse


def main():
    pars = argparse.ArgumentParser()
    pars.add_argument("--name", help="Write your name", type=str)
    pars.add_argument("--gender", help="Choose your gender: male, female", type=str,
                      choices=["male", "female"])
    pars.add_argument("height", help="Write your height (cm)", type=float)
    pars.add_argument("weight", help="Write your weight (kg)", type=float)
    pars.add_argument("sleep", help="How much do you usually sleep?", type=int)
    pars.add_argument("food", help="How many meals does your daily diet include?", type=int)
    pars.add_argument("health_food", help="""How many fresh fruits and vegetables do you eat during the day?
                      1 - I do not eat these products regularly;
                      2 - Less than 500 grams;
                      3 - More than 500 grams""",
                      type=int)
    pars.add_argument("steps", help="""How many steps do you walk on average per day?
                      1 - Less than 5 thousand steps;
                      2 - 5-10 thousand steps;
                      3 - More than 10 thousand steps""", type=int)
    pars.add_argument("health",
                      help="""Do you monitor your health? 
                      1 - No; 
                      2 - Yes, I have been undergoing medical examination in the last 3 years; 
                      3 - Yes, but I do not see a doctor""",
                      type=int)
    pars.add_argument("mood", help="What is your mood today? Good, Neutral or Bad?", type=str,
                      choices=["Good", "Neutral", "Bad"])
    pars.add_argument("happiness",
                      help="""When was the last time you had a state of happiness? 
                      1 - During the week, 
                      2 - During the month, 
                      3 - During the year""",
                      type=int)
    args = pars.parse_args()
    health_index = 0
    body_mass_index = args.weight / (args.height ** 2)
    if 25 > body_mass_index >= 18.5:
        health_index += 1
    if 8 >= args.sleep >= 7:
        health_index += 1
    if 5 >= args.food >= 4:
        health_index += 1
    if args.health_food == 3:
        health_index += 1
    if args.steps == 3:
        health_index += 1
    if args.health == 2:
        health_index += 1
    if args.mood == "Good":
        health_index += 1
    if args.happiness == 1 or args.happiness == 2:
        health_index += 1

    if health_index == 8:
        print("Your index of a healthy lifestyle is 8/8, which means that you are a true "
              "leader in a healthy lifestyle!")
    if 7 >= health_index >= 5:
        print("Your health index is [5-7]/8, which means that you are on the right track!")
    if 4 >= health_index >= 0:
        print("Your healthy lifestyle index is [0-4]/8, you need to rethink your healthy lifestyle!")


if __name__ == '__main__':
    main()

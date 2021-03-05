import math

class APP():
    def __init__(self):
        ## first to ask user to input all required data :
        self.age1=100

    def Body_mass_index(self):
## BMI calculation :
        print('\n===============================================\n')
        str1 = input(' How tall are you? Enter feet and inch separated by a space: ')
        list1 = str1.split()
        height = int(list1[0]) * 12 + int(list1[1])
        weight = float(input(' Enter your weight(lbs): '))
        v1=weight*0.45
        v2=height*0.025
        v22=v2*v2
        BMI=v1/v22
        print('BMI=',BMI)

        if BMI <= 18.5 :
            cat= "Underweight"
        else:
            if BMI < 24.9 and BMI > 18.5 :
                cat = 'Normal weight'
            else :
                if BMI >= 30 :cat="Obese"
                else: cat='Overweight'

        return BMI, cat

#####
    def Retirement(self):
        print('\n===============================================\n')
        age = float(input(' Enter your current age: '))
        salary = float(input('Enter your yearly-salary in dollars: '))
        print('Note : Now please enter the savings percentage ')
        print(' For example:  20. means you want to save 20% of your salary ')
        v1 = float(input('Enter your planned savings percentage now :'))
        save_pc = v1 / 100.
        employer_match=0.35*save_pc  ## this is unclear ???
        print(' Tell us about your retirement plan! ')
        print(' Note that we assume you will live to 100 years old,')
        print(' So think about your retirement goal (dollar amount) for a while!')
        ret_age=int(input('Please enter your desired retirement age: '))
        goal = input(' Please enter retirement-saving goal (dollar amount): ')
        goal=float(goal)
        years=ret_age-age
        total=years*(employer_match+save_pc)*salary
        print('\n You will have saved :',total, 'dollars at the planned retiring age!')
        if total >= goal :
            met_or_not=True
        else:
            met_or_not=False
        return met_or_not

#######################################################
#### main program

print('\n====================================================')
print('This App can do some calculations for you!')
print(' Please select from the following two options: ')
print(' (1) Compute your Body-mass-index for you ')
print(' (2) Check your retirement plan')
print('====================================================\n')

choice=input(' Please enter your selection: enter 1 or 2 \n')



app1=APP()

if choice == '1' :
    BMI_v, cat = app1.Body_mass_index()
    print(BMI_v, cat)
else:
    ans=app1.Retirement()
    if ans==True :
        print(" Congrulation ! You will meet your goal !")
    else:
        print('Sorry, You won\'t meet your goal')
        print(' you need to save more or increase your salary ')

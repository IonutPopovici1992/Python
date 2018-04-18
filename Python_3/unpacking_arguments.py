def health_calculator(age, apples_ate, cigs_smoked):
    answer = (100 - age) + (apples_ate * 3.5) - (cigs_smoked * 2)
    print(answer)

johnnys_data = [25, 20, 0]

health_calculator(johnnys_data[0], johnnys_data[1], johnnys_data[2])
health_calculator(*johnnys_data)

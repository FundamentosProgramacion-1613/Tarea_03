#encoding: UTF-8
#Autor: Diego Perez AKA DiegoCodes
#Calculador del Pago de Un Trabajador

#Calcula el producto de salario por hora, normal y extra, y las suma
def salaryMath(hours,ex_hours,wage):
    normSalary = hours*wage
    extraSalary = ex_hours*(wage*1.5)
    totalSalary = normSalary+extraSalary
    return normSalary,extraSalary,totalSalary
    
def main():
    hours = int(input("Horas normales trabajadas:"))
    ex_hours = int(input("Horas extras trabajadas:"))
    wage = int(input("Pago por hora normal"))
    (normSalary,extraSalary,totalSalary) = salaryMath(hours,ex_hours,wage)
    print("Horas Normales:",hours)
    print("Horas Extras:",ex_hours)
    print("Pago por hora:",wage)
    print("pago semanal normal: $",normSalary)
    print("pago semanal extra: $",extraSalary)
    print("pago semanal total: $", totalSalary)

main()
def calculo_inss(salariobruto):
    if salariobruto <= 1000:
        return 0.0
    if salariobruto <= 2000:
        return salario * 0.1
    else:
        return salariobruto * 0.2

def calculo_ir(salarioliquido):
    if salarioliquido <= 1400.0:
        return 0.0
    elif salarioliquido <= 2500.0:
        return salarioliquido*0.12
    elif salarioliquido <= 5000.0:
        return salarioliquido*0.2
    else:
        return salarioliquido*0.25

def calculasalariobase(salario,dependente):
    desc_inss=calculo_inss(salario)
    salario_ir = salario-desc_inss-100*dependente
    desc_ir = calculo_ir(salario_ir)
    return salario-desc_inss-desc_ir


salariobruto = input(" Entre com seu salario bruto = ")
dependente = input("Entre com o numero de depende = ")

print ("Salario base = ", calculasalariobase(salariobruto,dependente))

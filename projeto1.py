def calculo_inss(salariobruto)/;
    if salariobruto <= 1000:
        return 0.0
    if salariobruto <= 2000:
        return salario * 0.1
    else:
        return salariobruto * 0.2

def leap_year():
    year = int(input("Ingrese un año: "))

    divisible_por_400 = (year % 400 == 0)
    divisible_por_100 = (year % 100 == 0)
    divisible_por_4 = (year % 4 == 0)

    es_bisiesto = divisible_por_400 or (divisible_por_4 and not divisible_por_100)

    if es_bisiesto:
        print(f"El año {year} es bisiesto")
    else:
        print(f"El año {year} no es bisiesto")


if __name__ == "__main__":
    leap_year()

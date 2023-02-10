from functools import reduce
import os
from statistics import mean, median, mode

def relative_frequency_calculator(absolute_frequencies, summation_total):
    relative_frequencies = []
    for i in range(len(absolute_frequencies)):
        relative_frequency = absolute_frequencies[i] / summation_total
        relative_frequency = round(relative_frequency, 2)
        relative_frequencies.append(relative_frequency)
    return relative_frequencies

def percentage_and_degrees_calculator(relative_frequencies, which):
    if which == 1:
        percentages = []
        for i in range(len(relative_frequencies)):
            percentages.append(relative_frequencies[i] * 100)
        return percentages
    if which == 2:
        degrees = []
        for i in range(len(relative_frequencies)):
            degrees.append(round(360 * relative_frequencies[i], 2))
        return degrees

    
def mean_median_mode_calculator(data, which):
    if which == 1:
        return mean(data)
    if which == 2:
        return median(data)
    if which == 3:
        return mode(data)


def range_variance_calculator(classes, mode, absolute_frequencies, summation, which):
    if which == 1:
        for i in absolute_frequencies:
            if i == 1:
                Range = mode - absolute_frequencies[len(absolute_frequencies) - 1]
                return Range
            else:
                Range = classes[0] - classes[len(absolute_frequencies) - 1]
                return Range
    else:
        summation_squared = summation ** 2
        another_summation_squared = 0
        for i in absolute_frequencies:
            another_summation_squared = another_summation_squared + i ** 2
        halfway_variance = summation_squared / summation
        almost_variance = another_summation_squared - halfway_variance
        variance = almost_variance / (summation - 1)
        if which == 2:
            return variance


def run():
    os.system("cls")
    print("""
                          _             _             _                        _       
     /\                  | |           | |           | |                      | |      
    /  \  _   _ _   _  __| | __ _ _ __ | |_ ___    __| | ___   _ __ ___   __ _| |_ ___ 
   / /\ \| | | | | | |/ _` |/ _` | '_ \| __/ _ \  / _` |/ _ \ | '_ ` _ \ / _` | __/ _ \
  / ____ \ |_| | |_| | (_| | (_| | | | | ||  __/ | (_| |  __/ | | | | | | (_| | ||  __/
 /_/    \_\__, |\__,_|\__,_|\__,_|_| |_|\__\___|  \__,_|\___| |_| |_| |_|\__,_|\__\___|
           __/ |                                                                       
          |___/                                                                                                                                                                                                
    """)
    input("Bienvenido al creador de tablas, presiona enter para continuar")
    amount_of_classes = input("Ingresa la cantidad de clases que tienes: ")
    classes = []
    classes_in_order = []
    data = []
    class_absolute_frequencies_dictionary = {}
    relative_frequencies = []
    acumulative_frequencies = []
    absolute_frequencies_men = []
    absolute_frequencies_women = []
    old_absolute_frequencies_total = []
    absolute_frequencies_total = []
    for i in range(int(amount_of_classes)):
        a_class = input("Ingresa la clase número " + str(i + 1) + ": ")
        classes.append(int(a_class))
        absolute_frequency_women = input("Ingresa la frecuencia absoluta de la clase " + str(i + 1) + " en mujeres: ")
        absolute_frequency_men = input("Ingresa la frecuencia absoluta de la clase " + str(i + 1) + " en hombres: ")
        absolute_frequencies_men.append(int(absolute_frequency_men))
        absolute_frequencies_women.append(int(absolute_frequency_women))
    for i in range(len(absolute_frequencies_men)):
        absolute_frequencies_total.append(absolute_frequencies_men[i] + absolute_frequencies_women[i])
    summation_men = reduce(lambda a, b: a + b, absolute_frequencies_men)
    summation_women = reduce(lambda a, b: a + b, absolute_frequencies_women)
    acumulative_frequency = 0
    for i in absolute_frequencies_total:
        acumulative_frequency += i
        acumulative_frequencies.append(acumulative_frequency)
    for i in range(len(classes)):
        class_absolute_frequencies_dictionary.update({absolute_frequencies_total[i]: classes[i]})
    for i in absolute_frequencies_total:
        old_absolute_frequencies_total.append(i)
    absolute_frequencies_total.sort(reverse=True)
    absolute_frequencies_women.sort(reverse=True)
    absolute_frequencies_men.sort(reverse=True)
    for i in range(len(classes)):
        which_class = class_absolute_frequencies_dictionary.get(absolute_frequencies_total[i])
        classes_in_order.append(which_class)
    for i in range(len(classes)):
        for y in range(absolute_frequencies_total[i]):
            data.append(classes_in_order[i])
    summation_total = summation_women + summation_men
    relative_frequencies_women = relative_frequency_calculator(absolute_frequencies_women, summation_total)
    relative_frequencies_men = relative_frequency_calculator(absolute_frequencies_men, summation_total)
    for i in range(len(relative_frequencies_men)):
        relative_frequencies.append(relative_frequencies_women[i] + relative_frequencies_men[i])
    percentages_women = percentage_and_degrees_calculator(relative_frequencies_women, 1)
    percentages_men = percentage_and_degrees_calculator(relative_frequencies_men, 1)
    degrees_women = percentage_and_degrees_calculator(relative_frequencies_women, 2)
    degrees_men = percentage_and_degrees_calculator(relative_frequencies_men, 2)
    percentages_total = percentages_men + percentages_women
    degrees_total = degrees_men + degrees_women
    mean = mean_median_mode_calculator(data, 1)
    median = mean_median_mode_calculator(data, 2)
    mode = mean_median_mode_calculator(data, 3)
    Range = range_variance_calculator(classes_in_order, mode, absolute_frequencies_total, summation_total, 1)
    Variance = range_variance_calculator(classes_in_order, mode, absolute_frequencies_total, summation_total, 2)
    sd = Variance ** 0.5
    sd = round(sd, 2)
    os.system("cls")
    for i in range(len(classes_in_order)):
        print("")
        print("Clase " + str(classes_in_order[i]) + ":")
        print("Frecuencia absoluta total: " + str(absolute_frequencies_total[i]))
        print("Frecuencia absoluta de mujeres: " + str(absolute_frequencies_women[i]))
        print("Frecuencia absoluta de hombres: " + str(absolute_frequencies_men[i]))
        print("")
        print("Frecuencia relativa: " + str(relative_frequencies[i]))
        print("Frecuencia acumulada: " + str(acumulative_frequencies[i]))
        print("")
        print("Porcentajes totales: " + str(percentages_total[i]))
        print("Porcentajes de mujeres: " + str(percentages_women[i]))
        print("Porcentajes de hombres: " + str(percentages_men[i]))
        print("")
        print("Grados: " + str(degrees_total[i]))
        print("Grados en mujeres: " + str(degrees_women[i]))
        print("Grados en hombres: " + str(degrees_men[i]))
        print("")
    print("Media: " + str(mean))
    print("Mediana: " + str(median))
    print("Moda: " + str(mode))
    print("Rango: " + str(Range))
    print("Varianza: " + str(Variance))
    print("Desviación estándar: " + str(sd))


if __name__ == "__main__":
    run()
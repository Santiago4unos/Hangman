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
            degrees.append(360 * relative_frequencies)
        return degrees

    
def mean_median_mode_calculator(data, which):
    if which == 1:
        return mean(data)
    if which == 2:
        return median(data)
    if which == 3:
        return mode(data)


def range_variance_sd_calculator(data, mode, absolute_frequencies, acumulative_frequencies, summation, which):
    if which == 1:
        for i in absolute_frequencies:
            if i == 1:
                Range = mode - absolute_frequencies[len(absolute_frequencies) - 1]
                return Range
            else:
                Range = absolute_frequencies[len(absolute_frequencies) - 1] - absolute_frequencies[0]
                return Range
    else:
        summation_squared = summation ** 2
        another_summation_squared = 0
        for i in absolute_frequencies:
            another_summation_squared = another_summation_squared ** 2 + i
        halfway_variance = another_summation_squared / acumulative_frequencies[len(acumulative_frequencies) - 1]
        almost_variance = summation_squared - halfway_variance
        variance = almost_variance / (acumulative_frequencies[len(acumulative_frequencies) - 1] - 1)
        if which == 2:
            return variance
        if which == 3:
            sd = variance ** 0.5
            return sd


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
    input("Bienvenido al creador de tablas, presiona cualquier tecla para continuar")
    amount_of_classes = input("Ingresa la cantidad de clases que tienes: ")
    classes = []
    data = []
    acumulative_frequencies = []
    absolute_frequencies_men = []
    absolute_frequencies_women = []
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
    absolute_frequencies_total.sort(reverse=True)
    summation_men = reduce(lambda a, b: a + b, absolute_frequencies_men)
    summation_women = reduce(lambda a, b: a + b, absolute_frequencies_women)
    for i in range(len(absolute_frequencies_men)):
        for y in range(len(absolute_frequencies_men)):
            if i != y:
                acumulative_frequencies.append(absolute_frequencies_men[i])
            else:
                break
    for i in range(len(classes)):
        for y in range(absolute_frequencies_total[i]):
            data.append(classes[i])
    summation_total = summation_women + summation_men
    relative_frequencies_women = relative_frequency_calculator(absolute_frequencies_total, summation_total)
    relative_frequencies_men = relative_frequency_calculator(absolute_frequencies_total, summation_total)
    percentages_women = percentage_and_degrees_calculator(relative_frequencies_women, 1)
    percentages_men = percentage_and_degrees_calculator(relative_frequencies_men, 1)
    degrees_women = percentage_and_degrees_calculator(relative_frequencies_women, 2)
    degrees_men = percentage_and_degrees_calculator(relative_frequencies_men, 2)
    percentages_total = percentages_men + percentages_women
    degrees_total = degrees_men + degrees_women
    mean = mean_median_mode_calculator(data, 1)
    median = mean_median_mode_calculator(data, 2)
    mode = mean_median_mode_calculator(data, 3)
    Range = range_variance_sd_calculator(data, mode, absolute_frequencies_total, acumulative_frequencies, summation_total, 1)
    Variance = range_variance_sd_calculator(data, mode, absolute_frequencies_total, acumulative_frequencies, summation_total, 2)
    sd = range_variance_sd_calculator(data, mode, absolute_frequencies_total,acumulative_frequencies, summation_total, 3)
    for i in classes:
        print("Clase" + (i+1) + ":")
        print()


if __name__ == "__main__":
    run()
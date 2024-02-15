#Рассмотрим пример, где мы используем цикл while для проверки значений пациентов на наличие аномалий:

patient_data = [38.2, 36.9, 37.5, 36.8, 39.1]
abnormal_temperatures = []

index = 0
while index < len(patient_data):
    temperature = patient_data[index]
    if temperature > 38:
        abnormal_temperatures.append(temperature)
    index += 1

print("Пациенты с аномальной температурой:", abnormal_temperatures)
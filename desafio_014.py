#Código que converte a temperatura de °C para °F e K
c = float(input('Informe a temperatura em °C: '))
print('{}°C é correspondente a {:.1f}°F'.format(c, c * 9 / 5 + 32))
print('{}°C é correspondente a {:.2f}K'.format(c, c + 273.15))

#fahrenheit = °C * 9 / 5 + 32
#kelvin = °C + 273.15

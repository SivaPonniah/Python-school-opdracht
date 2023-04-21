### PYTHON TOETS SIVA PONNIAH
########## wanneer de vraag :Wat is de prijs inclusief BTW? moet u het bedrag van de laptop invoeren #############
########## Wanner de keuze wordt gevraagd voor welke laptop kopieer de de naam van de laptop en plak dat is gemakkelijker####
# Importeer de datetime module om de huidige datum te verkrijgen
import datetime

# Definieer de lijst van laptops
laptop_list = {
    "Macbook Air": 999,
    "Macbook Pro": 1299,
    "Dell XPS": 1099,
    "HP Spectre": 1199,
    "Lenovo Yoga": 899,
    "Asus Zenbook": 999,
    "Acer Swift": 699,
    "Microsoft Surface": 1099,
    "Razer Blade": 1499,
    "LG Gram": 999
}

# Definieer de functie om de BTW te berekenen
def calculate_vat(price):
    vat_rate = 0.21
    vat = price * vat_rate
    return round(vat, 2)

# Definieer variabelen voor de factuur
total_price = 0
selected_laptops = []

# Toon de lijst van laptops aan de gebruiker
print("Welkom bij onze laptopwinkel! Hieronder vindt u onze lijst met laptops:")
for laptop in laptop_list:
    print(f"- {laptop} ({laptop_list[laptop]} euro)")

# Vraag de gebruiker om een laptop te kiezen
while True:
    selected_laptop = input("Welke laptop zou u graag willen kopen? ")
    if selected_laptop in laptop_list:
        # Vraag de gebruiker om de prijs van de laptop
        price = float(input(f"De prijs van de {selected_laptop} is {laptop_list[selected_laptop]} euro (exclusief BTW).\nWat is de prijs inclusief BTW? "))

        # Bereken de BTW en voeg deze toe aan het totaalbedrag
        vat = calculate_vat(price)
        total_price += price + vat

        # Voeg de geselecteerde laptop toe aan de lijst
        selected_laptops.append((selected_laptop, price, vat))

        # Vraag de gebruiker of hij of zij nog een laptop wilt kiezen
        continue_shopping = input("Wilt u doorgaan met het winkelen voor laptops? (ja/nee) ")
        if continue_shopping.lower() == "nee":
            break
    else:
        print("Deze laptop staat niet op onze lijst. Probeer het opnieuw.")

# Toon de factuur aan de gebruiker
print("Factuur:")
for laptop in selected_laptops:
    print(f"- {laptop[0]} ({laptop[1]} euro, inclusief {laptop[2]} euro BTW)")
print(f"Totaalbedrag (inclusief BTW): {round(total_price, 2)} euro")

# Vraag de gebruiker om zijn of haar naam en sla de factuur op als een textbestand
name = input("Wat is uw naam? ")
date = datetime.date.today().strftime("%d-%m-%Y")
filename = f"{name}_{date}.txt"
with open(filename, "w") as file:
    file.write("Factuur:\n")
    for laptop in selected_laptops:
        file.write(f"- {laptop[0]} ({laptop[1]} euro, inclusief {laptop[2]} euro BTW)\n")
    file.write(f"Totaalbedrag (inclusief BTW): {round(total_price, 2)} euro\n")
print("Bedankt voor het gebruik van onze applicatie!")

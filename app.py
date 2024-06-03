import json

def max_price(dimond_data):
    max_price_object = max(dimond_data, key=lambda obj: obj["price"])
    return max_price_object

def sum_price(dimond_data):
     total_price = sum(obj["price"] for obj in dimond_data)
     average_price = float (total_price)/ len(dimond_data)
     return average_price

def is_Ideal(dimond_data, key, value):
    count = 0
    for obj in dimond_data:
        if obj.get(key) == value:
            count += 1
    return count

def count_colors(dimond_data, key,value):
    unique_colour = set()
    colour_values = set()
    for obj in dimond_data:
        if key in obj:
            colour_values.add(obj[value])
            unique_colour.add(obj[key])
    return len(unique_colour),colour_values

def average_carat_by_cut(dimond_data):
    carats_by_cut = {}
    count_by_cut = {}
    for obj in dimond_data:
        cut_type = obj.get("cut")
        carat = obj.get("carat", 0)
        if cut_type:
            if cut_type not in carats_by_cut:
                carats_by_cut[cut_type] = carat
                count_by_cut[cut_type] = 1
            else:
                carats_by_cut[cut_type] += carat
                count_by_cut[cut_type] += 1
    average_carats_by_cut = {cut_type: carats_by_cut[cut_type] / count_by_cut[cut_type] for cut_type in carats_by_cut}
    return average_carats_by_cut

def average_price_by_color(dimond_data):
    price_by_color ={}
    count_by_color = {}
    for obj in dimond_data:
        color_av = obj.get("color")
        price_av = obj.get("price", 0)
        if color_av:
           if color_av not in price_by_color:
             price_by_color[color_av] = price_av
             count_by_color[color_av] =1
           else:
            price_by_color[color_av] += price_av
            count_by_color[color_av] +=1 
    average_price_by_colors = {color_av:price_by_color[color_av]/ count_by_color[color_av] for color_av in price_by_color}
    return average_price_by_colors

def median_carats_premium(dimond_data):
    premium_carats = [obj.get("carat", 0) for obj in dimond_data if obj.get("cut") == "Premium"]
    sorted_carats = sorted(premium_carats)
    n = len(sorted_carats)
    if n % 2 == 0:
        median = (sorted_carats[n // 2 - 1] + sorted_carats[n // 2]) / 2
    else:
        median = sorted_carats[n // 2]
    return median


json_file = "dimonddata.json"

with open(json_file, "r") as file:
    dimond_data = json.load(file)



average_price = sum_price(dimond_data)
max_price_object = max_price(dimond_data)


if __name__ =='__main__':
 if max_price_object:
    print("The price of the most expensive item is:", max_price_object["price"])
 if average_price:
    print("The average price of all dimonds is:",float (average_price))
# the key and value i need to check for 3.3 
key_of_type = "cut"
value_of_type = "Ideal"
count_ideal = is_Ideal(dimond_data, key_of_type, value_of_type)
print(f"The number of items with the value '{value_of_type}' is: {count_ideal}")
# the key i need to check for 3.4 
key_of_colour = "color"

unique_colour_count, colour_values = count_colors(dimond_data, key_of_colour, "color")
print(f"The number of colors the diamonds come in '{key_of_colour}' is: {unique_colour_count} And the colors are: {colour_values}")

median_carat_premium = median_carats_premium(dimond_data)
print("The median carats of Premium cut diamonds is:", median_carat_premium)

average_carats_by_cut = average_carat_by_cut(dimond_data)
for cut_type, average_carat in average_carats_by_cut.items():
    print(f"Average carats for '{cut_type}' cut diamonds: {average_carat}")

average_price_by_colors = average_price_by_color(dimond_data)
for color_av, average_price in average_price_by_colors.items():
    print(f"Average price for diamonds with '{color_av}' color: {average_price}")

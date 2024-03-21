# 6.4 嵌套
# 将字典存储在列表中或将列表存储在字典中称为嵌套

# 6.4.1 字典列表
# 在列表中存储字典
alien_0 = {"color": "green", "point": 5}
alien_1 = {"color": "yellow", "point": 10}
alien_2 = {"color": "red", "point": 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# 生成30个外星人
aliens = []
for alien_number in range(30):
    new_alien = {"color": "green", "point": 5, "speed": "slow"}
    aliens.append(new_alien)
for alien in aliens[:5]:
    print(alien)
print("...")
print("Total number of aliens: " + str(len(aliens)))

# 修改前三个外星人的属性
for alien in aliens[0:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = 10
for alien in aliens[:5]:
    print(alien)
print("...")

# 修改前5个外星人的属性
for alien in aliens[0:5]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["point"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["point"] = 15
for alien in aliens[:8]:
    print(alien)
print("...")

# 6.4.2 在字典中存储列表
pizza = {"crust": "thick", "toppings": ["mushrooms", "extra pizza"]}
print(
    "You ordered a " + pizza["crust"] + "-crust pizza " + "with the following toppings:"
)
for topping in pizza["toppings"]:
    print("\t" + topping)

favorite_languages = {
    "jen": ["python", "ruby"],
    "sarah": ["c"],
    "edward": ["ruby", "go"],
    "phil": ["python", "haskell"],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())

# 6.4.3 在字典中存储字典
users = {
    "aeinstein": {
        "first": "albert",
        "last": "einstein",
        "location": "princeton",
    },
    "mcurie": {
        "first": "marie",
        "last": "curie",
        "location": "paris",
    },
}
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info["first"] + " " + user_info["last"]
    location = user_info["location"]

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

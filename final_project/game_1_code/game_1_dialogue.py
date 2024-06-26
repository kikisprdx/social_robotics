# Define the mapping of animals, their locations, an interesting fact, and a hint
animal_questions = {
    "Giraffe": ("Africa", "Did you know that giraffes have the same number of neck vertebrae as humans, although they have very long necks?", "It's the continent with the famous Serengeti."),
    "Panda": ("Asia", "Pandas spend around 14 hours a day eating bamboo.", "It's the largest continent in the world."),
    "Kangaroo": ("Australia", "Kangaroos can leap over 30 feet in a single bound.", "It's known as the 'Land Down Under'."),
    "Penguin": ("Antarctica", "Penguins can drink seawater because they have a special gland that filters out the salt.", "It's the coldest continent."),
    "Elephant": ("Africa", "Elephants are the largest land animals and can weigh up to 14,000 pounds.", "It's home to the Sahara Desert."),
    "Tiger": ("Asia", "Tigers are excellent swimmers and can swim for several kilometers.", "It's the continent with the Great Wall."),
    "Koala": ("Australia", "Koalas sleep up to 18 hours a day to conserve energy.", "It's the smallest continent."),
    "Polar Bear": ("Arctic", "Polar bears have black skin under their white fur to absorb heat from the sun.", "It's the northernmost region.")
}

# Define false statements
false_statements = {
    "Giraffe": ("Giraffes are native to South America.", "Giraffes can only be found in deserts."),
    "Panda": ("Pandas are native to Africa.", "Pandas eat meat."),
    "Kangaroo": ("Kangaroos are native to North America.", "Kangaroos can swim but can't hop."),
    "Penguin": ("Penguins live in the Arctic.", "Penguins can fly."),
    "Elephant": ("Elephants are native to South America.", "Elephants are the smallest land animals."),
    "Tiger": ("Tigers are native to Europe.", "Tigers are herbivores."),
    "Koala": ("Koalas are native to Antarctica.", "Koalas are active at night."),
    "Polar Bear": ("Polar bears live in Antarctica.", "Polar bears have white skin under their white fur.")
}

# Define the mapping of continent Aruco card IDs to continent names
continent_cards = {
    1: "Australia",
    2: "Asia",
    3: "Africa",
    4: "Arctic",
    5: "Antarctica"
}

true_false_cards = {
    6: True,
    7: False
}

#the correct responses for the continent questions
correct_responses = [
    "Well done! The {animal} indeed lives in {location}.",
    "Great job my friend! You found that the {animal} is from {location}.",
    "Excellent work! The {animal} calls {location} its home.",
    "You're right! How did you know that one? The {animal} lives in {location}.",
    "Good work! The {animal} is indeed found in {location}."
]

# the incorrect responses
incorrect_responses = [
    "That's not the right answer. Try again!",
    "Not quite. Give it another shot! You can do it!",
    "That's incorrect. Please try once more!",
    "Nope, that's not it. Try again!",
    "That's not the right one. But have another go!"
]


correct_responses_true_false = [
    "Well done!",
    "Great job my friend!",
    "Excellent work!",
    "You're right! How did you know that one? You must have been listening very well",
    "Good work! Great that you paid attention!"
]

incorrect_responses_true_false = [
    "That's not the right answer. Try the other card",
    "Not quite. Give it another shot! You should know the answer by now.",
    "That's incorrect. Please try once more!",
    "Nope, that's not it. Try the other card",
    "That's not the right one. But have another go!"
]


from abc import ABC
class FOOD(ABC):
    def recipe(self):
        pass
class biryani(FOOD):
    def recipe(self):
        print("""Ingredients:
For Chicken Marinade:
Chicken pieces
Yogurt, ginger-garlic paste, chili powder, turmeric, and garam masala.
For Rice:
Basmati rice, whole spices (cardamom, cloves, bay leaves, cinnamon).
For Biryani Layering:
Fried onions, mint, coriander, saffron-soaked milk, ghee or butter.
Steps:
Marinate Chicken: Mix the chicken with the marinade ingredients and let it rest for 1–2 hours.
Cook Rice: Boil rice with whole spices until it’s 70% cooked. Drain and set aside.
Cook Chicken: Sauté onions until golden, add the marinated chicken, and cook until tender.
Layer Biryani: In a pot, layer rice and chicken alternately. Top with fried onions, mint, saffron milk, and ghee.
Steam (Dum): Cover tightly and cook on low heat for 20–30 minutes to allow flavors to meld.
Pro Tips:
Serve with raita or a tangy salad for a complete meal.
Customize spices to suit your heat tolerance.""")


class crows(biryani):
    def recipe(self):
        print("""Cooking crow is rare and not part of most culinary traditions. However, historically, it has been consumed in survival situations or as part of novelty recipes. If you're considering cooking crow, ensure the bird is legally hunted and properly prepared to avoid health risks.

Basic Recipe Summary:
Preparation:

Pluck and clean the bird thoroughly.
Remove feathers, organs, and wash the carcass.
Marinade:

Marinade with vinegar or lemon juice to tenderize and neutralize gamey flavors.
Add garlic, herbs, salt, and pepper for seasoning.
Cooking:

Crow can be roasted, stewed, or braised.
If stewing, cook with vegetables, broth, and spices to enhance flavor and tenderness.
Serving:

Serve with sides like mashed potatoes or bread.
For detailed and specific recipes, you can refer to sources like survival cooking guides or historical recipe collections. If you'd like, I can look for additional links to ensure safe and flavorful preparation.""")



class crow_nuggies(crows):
    def recipe(self):
        print("""
Making "crow nuggets" (crow nuggies) is unconventional, and ensuring the meat is safe for consumption is crucial. Proper cleaning, preparation, and cooking techniques are essential when dealing with wild game like crow.

Step-by-Step Guide to Make Crow Nuggets:
1. Ingredients:
Crow breast meat (boneless, cleaned, and tenderized).
Flour or breadcrumbs for coating.
Egg wash (beaten eggs mixed with a little water or milk).
Seasoning (salt, pepper, garlic powder, onion powder, paprika).
Oil for frying.
2. Preparation:
Clean the Meat: Remove feathers, skin, and any inedible parts. Wash the meat thoroughly in cold water.
Tenderize: Soak the meat in a marinade (buttermilk, vinegar, or lemon juice) for a few hours to reduce gaminess and improve texture.
Cut: Slice the meat into nugget-sized pieces.
3. Coating:
Season the flour or breadcrumbs with your preferred spices.
Dip each piece of meat into the egg wash, then coat with the seasoned flour/breadcrumb mixture.
4. Cooking:
Heat oil in a deep skillet or fryer to about 350°F (175°C).
Fry the coated pieces until golden brown and fully cooked (internal temperature of at least 165°F or 74°C).
Place on paper towels to drain excess oil.
5. Serving:
Serve with dipping sauces like barbecue, ranch, or honey mustard.

Safety Tips:
Ensure the crow meat comes from a safe source and has not been exposed to diseases.
Cook thoroughly to kill any potential pathogens.""") 


ob1 = biryani()
ob1.recipe()
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
ob2 = crows()
ob2.recipe()
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
ob3 = crow_nuggies()
ob3.recipe()

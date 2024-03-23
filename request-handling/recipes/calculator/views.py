from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def omlet(request):
    recipe_omlet = DATA.get('omlet')
    serving = int(request.GET.get('serving', 1))
    serving_recipe = {}
    if serving > 1:
        for ingredient, count in recipe_omlet.items():
            count_for_serving = serving * count
            serving_recipe.setdefault(ingredient, count_for_serving)
        return render(request, 'calculator/index.html', context={
            'recipe': serving_recipe
        })
    else:
        return render(request, 'calculator/index.html', context={
        'recipe': recipe_omlet
    })

def pasta(request):
    recipe_pasta = DATA.get('pasta')
    serving = int(request.GET.get('serving', 1))
    serving_recipe = {}
    if serving > 1:
        for ingredient, count in recipe_pasta.items():
            count_for_serving = serving * count
            serving_recipe.setdefault(ingredient, count_for_serving)
        return render(request, 'calculator/index.html', context={
            'recipe': serving_recipe
        })
    else:
        return render(request, 'calculator/index.html', context={
            'recipe': recipe_pasta
        })

def buter(request):
    recipe_buter = DATA.get('buter')
    serving = int(request.GET.get('serving', 1))
    serving_recipe = {}
    if serving > 1:
        for ingredient, count in recipe_buter.items():
            count_for_serving = serving * count
            serving_recipe.setdefault(ingredient, count_for_serving)
        return render(request, 'calculator/index.html', context={
            'recipe': serving_recipe
        })
    else:
        return render(request, 'calculator/index.html', context={
            'recipe': recipe_buter
        })
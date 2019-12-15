from django.shortcuts import render
from .models import Shop, Item, Profile 
from django.http import HttpResponse
import json

# return true if shop is in radius of 2 unit
def is_nearby(shop=None, user_lati=None, user_longi=None): 
    shop_lati,shop_longi = list(map(int, shop.location.split(',')))
    print('shop_lati, shop_longi',shop_lati,shop_longi)
    if((shop_lati-user_lati)**2 + (shop_longi-user_longi)**2 <= 2): return True 
    return False

def profile(request):
    user = request.user
    # profile = Profile.objects.get(user=user)
    if request.method == 'POST' and len(request.POST.get('location'))==3:
        location = request.POST.get('location')
        user_lati,user_longi = list(map(int, location.split(',')))
        print('lati, longi', user_lati, user_longi)
        shops = Shop.objects.all()

        nearby_shops = []
        for shop in shops:
            if is_nearby(shop, user_lati, user_longi):
                nearby_shops.append(shop)
        items_to_purchase = Item.objects.all().filter(profile=user.profile, is_purchased=False)
        print('items to purchase ', items_to_purchase)

        # context = { 'nearby_shops':nearby_shops,
        #            'user':user,
        #            'items_to_purchase':items_to_purchase,
        #           }
        # template_name = 'items/user_profile.htm'
        
        shop_details = {}
        for shop in nearby_shops:
            shop_details[shop.owner_name] = shop.items_available

        print('sending json response', shop_details)

        return HttpResponse(json.dumps(shop_details))
        # return render(request, template_name, context)
    else:
        template_name = 'items/user_profile.htm'
        context = {}
        items_to_purchase = Item.objects.all().filter(profile=user.profile, is_purchased=False)
        print('items to purchase ', items_to_purchase)

        context = {'items_to_purchase':items_to_purchase, 'user':user}
        return render(request, template_name, context)

  
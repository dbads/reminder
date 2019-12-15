from django.contrib import admin


from .models import Profile, Item, Shop

class ProfileModelAdmin(admin.ModelAdmin):
	list_display = ["user",'location']
	# list_display_link = ["user"]
	# list_editables = ["url"]
	# list_filter = ["location","job_title"]
	# search_fields = ["location","user"]
	class Meta:
		model = Profile

class ItemModelAdmin(admin.ModelAdmin):
	list_display = ["profile",'item_name']
	# list_display_link = ["user"]
	# list_editables = ["url"]
	# list_filter = ["location","job_title"]
	# search_fields = ["location","user"]
	class Meta:
		model = Item

class ShopModelAdmin(admin.ModelAdmin):
	list_display = ["owner_name",'location']
	# list_display_link = ["user"]
	# list_editables = ["url"]
	# list_filter = ["location","job_title"]
	# search_fields = ["location","user"]
	class Meta:
		model = Shop

admin.site.register(Profile, ProfileModelAdmin)
admin.site.register(Item, ItemModelAdmin)
admin.site.register(Shop, ShopModelAdmin)

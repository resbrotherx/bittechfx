from django.contrib import admin
from .models import *


admin.site.site_header = "bittechfxhub"
admin.site.site_title = "bittechfxhub"
admin.site.index_title = "bittechfxhub"
# admin.site.register(User_ip)
admin.site.register(Details)
admin.site.register(Userwallet)
admin.site.register(Client_ips)
admin.site.register(Referal)
admin.site.register(Deposit_history)
admin.site.register(Withdraw_request)
admin.site.register(Userinfo)
admin.site.register(PayHistory)
admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(Subscription)
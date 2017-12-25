"""demo1_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from sdt.views import *
app_name='sdt'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^club/', club_list),
    url(r'^club_add/', club_add),
    url(r'^checkclub/', checkclub),
    url(r'^user/',user),
    url(r'^checkuser/',checkuser),
    url(r'^user_list/',user_list),
    url(r'^user_add/',user_add),
    url(r'^old_user_add/',old_user_add),
    url(r'^cash/',cash),
    url(r'^getbalance/',getbalance),
    url(r'^cashin/',cashin),
    url(r'^result/$', result),
    url(r'^result_pretreat_step1/', result_pretreat_step1),
    url(r'^result_newuser/', result_newuser),
    url(r'^result_club/', result_club),
    url(r'^table/', loadtabletype),
    url(r'^getante/', getante),
    url(r'^table_list/', table_list),
    url(r'^game_reg/', game_reg),
    url(r'^result_preview/$', result_preview),
    url(r'^result_view/', result_view),
    url(r'^result_l1/', result_l1),
    url(r'^result_post/', result_post),
    url(r'^result_union/', result_union),
    url(r'^result_unionbyclub/', result_unionbyclub),
    url(r'^useraccountview/', useraccountview),
    url(r'^usercash/', usercash),
    url(r'^login/', login),
    url(r'^default/', default),
    url(r'^report_view/', report_view),
    url(r'^operator/', operator),
    url(r'^add_operator_group/', add_operator_group),
    url(r'^operator_group_list/', operator_group_list),
    url(r'^operator_list/', operator_list),
    url(r'^add_operator/', add_operator),
    url(r'^operator_setup/', operator_setup),
    url(r'^operator_relation/', operator_relation),
    url(r'^operator_relation_setup/', operator_relation_setup),
    url(r'^relation_list/', relation_list),
    url(r'^club_account_info/', club_account_info),
    url(r'^check_balance/', check_balance),
    url(r'^test/', test),
    url(r'^searchUser/', searchUser),
    url(r'^modify_user/', modify_user),
    url(r'^modifyUserInfo/', modifyUserInfo),
    url(r'^user_account_group/', user_account_group),
    url(r'^user_group_search/', user_group_search),
    url(r'^account_migrate/', account_migrate),
    url(r'^club_manage/', club_manage),
    url(r'^club_info/', club_info),
    url(r'^modify_club/', modify_club),
    url(r'^table_reg_mini/', table_reg_mini),
    url(r'^getusefulbalance/', getusefulbalance),
    url(r'^userbuyin/', userbuyin),
    url(r'^freeze_minilist/', freeze_minilist),
    url(r'^abortgame/', abortgame),
    url(r'^union_account/', union_account),
    url(r'^union_account_list/', union_account_list),
    url(r'^club_account_view/', club_account_view),
    url(r'^club_cash/', club_cash),
    url(r'^union_check/', union_check),
    url(r'^result_detail/', result_detail),
    url(r'^group_balance_search/', group_balance_search),
    url(r'^group_balance_list/', group_balance_list),
    url(r'^company_account/', company_account),
    url(r'^getGroupAccount/', getGroupAccount),
    url(r'^company_cash/', company_cash),
    url(r'^company_balance_list/', company_balance_list),
    url(r'^getGameStatus/', getGameStatus),
    url(r'^loadsidebar/', loadsidebar),
    url(r'^correct_manage/', correct_manage),
    url(r'^correct_user_list/', correct_user_list),
    url(r'^correct_user/', correct_user),
    url(r'^correct_club_list/', correct_club_list),
    url(r'^correct_club/', correct_club),
    url(r'^correct_company_list/', correct_company_list),
    url(r'^correct_company/', correct_company),
    url(r'^loadnavigate/', loadnavigate),
    url(r'^company_income_manage/', company_income_manage),
    url(r'^company_income_reg/', company_income_reg),
    url(r'^developer_manage/', developer_manage),
    url(r'^developer_new/', developer_new),
    url(r'^check_developer/', check_developer),
    url(r'^developer_reg/', developer_reg),
    url(r'^developer_list/', developer_list),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

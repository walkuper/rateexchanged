from django.db import models
from datetime import datetime
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core import validators
from django.contrib import admin
from django.template.loader import render_to_string

class BankPack(models.Model):
	"""
	紀錄銀行資訊
	銀行可以有兌換不同貨幣
	但是貨幣可能不被銀行匯兌(因為國際換匯問題)
	"""
	bankname = models.CharField(max_length=100) #日盛銀行
	bankcode = models.CharField(max_length=6, blank=True) # 815
	banknameInfo = models.TextField(blank=True) #日盛銀行成立於xxxx，是一家...
	bankaddress = models.CharField(max_length=400, blank=True) #台北市中正區重慶南路一段10號一樓
	bankphone = models.CharField(max_length=40, blank=True) #電話
	chargefee = models.CharField(max_length=400, blank=True) #各家計算
	webatm = models.URLField() #網址
	update_time = models.DateTimeField(auto_now=True) #更新時間
	created_at = models.DateTimeField(auto_now_add=True) #建立時間

	def goatm(self):
		goatm_path = """<a href="%s" target="_blank">網路ATM</a>""" % self.webatm
		return goatm_path

	def __str__(self):
		return self.title

class ExATM(models.Model):
	"""外幣ATM服務據點"""
	city = models.CharField(max_length=10) #所在城市
	location = models.CharField(max_length=600) #裝設地點
	atmaddr = models.CharField(max_length=400) #裝設地址
	bank = models.ForeignKey(BankPack) #對應的銀行
	update_time = models.DateTimeField(auto_now=True) #更新時間

	def __str__(self):
		return self.atmaddr

class Nation(models.Model):
	nationname = models.CharField(max_length=50) #國家 台灣
	nationInfo = models.TextField(blank=True) #國家基本介紹
	language = models.CharField(max_length=60) #使用語言 繁體中文
	languagecode = models.CharField(max_length=10) #語言代碼 zh-tw
	#maincurrency = models.ForeignKey(CurrencyPack) #主要貨幣

class CurrencyPack(models.Model):
	bankpub = models.ForeignKey(BankPack) #需要先有銀行資訊才不會出錯，否則會有no such column: graparate_currencypack.bankpub_id的錯誤
	currencyname = models.CharField(max_length=50) #貨幣名稱 新台幣
	usecountry = models.ManyToManyField(Nation) #使用國家，一個國家可能會有兩三種貨幣流通
	image = models.ImageField(upload_to = "graparate/static/images", blank=True)
	currencyunit = models.CharField(max_length=20) #單位 里拉、元、披索、銖、法朗
	currencycode = models.CharField(max_length=20) #TWD、USD
	created_at = models.DateTimeField(auto_now_add=True) #建立時間

	#讓CurrencyPackAdmin取得多對多的資料欄位
	def get_usecountry(self):
		return "\n".join([u.nationname for u in self.usecountry.all()])

	def callspotbuy(CurrencyRate):
		csb = spotbuy
		return csb

	def __str__(self):
		return self.currencyname

	def currency_flags(self):
		imagepath = u'<img src="%s" width="100">' % self.image.url
		return imagepath
        #currency_flags.allow_tags = True #替代方案
        #return render_to_string('flags.html',{'image': self}) #替代方案


class CurrencyRate(models.Model):
	spotbuy = models.DecimalField(max_digits=4,decimal_places=3,default=0) #買進，小數點後三位的四位數字
	spotsell = models.DecimalField(max_digits=4,decimal_places=3,default=0) #賣出，小數點後三位的四位數字
	billbuy = models.DecimalField(max_digits=4,decimal_places=3,default=0) #即期買進，小數點後三位的四位數字
	billsell = models.DecimalField(max_digits=4,decimal_places=3,default=0) #即期賣出，小數點後三位的四位數字
	refreshtime = models.DateTimeField(auto_now=True) #牌告更新時間
	currencytype = models.ForeignKey(CurrencyPack) #屬於貨幣類型，因為要歷史紀錄，一種貨幣會記錄很多，使用最新的紀錄

class BankPackAdmin(admin.ModelAdmin):
	list_display = ('bankcode','bankname','bankphone','bankaddress','goatm')
	ordering = ('bankcode',)

class ExATMAdmin(admin.ModelAdmin):
	list_display = ('city','bank','location','atmaddr')
	list_filter = ('city',)

class CurrencyPackAdmin(admin.ModelAdmin):
	list_display = ('currencyname','currencyname','currencycode','get_usecountry','currencyunit','callspotbuy')


admin.site.register(BankPack,BankPackAdmin)
admin.site.register(ExATM,ExATMAdmin)
admin.site.register(CurrencyPack,CurrencyPackAdmin)

from django.contrib import admin
from polls.models import Choice, Poll

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 1

class PollAdmin(admin.ModelAdmin):
	fieldset = [
				(None,					{'fields': ['question']}),
				('Date Information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question']
	date_heirarchy = ['pub_date']

admin.site.register(Poll, PollAdmin)
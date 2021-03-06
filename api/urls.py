from django.conf.urls import url
from .views import UserView,ScheduleView, MarkPresenceView, EventView, CheckRegistrationView, RegisterForTeamEventView, RegisterForSingleEventView, MessageFromTeamView,EventCategoryView, SaveDeviceTokenView

app_name = 'api'

urlpatterns = [
	url(r'^user/$', UserView.as_view(), name='user'),
	url(r'^event-categories/$', EventCategoryView.as_view(), name='EventCategoryView'),

	url(r'^events/$', EventView.as_view(), name='events'),
	url(r'^check-registration/$', CheckRegistrationView.as_view(), name='CheckRegistration'),
	url(r'^register-for-team-event/$', RegisterForTeamEventView.as_view(), name='RegisterForTeamEventView'),
	url(r'^register-for-single-event/$', RegisterForSingleEventView.as_view(), name='RegisterForSingleEventView'),
	url(r'^message-from-team/$', MessageFromTeamView.as_view(), name='MessageFromTeamView'),
	url(r'^device-token/$', SaveDeviceTokenView.as_view(), name='SaveDeviceTokenView'),
	url(r'^mark-presence/$', MarkPresenceView.as_view(), name='MarkPresenceView'),
	url(r'^schedule/$', ScheduleView.as_view(), name='ScheduleView'),

	]
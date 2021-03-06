from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('email-view/', EmailInboxView.as_view(), name='email_view'),
    path('new-email/', AddNewEmail.as_view(), name='new_email'),
    path('#sentbox/', EmailSentboxView.as_view(), name='email_sentbox'),
    path('#drafts/', EmailDraftsView.as_view(), name='email_drafts'),
    path('#archive/', EmailArchiveView.as_view(), name='email_archive'),
    path('#archive-add/<int:email_id>/', EmailArchiveAdd.as_view(), name='add_email_archive'),
    path('detail/<int:email_id>/', DetailEmailView.as_view(), name='detail_email'),
    path('add-label/', AddLabelView.as_view(), name='add_label'),
    path('add-label-filter/', AddLabelFilter.as_view(), name='add_label_filter'),
    path('#trash/', EmailTrashView.as_view(), name='email_trash'),
    path('delete-email/<int:email_id>/', DeleteEmail.as_view(), name='delete_email'),
    path('detail_label/<int:label_id>/', DetailLabel.as_view(), name='detail_label'),
    path('label_delete/<int:label_id>/', DeleteLabel.as_view(), name='label_delete'),
    path('add-email-to-label/<int:email_id>/<int:label_id>/', AddLabelEmail.as_view(), name='email_to_label'),
    path('label_view/', LabelView.as_view(), name='label_view'),
    path('search/', Search.as_view(), name='search'),
    path('setting/', Setting.as_view(), name='setting'),
    path('search-email/', csrf_exempt(search_email), name="search_email"),
    path('change-theme/', ChangeTheme.as_view(), name="change_theme"),

    # path('delete-email/', trash_email, name='trash'),

]

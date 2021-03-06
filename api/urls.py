from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from . import views as api_views

api_router = routers.DefaultRouter()

api_router.register("dogs", api_views.DogViewSet, basename="dog")
api_router.register("users", api_views.UserViewSet, basename="user")
api_router.register(
    "conversations", api_views.ConversationViewSet, basename="conversation"
)
api_router.register("messages", api_views.MessageViewSet, basename="message")
api_router.register("meetups", api_views.MeetupViewSet, basename="meetup")
api_router.register("locations", api_views.LocationViewSet, basename="location")
api_router.register("posts", api_views.PostViewSet, basename="post")
api_router.register("comments", api_views.CommentViewSet, basename="comment")
api_router.register(
    "discussionboards", api_views.DiscussionBoardViewSet, basename="discussionboard"
)
api_router.register("notes", api_views.NoteViewSet, basename="note")
api_router.register("websockets", api_views.SocketViewSet, basename="websocket")
api_router.register(
    "notifications", api_views.NotificationViewSet, basename="notifications"
)
api_router.register("requests", api_views.RequestViewSet, basename="request")
api_router.register("reactions", api_views.ReactionViewSet, basename="reaction")


urlpatterns = [
    path("", include(api_router.urls)),
]
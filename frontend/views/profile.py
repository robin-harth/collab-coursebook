"""Purpose of this file

This file describes the frontend views related to profiles.
"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.utils.translation import gettext_lazy as _

from base.models import Profile
from base.models.profile import UserPreference

from frontend.forms.profile import AddProfile, AddPreference


class ProfileView(LoginRequiredMixin, DetailView):
    """Profile view

    This model represents the profiles view of the user.

    :attr ProfileView.model: The model of the view
    :type ProfileView.model: Model
    :attr ProfileView.template_name: The path to the html template
    :type ProfileView.template_name: str
    :attr ProfileView.context_object_name: The context object name
    :type ProfileView.context_object_name: str
    """
    model = Profile
    template_name = "frontend/profile/profile.html"
    context_object_name = "profile"

    def get_context_data(self, **kwargs):
        """Context data

        Gets the context data of the view which can be accessed in
        the html templates.

        :param kwargs: The additional arguments
        :type kwargs: dict[str, Any]

        :return: the context data
        :rtype: dict[str, Any]
        """
        context = super().get_context_data(**kwargs)
        content = self.get_object()
        context['user'] = self.request.user
        try:
            content_file = UserPreference.objects.get(user=context['profile'])
        except:
            content_file = UserPreference.objects.create(user=context['profile'])
        #context['user_preference_form'] = AddPreference(initial={'language': content_file.language})
        context['user_preference_language'] = 'German' if (content_file.language == 'de') else 'English'
        return context


class ProfileEditView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    """Profile view

    This model represents the editing profiles view of the user.

    :attr ProfileEditView.model: The model of the view
    :type ProfileEditView.model: Model
    :attr ProfileEditView.template_name: The path to the html template
    :type ProfileEditView.template_name: str
    :attr ProfileEditView.fields: Including fields into the form
    :type ProfileEditView.fields: list[str]
    """
    model = Profile
    form_class = AddProfile
    template_name = "frontend/profile/profile_edit.html"

    def get_success_url(self):
        """Success URL

        Returns the url for successful editing of the profile.

        :return:  the url for successful editing of the profile
        :rtype: __proxy__
        """
        return reverse_lazy('frontend:profile', kwargs={'pk': self.request.user.pk})

    def get_success_message(self, cleaned_data):
        """Success message

        Returns the success message when the profile was updated

        :param cleaned_data: The cleaned data
        :type cleaned_data: dict[str, Any]

        :return: the success message when the profile was updated
        :rtype: __proxy__
        """
        return _("Profile updated")

    def get_object(self, queryset=None):
        """Get object

        Returns the profile object of this user profile.

        :param queryset: The given queryset
        :type queryset: QuerySet

        :return: the profile object of this user
        :rtype: Profile
        """
        return Profile.objects.get(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['user'] = self.request.user
        try:
            content_file = UserPreference.objects.get(user=context['profile'])
        except:
            content_file = UserPreference.objects.create(user=context['profile'])
        context['user_preference_form'] = AddPreference(initial={'language': content_file.language})

        return context

    def post(self, request, *args, **kwargs):
        """Post

        Defines the action after a post request.

        :param request: The given request
        :type request: HttpRequest
        :param args: The arguments
        :type args: Any
        :param kwargs: The keyword arguments
        :type kwargs: dict[str, Any]

        :return: the response after a post request
        :rtype: HttpResponseRedirect
        """
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            form.save()
        UserPreference.objects.filter(user=request.user.profile).update(language=request.POST['language'])


        # Redirect to error page (should not happen for valid content types)
        return HttpResponseRedirect(self.get_success_url())
from django.shortcuts import render_to_response, redirect
from system.models import CustomUser
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import BaseUserManager
from django import forms
from system.controllers.postFinishView import finish


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = CustomUser
        fields = ("username",)


    def save(self, commit=True):
        print(" === save === ")
        user = super(RegisterForm, self).save(commit=False)
        user.email = BaseUserManager.normalize_email(self.cleaned_data["email"])
        if commit:
            user.save()
        return user


def userRegister(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(" === create user === :" +str(form.cleaned_data["username"]))
            form.save()
            return redirect(reverse("system:finish_register"))
        return redirect(reverse("system:user_register"))
    return userRegisterView(request)


def userRegisterView(request):
    return render_to_response("userRegisterView.html", RequestContext(request, {
        "register_forms": RegisterForm(),
        }))


def finishUserRegisterView(request):
    return render_to_response("postFinishView.html", RequestContext(request, {
        "message": "ユーザー登録",
        }))

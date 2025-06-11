from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group

class SignUpForm(UserCreationForm):
    group = forms.ModelChoiceField(
        queryset=Group.objects.none(),
        required=True,
        label="Groupe d'utilisateur"
    )

    add_admin_permission = forms.BooleanField(
        required=False,
        label="Donner l'accès Admin (staff)",
        help_text="Cochez pour donner l'accès au panneau d'administration."
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "group", "add_admin_permission")

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            if user.groups.filter(name="Market").exists():
                self.fields['group'].queryset = Group.objects.filter(name="Test Clients")
            elif user.groups.filter(name="SuperAdmin").exists():
                self.fields['group'].queryset = Group.objects.all()
            else:
                self.fields['group'].queryset = Group.objects.none()

            # N'affiche le champ que si le créateur est dans le groupe "SuperAdmin"
            if not user.groups.filter(name="SuperAdmin").exists():
                self.fields.pop('add_admin_permission')
        else:
            self.fields['group'].queryset = Group.objects.none()
            self.fields.pop('add_admin_permission')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            # Attribuer le statut staff si demandé
            if 'add_admin_permission' in self.cleaned_data and self.cleaned_data['add_admin_permission']:
                user.is_staff = True
            user.save()
            # Ajouter l'utilisateur au groupe sélectionné
            group = self.cleaned_data['group']
            user.groups.add(group)
        return user

from django import forms

# Admin forms
class CreateTournamentForm(forms.Form):
    start_time = forms.DateTimeField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    end_time = forms.DateTimeField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    respin_start_time = forms.DateTimeField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    respin_end_time = forms.DateTimeField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    respin_price = forms.FloatField()
    max_players = forms.IntegerField()

    def save(self, commit=True):
        tournament = super().save(commit=False)
        tournament.start_time = self.cleaned_data['start_time']
        tournament.end_time = self.cleaned_data['end_time']
        tournament.respin_start_time = self.cleaned_data['respin_start_time']
        tournament.respin_end_time = self.cleaned_data['respin_end_time']
        tournament.entry_fee = self.cleaned_data['entry_fee']

        if commit:
            tournament.save()
        return tournament
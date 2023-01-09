from django import forms


class EntryEditor(forms.Form):

    template_name = 'encyclopedia/editor_form.html'

    entry_title = forms.CharField(label='Entry Title', max_length=100, min_length=1)
    entry_content = forms.CharField(label='Entry Content', widget=forms.Textarea)

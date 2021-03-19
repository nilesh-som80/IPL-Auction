from django import forms
from .models import Player,TEST_STATS,T20I_STATS,ODI_STATS,IPL_STATS

class PlayerForm(forms.ModelForm):
    
    class Meta:
        model = Player
        exclude = ("Player_img_1","Player_img_2")
    
    def __init__(self, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class TEST_STATSForm(forms.ModelForm):
    
    class Meta:
        model = TEST_STATS
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(TEST_STATSForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class T20I_STATSForm(forms.ModelForm):
    
    class Meta:
        model = T20I_STATS
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(T20I_STATSForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class ODI_STATSForm(forms.ModelForm):
    
    class Meta:
        model = ODI_STATS
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(ODI_STATSForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

class IPL_STATSForm(forms.ModelForm):
    
    class Meta:
        model = IPL_STATS
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(IPL_STATSForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    

class ActiveForm(forms.ModelForm):
    
    class Meta:
        model = Player
        fields = ["active"]
    




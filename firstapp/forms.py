from django import forms

class Payment(forms.Form):
      name = forms.CharField(label=' Name', max_length=100)
      amount =forms.IntegerField()
      product = forms.CharField(max_length=300)

      def __str__(self):
        return self.name
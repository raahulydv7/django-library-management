from django import forms
from .models import Books,BorrowBook,BookBorrowHistory
from datetime import timedelta
from django.utils import timezone
class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title','author','description','image','quantity']
    
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowBook
        fields = []
    
    def save(self, commit = True):
        borrow =  super().save(commit= False)
        if not borrow.due_date:
            borrow.due_date = timezone.now().date() + timedelta(days=7)
        if commit:
            borrow.save()
        return borrow
    
class BookBorrowHistoryForm(forms.ModelForm):
    class Meta:
        model = BookBorrowHistory
        fields = ['action']
class BorrowBookReturnForm(forms.ModelForm):
    return_action = forms.ChoiceField()
    class Meta:
        model = BorrowBook
        fields = ['return_date','returned','return_action']
    
            
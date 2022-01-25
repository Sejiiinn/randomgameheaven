from django.contrib.auth.forms import PasswordChangeForm

class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm,self).__init__(*args, **kwargs)
        self.fileds['old_pw'].label = '현재 비밀번호'
        self.fileds['old_pw'].widget.attrs.update({
            'class': 'form-control',
            'autofocus':False,
        })
        self.fileds['new_pw'].label = '변경할 비밀번호'
        self.fileds['new_pw'].widget.attrs.update({
            'class':'form-control'
        })
        self.fileds['new2_pw'].label = '비밀번호 재확인'
        self.fileds['new2_pw'].widget.attrs.update({
            'class':'form-control'
        })
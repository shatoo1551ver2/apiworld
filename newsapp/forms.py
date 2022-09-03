from django import forms

class ApiForm(forms.Form):
    name= forms.CharField(label='name',max_length=1000)
    describe= forms.CharField(label='describe',max_length=1000)
    url= forms.URLField(label='url')
    usrname= forms.CharField(label='usrname')
    apikey=forms.CharField(label='apikey')

class NewsAPIForm(forms.Form):
    keyword= forms.CharField(label='keyword')
    # sortBy= forms.CharField(label='sortBy')
    pageSize= forms.CharField(label='pageSize')

class DeepLForm(forms.Form):
    source_lang= forms.CharField(label='source_lang')
    target_lang= forms.CharField(label='target_lang')
    text= forms.CharField(label='text')



# BooleanField	CheckboxInput	required=True の場合、チェックされていることを確認する	required
# CharField	TextInput	max_length, min_length	required, max_length, min_length
# ChoiceField	Select	値が存在するかどうかチェックする	required, invalid_choice
# TypedChoiceField	Select	値が存在するかどうかチェックし、それが coerce で指定した型できるかチェックする	required, invalid_choice
# DateField	DateInput	datetime.date, datetime.datetime または input_formats で指定したフォーマットであるかチェック
# input_formats は '%m/%d/%y', '%B %d, %Y' などを指定。	required, invalid
# DateTimeField	DateTimeInput	datetime.date, datetime.datetime または input_formats で指定したフォーマットであるかチェック
# input_formats は '%m/%d/%y %H:%M:%S' 等を指定	required, invalid
# DecimalField	TextInput	値が decimal かチェックする	required, invalid, max_value, min_value, max_digits, max_decimal_places, max_whole_digits
# EmailField	TextInput	メールアドレス	required
# FileField	ClearableFileInput	ファイルアップロード	required, invalid, missing, empty
# FilePathField	Select		required, invalid_choice
# FloatField	TextInput		required, invalid_choice
# ImageField	TextInput	int 値であることをチェック	required, invalid, max_value, min_value
# IPAddressField	TextInput	IPv4 の値であることをチェック	required, invalid
# MultipleChoiceField	SelectMultiple	Unicode オブジェクトのリストであることをチェック	required, invalid_choice, invalid_list
# NullBooleanField	NullBooleanSelect		
# RegexField	TextInput		required, invalid
# SlugField	TextInput	文字、数字、アンダースコア、ハイフンのみを含むことをチェック	required, invalid
# TimeField	TextInput	datetime.time	required, invalid
# URLField	TextInput	
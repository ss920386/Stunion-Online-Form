from django import forms
from django.db import models
from .models import Reflection, Reply

def set_field_html_name(cls, new_name):
    """
    This creates wrapper around the normal widget rendering, 
    allowing for a custom field name (new_name).
    """
    old_render = cls.widget.render
    def _widget_render_wrapper(name, value, attrs=None):
        return old_render(new_name, value, attrs)

    cls.widget.render = _widget_render_wrapper

class ReflectionForm(forms.ModelForm):
    class Meta:
        model = Reflection
        fields = ['name','email','category','content','advice']
        help_texts = {
            'content': '最多500字',
            'advice': '最多500字',
        }
        labels = {
            'name': '姓名(非必填)',
            'email': '信箱地址',
            'category': '類別',
            'content': '意見內容',
            'advice': '建議方向',
        }

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['user','content']
        help_texts = {
            'content': '最多500字',
        }
        labels = {
            'user': '回覆人',
            'content': '意見內容',
        }
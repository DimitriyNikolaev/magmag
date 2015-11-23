# -*- coding: utf-8 -*-
__author__ = 'dimitriy'
from django.forms.models import inlineformset_factory
from django.forms import ModelForm
from magmag_core.apps.catalogue.models import Category, Store, Product, ProductImage
from magmag_core.global_utils.image_utils import get_thumbnail, get_preview


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = "__all__"


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"


class ProductImageForm(ModelForm):
    class Meta:
        model = ProductImage
        exclude = ('preview', 'thumbnail',)

    def save(self, *args, **kwargs):
        # # We infer the display order of the image based on the order of the
        # # image fields within the formset.

        kwargs['commit'] = False
        obj = super(ProductImageForm, self).save(*args, **kwargs)
        if not obj.preview:
            preview = get_preview(self.cleaned_data['original'], 'preview')
            obj.preview.save(preview.name, preview)
            self.cleaned_data['original'].seek(0)
            thumbnail = get_thumbnail(self.cleaned_data['original'], 'thumbnail')
            obj.thumbnail.save(thumbnail.name, thumbnail)
        obj.save()
        return obj




BaseProductImageFormSet = inlineformset_factory(
    Product, ProductImage, form=ProductImageForm)


class ProductImageFormSet(BaseProductImageFormSet):
    def __init__(self, product_class, user, *args, **kwargs):
        super(ProductImageFormSet, self).__init__(*args, **kwargs)
from apps.bluebottle_drf2.serializers import PolymorphicSerializer
from apps.cowry_docdata.models import DocDataWebMenu, DocDataWebDirectDirectDebit
from rest_framework import serializers
from .models import DocDataPayment


class DocDataOrderProfileSerializer(serializers.ModelSerializer):
    # # TODO Generate country list from docdata api and use ChoiceField.
    # country = serializers.CharField(required=True)
    id = serializers.Field(source='payment_ptr_id')
    country = serializers.CharField(required=True)

    class Meta:
        model = DocDataPayment
        fields = ('id', 'first_name', 'last_name', 'email', 'street', 'city', 'postal_code', 'country')


class DocDataPaymentMethodSerializerBase(serializers.ModelSerializer):
    id = serializers.Field(source='docdatapaymentmethod_ptr_id')

    class Meta:
        fields = ('id', )


class DocDataWebMenuSerializer(DocDataPaymentMethodSerializerBase):
    class Meta:
        model = DocDataWebMenu
        fields = DocDataPaymentMethodSerializerBase.Meta.fields + ('payment_url',)


class DocDataWebDirectDirectDebitSerializer(DocDataPaymentMethodSerializerBase):
    class Meta:
        model = DocDataWebDirectDirectDebit
        fields = DocDataPaymentMethodSerializerBase.Meta.fields + ('bank_account_number', 'bank_account_name', 'bank_account_city')


class DocDataPaymentMethodSerializer(PolymorphicSerializer):
    class Meta:
        child_models = (
            (DocDataWebMenu, DocDataWebMenuSerializer),
            (DocDataWebDirectDirectDebit, DocDataWebDirectDirectDebitSerializer),
        )

from rest_framework import serializers
from .models import ReportField, ReportPage, Class, DevelopmentPage, Choice, LearningOutcome, Section


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'


class LearningOutcomeSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer(many=True)

    class Meta:
        model = LearningOutcome
        fields = '__all__'


class SectionSerializer(serializers.ModelSerializer):
    learning_outcome = LearningOutcomeSerializer(many=True)

    class Meta:
        model = Section
        fields = '__all__'

class DevelopmentPageSerializer(serializers.ModelSerializer):
    sections = SectionSerializer(many=True)

    class Meta:
        model = DevelopmentPage
        fields = '__all__'


class ReportFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportField
        fields = '__all__'


class ReportPageSerializer(serializers.ModelSerializer):
    report_fields = ReportFieldSerializer(many=True)

    class Meta:
        model = ReportPage
        fields = '__all__'


class ClassSerializer(serializers.ModelSerializer):
    cover_page = ReportPageSerializer()
    first_page = ReportPageSerializer()
    development_page = DevelopmentPageSerializer(many=True)


    class Meta:
        model = Class
        fields = '__all__'

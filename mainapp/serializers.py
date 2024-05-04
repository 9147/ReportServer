from rest_framework import serializers
from .models import ReportField, ReportPage, Class, DevelopmentPage, Choice, LearningOutcome, Section, FeedbackField, FeedbackFieldsChoice, FeedbackPage, FeedbackSection, Signature, Image , ImagePage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ImagePageSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)

    class Meta:
        model = ImagePage
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = '__all__'

class FeedbackFieldsChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedbackFieldsChoice
        fields = '__all__'

class FeedbackFieldSerializer(serializers.ModelSerializer):
    options = FeedbackFieldsChoiceSerializer(many=True)

    class Meta:
        model = FeedbackField
        fields = '__all__'

class FeedbackSectionSerializer(serializers.ModelSerializer):
    Fields = FeedbackFieldSerializer(many=True)

    class Meta:
        model = FeedbackSection
        fields = '__all__'
    
class SignatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signature
        fields = '__all__'

class FeedbackPageSerializer(serializers.ModelSerializer):
    sections = FeedbackSectionSerializer(many=True)
    signature = SignatureSerializer(many=True)

    class Meta:
        model = FeedbackPage
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
    Image_page = ImagePageSerializer()
    development_page = DevelopmentPageSerializer(many=True)
    feedback_page = FeedbackPageSerializer()


    class Meta:
        model = Class
        fields = '__all__'

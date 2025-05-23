from rest_framework import serializers
from .models import (InteriorDesignService, Expertise, Methodology,
                     FitOutService, FitOutExpertise, TransformationProcess, SpecializedService, MoreInformationSection,
                     ArchitectureService, AdditionalExpertise, WorkProcess, ArchitecturalService)


class ExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expertise
        fields = '__all__'


class MethodologySerializer(serializers.ModelSerializer):
    class Meta:
        model = Methodology
        fields = '__all__'


class InteriorDesignServiceSerializer(serializers.ModelSerializer):
    expertises = ExpertiseSerializer(many=True)
    methodologies = MethodologySerializer(many=True)

    class Meta:
        model = InteriorDesignService
        fields = '__all__'
        depth = 1


class FitOutExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitOutExpertise
        fields = '__all__'


class TransformationProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransformationProcess
        fields = '__all__'


class SpecializedServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecializedService
        fields = '__all__'


class MoreInformationSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoreInformationSection
        fields = '__all__'


class FitOutServiceSerializer(serializers.ModelSerializer):
    fit_out_expertises = FitOutExpertiseSerializer(many=True)
    transformation_processes = TransformationProcessSerializer(many=True)
    specialized_services = SpecializedServiceSerializer(many=True)
    more_information_sections = MoreInformationSectionSerializer(many=True)

    class Meta:
        model = FitOutService
        fields = '__all__'
        depth = 1


class AdditionalExpertiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalExpertise
        fields = '__all__'


class WorkProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkProcess
        fields = '__all__'


class ArchitecturalServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchitecturalService
        fields = '__all__'


class ArchitectureServiceSerializer(serializers.ModelSerializer):
    additional_expertises = AdditionalExpertiseSerializer(many=True)
    work_processes = WorkProcessSerializer(many=True)
    architectural_services = ArchitecturalServiceSerializer(many=True)

    class Meta:
        model = ArchitectureService
        fields = '__all__'
        depth = 1
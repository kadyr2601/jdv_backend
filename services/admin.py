from django.contrib import admin
from services.models import (InteriorDesignService, Expertise, Methodology, FitOutService, FitOutExpertise,
                             TransformationProcess, SpecializedService, MoreInformationSection, ArchitectureService,
                             AdditionalExpertise, WorkProcess, ArchitecturalService)


class ExpertiseInline(admin.StackedInline):
    model = Expertise
    extra = 1


class MethodologyInline(admin.StackedInline):
    model = Methodology
    extra = 1


@admin.register(InteriorDesignService)
class InteriorDesignServiceAdmin(admin.ModelAdmin):
    inlines = [ExpertiseInline, MethodologyInline]


class FitOutExpertiseInline(admin.StackedInline):
    model = FitOutExpertise
    extra = 1


class TransformationProcessInline(admin.StackedInline):
    model = TransformationProcess
    extra = 1


class SpecializedServiceInline(admin.StackedInline):
    model = SpecializedService
    extra = 1


class MoreInformationSectionInline(admin.StackedInline):
    model = MoreInformationSection
    extra = 1


@admin.register(FitOutService)
class FitOutServiceAdmin(admin.ModelAdmin):
    inlines = [FitOutExpertiseInline, TransformationProcessInline, SpecializedServiceInline, MoreInformationSectionInline]


class AdditionalExpertiseInline(admin.StackedInline):
    model = AdditionalExpertise
    extra = 1


class WorkProcessInline(admin.StackedInline):
    model = WorkProcess
    extra = 1


class ArchitecturalServiceInline(admin.StackedInline):
    model = ArchitecturalService
    extra = 1


@admin.register(ArchitectureService)
class ArchitectureServiceAdmin(admin.ModelAdmin):
    inlines = [AdditionalExpertiseInline, WorkProcessInline, ArchitecturalServiceInline]
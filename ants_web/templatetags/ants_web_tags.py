from django import template

register = template.Library()


@register.filter(name='has_student_joined_course')
def has_student_joined_course(student, course):
    return student.has_joined_course(course)


@register.filter(name='get_element')
def get_element(dictionary, index):
    return dictionary.get(index)

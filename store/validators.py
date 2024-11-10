from django.core.exceptions import ValidationError

def file_size_validate(file):
    max_size = 50

    if file.size > max_size *1024:
        raise ValidationError(f'very big . the file size must be less then {max_size}KB!')
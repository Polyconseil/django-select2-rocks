import select2rocks


class MultipleBeachesChoiceField(select2rocks.Select2ModelMultipleChoiceField):

    def clean(self, value):
        # select2 gives us a CSV line, Django wants a list
        return super(MultipleBeachesChoiceField, self).clean(value.split(','))

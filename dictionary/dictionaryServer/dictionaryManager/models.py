from django.db import models


class Dictionary(models.Model):
    class Meta:
        db_table = "DICTIONARY_INFO"

    word = models.CharField(db_column='WORD', max_length=100)
    definition = models.CharField(db_column='DEFINITION', max_length=100)
    example = models.CharField(db_column='EXAMPLE', max_length=100)
    pos = models.CharField(db_column='PART_OF_SPEECH', max_length=100)

    '''
    def __str__(self):
        return self.word
    '''
